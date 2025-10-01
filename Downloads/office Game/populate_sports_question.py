from app import app
from models import db, Category, Question

with app.app_context():
    # Get or create category
    sports_category = Category.query.filter_by(name="Sports").first()
    if not sports_category:
        sports_category = Category(name="Sports", description="Sports trivia questions")
        db.session.add(sports_category)
        db.session.commit()

    # 20 Sports category questions
    sports_questions = [
        {"question_text": "Which country won the FIFA World Cup in 2018?", 
         "option_a": "Germany", "option_b": "Brazil", "option_c": "France", "option_d": "Argentina", "correct_option": "C"},
        
        {"question_text": "How many players are there in a cricket team?", 
         "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "9", "correct_option": "B"},
        
        {"question_text": "Which sport is Michael Jordan famous for?", 
         "option_a": "Football", "option_b": "Tennis", "option_c": "Basketball", "option_d": "Baseball", "correct_option": "C"},
        
        {"question_text": "In which sport is the term 'Love' used?", 
         "option_a": "Tennis", "option_b": "Cricket", "option_c": "Football", "option_d": "Hockey", "correct_option": "A"},
        
        {"question_text": "Who won the first Cricket World Cup in 1975?", 
         "option_a": "Australia", "option_b": "India", "option_c": "West Indies", "option_d": "England", "correct_option": "C"},
        
        {"question_text": "How many rings are there in the Olympic logo?", 
         "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_option": "B"},
        
        {"question_text": "Which country is known as the birthplace of the Olympic Games?", 
         "option_a": "Italy", "option_b": "Greece", "option_c": "France", "option_d": "Germany", "correct_option": "B"},
        
        {"question_text": "Who is known as the 'God of Cricket'?", 
         "option_a": "Virat Kohli", "option_b": "Sachin Tendulkar", "option_c": "Ricky Ponting", "option_d": "MS Dhoni", "correct_option": "B"},
        
        {"question_text": "Which sport uses a shuttlecock?", 
         "option_a": "Tennis", "option_b": "Squash", "option_c": "Badminton", "option_d": "Table Tennis", "correct_option": "C"},
        
        {"question_text": "Which country has won the most FIFA World Cups?", 
         "option_a": "Italy", "option_b": "Brazil", "option_c": "Germany", "option_d": "Argentina", "correct_option": "B"},
        
        {"question_text": "In basketball, how many points is a free throw worth?", 
         "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_option": "A"},
        
        {"question_text": "Who holds the record for the most Olympic gold medals?", 
         "option_a": "Usain Bolt", "option_b": "Michael Phelps", "option_c": "Carl Lewis", "option_d": "Simone Biles", "correct_option": "B"},
        
        {"question_text": "What is the national sport of Canada?", 
         "option_a": "Ice Hockey", "option_b": "Lacrosse", "option_c": "Baseball", "option_d": "Basketball", "correct_option": "B"},
        
        {"question_text": "In which year did India win its first Cricket World Cup?", 
         "option_a": "1975", "option_b": "1983", "option_c": "1987", "option_d": "1992", "correct_option": "B"},
        
        {"question_text": "What is the maximum score in a single frame of snooker?", 
         "option_a": "147", "option_b": "150", "option_c": "155", "option_d": "200", "correct_option": "A"},
        
        {"question_text": "Which tennis player is known as 'King of Clay'?", 
         "option_a": "Roger Federer", "option_b": "Rafael Nadal", "option_c": "Novak Djokovic", "option_d": "Andy Murray", "correct_option": "B"},
        
        {"question_text": "How long is a standard marathon?", 
         "option_a": "21.1 km", "option_b": "30 km", "option_c": "42.195 km", "option_d": "50 km", "correct_option": "C"},
        
        {"question_text": "Which country hosts the Wimbledon tennis tournament?", 
         "option_a": "USA", "option_b": "Australia", "option_c": "France", "option_d": "United Kingdom", "correct_option": "D"},
        
        {"question_text": "In football (soccer), how many players are on the field for one team?", 
         "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "9", "correct_option": "B"},
        
        {"question_text": "Who won the Ballon d'Or in 2023?", 
         "option_a": "Lionel Messi", "option_b": "Cristiano Ronaldo", "option_c": "Kylian Mbappe", "option_d": "Erling Haaland", "correct_option": "A"}
    ]

    # Add questions to DB if not already present
    for q in sports_questions:
        if not Question.query.filter_by(question_text=q["question_text"]).first():
            new_q = Question(
                category_id=sports_category.id,
                question_text=q["question_text"],
                option_a=q["option_a"],
                option_b=q["option_b"],
                option_c=q["option_c"],
                option_d=q["option_d"],
                correct_option=q["correct_option"]
            )
            db.session.add(new_q)

    db.session.commit()
    print("20 Sports category questions added!")
