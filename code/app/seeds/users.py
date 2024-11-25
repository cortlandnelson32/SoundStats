from app.models import db, User, environment, SCHEMA
from werkzeug.security import generate_password_hash
from sqlalchemy.sql import text

def seed_users():
    users = [
        User(
            email='demo@user.io',
            username='DemoUser',
            hashed_password=generate_password_hash('password'),
            first_name='Demo',
            last_name='User',
        ),
        User(
            email='jane.doe@example.com',
            username='JaneDoe',
            hashed_password=generate_password_hash('password2'),
            first_name='Jane',
            last_name='Doe',
        ),
        User(
            email='john.smith@example.com',
            username='JohnSmith',
            hashed_password=generate_password_hash('password3'),
            first_name='John',
            last_name='Smith',
        ),
        User(
            email='emily.brown@example.com',
            username='EmilyBrown',
            hashed_password=generate_password_hash('password4'),
            first_name='Emily',
            last_name='Brown',
        ),
        User(
            email='michael.jones@example.com',
            username='MichaelJones',
            hashed_password=generate_password_hash('password5'),
            first_name='Michael',
            last_name='Jones',
        ),
        User(
            email='sarah.johnson@example.com',
            username='SarahJohnson',
            hashed_password=generate_password_hash('password6'),
            first_name='Sarah',
            last_name='Johnson',
        ),
        User(
            email='david.williams@example.com',
            username='DavidWilliams',
            hashed_password=generate_password_hash('password7'),
            first_name='David',
            last_name='Williams',
        ),
        User(
            email='olivia.miller@example.com',
            username='OliviaMiller',
            hashed_password=generate_password_hash('password8'),
            first_name='Olivia',
            last_name='Miller',
        ),
        User(
            email='william.davis@example.com',
            username='WilliamDavis',
            hashed_password=generate_password_hash('password9'),
            first_name='William',
            last_name='Davis',
        ),
        User(
            email='sophia.moore@example.com',
            username='SophiaMoore',
            hashed_password=generate_password_hash('password10'),
            first_name='Sophia',
            last_name='Moore',
        ),
        User(
            email='daniel.taylor@example.com',
            username='DanielTaylor',
            hashed_password=generate_password_hash('password11'),
            first_name='Daniel',
            last_name='Taylor',
        ),
    ]

    db.session.bulk_save_objects(users)
    db.session.commit()


def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
