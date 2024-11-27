from flask.cli import AppGroup
from .users import seed_users, undo_users
# from .music_data import seed_music_data, undo_music_data
# from .report import seed_reports, undo_reports

from app.models.db import db, environment, SCHEMA

seed_commands = AppGroup('seed')


@seed_commands.command('all')
def seed():
    if environment == 'production':
        undo_users()
        # undo_music_data()
        # undo_reports()
    seed_users()
    # seed_music_data()
    # seed_reports()


@seed_commands.command('undo')
def undo():
    undo_users()
    # undo_music_data()
    # undo_reports()
