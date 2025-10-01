from app import app
from models import db, Category, Question

with app.app_context():
    # Get category object
    fun_category = Category.query.filter_by(name="Fun").first()

    # List of 20 Fun category questions
    fun_questions = [
        {"question_text": "What is the color of the sky?", "option_a": "Blue", "option_b": "Green", "option_c": "Red", "option_d": "Yellow", "correct_option": "A"},
        {"question_text": "Which animal says 'Meow'?", "option_a": "Dog", "option_b": "Cat", "option_c": "Cow", "option_d": "Sheep", "correct_option": "B"},
        {"question_text": "How many days are there in a leap year?", "option_a": "365", "option_b": "366", "option_c": "364", "option_d": "360", "correct_option": "B"},
        {"question_text": "Which fruit is known as the 'King of Fruits'?", "option_a": "Apple", "option_b": "Mango", "option_c": "Banana", "option_d": "Pineapple", "correct_option": "B"},
        {"question_text": "Which planet is known as the Red Planet?", "option_a": "Mars", "option_b": "Jupiter", "option_c": "Venus", "option_d": "Saturn", "correct_option": "A"},
        {"question_text": "What is 10 + 15?", "option_a": "20", "option_b": "25", "option_c": "30", "option_d": "35", "correct_option": "B"},
        {"question_text": "Which animal is known as the Ship of the Desert?", "option_a": "Horse", "option_b": "Camel", "option_c": "Elephant", "option_d": "Donkey", "correct_option": "B"},
        {"question_text": "What is the freezing point of water?", "option_a": "0°C", "option_b": "100°C", "option_c": "32°C", "option_d": "-10°C", "correct_option": "A"},
        {"question_text": "Which fruit is yellow and curved?", "option_a": "Banana", "option_b": "Mango", "option_c": "Apple", "option_d": "Papaya", "correct_option": "A"},
        {"question_text": "Which color do you get when you mix red and white?", "option_a": "Pink", "option_b": "Purple", "option_c": "Orange", "option_d": "Brown", "correct_option": "A"},
        {"question_text": "What do bees make?", "option_a": "Milk", "option_b": "Honey", "option_c": "Butter", "option_d": "Cheese", "correct_option": "B"},
        {"question_text": "Which month comes after July?", "option_a": "June", "option_b": "August", "option_c": "September", "option_d": "May", "correct_option": "B"},
        {"question_text": "Which day is celebrated as Children's Day in India?", "option_a": "14th Nov", "option_b": "1st Jan", "option_c": "25th Dec", "option_d": "15th Aug", "correct_option": "A"},
        {"question_text": "Which animal is known for its black and white stripes?", "option_a": "Zebra", "option_b": "Tiger", "option_c": "Leopard", "option_d": "Giraffe", "correct_option": "A"},
        {"question_text": "How many continents are there on Earth?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_option": "C"},
        {"question_text": "Which is the largest mammal?", "option_a": "Elephant", "option_b": "Blue Whale", "option_c": "Giraffe", "option_d": "Hippopotamus", "correct_option": "B"},
        {"question_text": "Which color do you get by mixing blue and yellow?", "option_a": "Green", "option_b": "Purple", "option_c": "Orange", "option_d": "Brown", "correct_option": "A"},
        {"question_text": "Which animal is famous for its long neck?", "option_a": "Elephant", "option_b": "Giraffe", "option_c": "Camel", "option_d": "Kangaroo", "correct_option": "B"},
        {"question_text": "Which shape has three sides?", "option_a": "Square", "option_b": "Triangle", "option_c": "Rectangle", "option_d": "Circle", "correct_option": "B"},
        {"question_text": "Which is the fastest land animal?", "option_a": "Cheetah", "option_b": "Lion", "option_c": "Tiger", "option_d": "Horse", "correct_option": "A"}
    ]

    # Add questions to database
    for q in fun_questions:
        if not Question.query.filter_by(question_text=q["question_text"]).first():
            new_q = Question(
                category_id=fun_category.id,
                question_text=q["question_text"],
                option_a=q["option_a"],
                option_b=q["option_b"],
                option_c=q["option_c"],
                option_d=q["option_d"],
                correct_option=q["correct_option"]
            )
            db.session.add(new_q)

    db.session.commit()
    print("20 Fun category questions added!")
