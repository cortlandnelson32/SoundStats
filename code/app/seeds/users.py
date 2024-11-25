from app.models import db, User, environment, SCHEMA
from werkzeug.security import generate_password_hash
from sqlalchemy.sql import text

def seed_users():
    demo_user = User(
        email='demo@user.io',
        username='DemoUser',
        hashed_password=generate_password_hash('password'),
        first_name='Demo',
        last_name='User',
    )
    jane_doe = User(
        email='jane.doe@example.com',
        username='JaneDoe',
        hashed_password=generate_password_hash('password2'),
        first_name='Jane',
        last_name='Doe',
    )
    john_smith = User(
        email='john.smith@example.com',
        username='JohnSmith',
        hashed_password=generate_password_hash('password3'),
        first_name='John',
        last_name='Smith',
    )
    emily_brown = User(
        email='emily.brown@example.com',
        username='EmilyBrown',
        hashed_password=generate_password_hash('password4'),
        first_name='Emily',
        last_name='Brown',
    )
    michael_jones = User(
        email='michael.jones@example.com',
        username='MichaelJones',
        hashed_password=generate_password_hash('password5'),
        first_name='Michael',
        last_name='Jones',
    )
    sarah_johnson = User(
        email='sarah.johnson@example.com',
        username='SarahJohnson',
        hashed_password=generate_password_hash('password6'),
        first_name='Sarah',
        last_name='Johnson',
    )
    david_williams = User(
        email='david.williams@example.com',
        username='DavidWilliams',
        hashed_password=generate_password_hash('password7'),
        first_name='David',
        last_name='Williams',
    )
    olivia_miller = User(
        email='olivia.miller@example.com',
        username='OliviaMiller',
        hashed_password=generate_password_hash('password8'),
        first_name='Olivia',
        last_name='Miller',
    )
    william_davis = User(
        email='william.davis@example.com',
        username='WilliamDavis',
        hashed_password=generate_password_hash('password9'),
        first_name='William',
        last_name='Davis',
    )
    sophia_moore = User(
        email='sophia.moore@example.com',
        username='SophiaMoore',
        hashed_password=generate_password_hash('password10'),
        first_name='Sophia',
        last_name='Moore',
    )
    daniel_taylor = User(
        email='daniel.taylor@example.com',
        username='DanielTaylor',
        hashed_password=generate_password_hash('password11'),
        first_name='Daniel',
        last_name='Taylor',
    )

    db.session.add_all([
        demo_user, jane_doe, john_smith, emily_brown, michael_jones,
        sarah_johnson, david_williams, olivia_miller, william_davis,
        sophia_moore, daniel_taylor
    ])
    db.session.commit()


def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
