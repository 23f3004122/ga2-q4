from app import app
from models import db, Category

with app.app_context():
    # List of categories to add
    categories = ["Fun", "Sports", "G.K.", "Tech", "Movies", "Music"]

    for cat_name in categories:
        # Check if category already exists
        if not Category.query.filter_by(name=cat_name).first():
            new_cat = Category(name=cat_name)
            db.session.add(new_cat)
    
    db.session.commit()
    print("Categories added successfully!")
