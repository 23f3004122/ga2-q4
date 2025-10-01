from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, User , Category, Question, Game, GamePlayer, Bid

# Initialize Flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///office_game.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "supersecretkey"

db.init_app(app)
with app.app_context():
    db.create_all()  # Create tables

# -------------------- Routes -------------------- #

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash("Login successful!")
            return redirect(url_for('home'))  # go to index.html after login
        else:
            flash("Invalid email or password.")
            return redirect(url_for('login'))
    
    return render_template('login.html')


# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if email already exists
        if User.query.filter_by(email=email).first():
            flash("Email already registered!")
            return redirect(url_for('register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please login.")
        return redirect(url_for('login'))
    
    return render_template('register.html')


# Index Page (after login)
@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # redirect if not logged in

    # Here you can pass user info if needed
    user = User.query.get(session['user_id'])
    return render_template('index.html', username=user.username)


# Lobby Page
@app.route('/lobby')
def show_lobby_page():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    sample_game_code = "DEMO1"
    players = {}
    user = User.query.get(session['user_id'])
    return render_template('lobby.html', username=user.username, game_code=sample_game_code, players=players)

@app.route('/quiz/Fun')
def fun_lobby():
    category = Category.query.filter_by(name="Fun").first()
    demo_game_code = "FUN123"
    joined_players = GamePlayer.query.filter_by(game_id=1).all()  # Replace with real game id
    return render_template('Fun/fun_lobby.html', game_code=demo_game_code, players=joined_players)

@app.route('/quiz/Sports')
def sports_lobby():
    category = Category.query.filter_by(name="Sports").first()
    demo_game_code = "SPORTS123"
    joined_players = GamePlayer.query.filter_by(game_id=2).all()
    return render_template('Sports/sports_lobby.html',
                           game_code=demo_game_code,
                           players=joined_players)


@app.route('/fun/start', methods=['GET', 'POST'])
def start_fun_quiz():
    fun_category = Category.query.filter_by(name="Fun").first()
    questions = Question.query.filter_by(category_id=fun_category.id).all()

    if request.method == 'POST':
        results = []
        score = 0

        for q in questions:
            selected_option = request.form.get(f"question_{q.id}")
            is_correct = (selected_option == q.correct_option)

            if is_correct:
                score += 1

            results.append({
                "question_text": q.question_text,
                "options": {
                    "A": q.option_a,
                    "B": q.option_b,
                    "C": q.option_c,
                    "D": q.option_d
                },
                "correct_option": q.correct_option,
                "selected_option": selected_option,
                "is_correct": is_correct
            })

        # ✅ Update user's total score in User table
        user_id = session.get("user_id")  
        if user_id:
            user = User.query.get(user_id)
            if user:
                user.score += score  # add to existing score
                db.session.commit()

        # Render result page
        return render_template(
            "Fun/fun_results.html",
            results=results,
            score=score,
            total=len(questions)
        )

    return render_template("Fun/fun_quiz.html", questions=questions)

    return render_template('Fun/fun_quiz.html', questions=questions)


@app.route('/sports/start', methods=['GET', 'POST'])
def start_sports_quiz():
    sports_category = Category.query.filter_by(name="Sports").first()
    questions = Question.query.filter_by(category_id=sports_category.id).all()

    if request.method == 'POST':
        results = []
        score = 0

        for q in questions:
            selected_option = request.form.get(f"question_{q.id}")

            if selected_option:  # User attempted the question
                if selected_option == q.correct_option:
                    score += 100   # ✅ Correct
                    is_correct = True
                else:
                    score -= 50    # ❌ Wrong
                    is_correct = False
            else:
                is_correct = False  # Not attempted
                # score += 0 (no change)

            results.append({
                "question_text": q.question_text,
                "options": {
                    "A": q.option_a,
                    "B": q.option_b,
                    "C": q.option_c,
                    "D": q.option_d
                },
                "correct_option": q.correct_option,
                "selected_option": selected_option,
                "is_correct": is_correct
            })

        # ✅ Update user's total score in User table
        user_id = session.get("user_id")  
        if user_id:
            user = User.query.get(user_id)
            if user:
                user.score += score
                db.session.commit()

        # Render result page
        return render_template(
            "Sports/sports_results.html",
            results=results,
            score=score,
            total=len(questions)
        )

    return render_template("Sports/sports_quiz.html", questions=questions)


# Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Logged out successfully.")
    return redirect(url_for('login'))


# -------------------- Run Server -------------------- #
if __name__ == '__main__':
    app.run(debug=True)
