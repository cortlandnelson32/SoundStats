from app.models import db, MusicData, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


def seed_music_data():
  music_data_entries = [
    MusicData(
        title='Blinding Lights',
        artist='The Weeknd',
        genre='Pop',
        release_date=datetime.strptime('2019-11-29', '%Y-%m-%d'),
        streams=3200000000,
        sales=5000000,
        region='Global'
    ),
    MusicData(
        title='Shape of You',
        artist='Ed Sheeran',
        genre='Pop',
        release_date=datetime.strptime('2017-01-06', '%Y-%m-%d'),
        streams=3100000000,
        sales=4000000,
        region='Global'
    ),
    MusicData(
        title='Bad Guy',
        artist='Billie Eilish',
        genre='Alternative',
        release_date=datetime.strptime('2019-03-29', '%Y-%m-%d'),
        streams=1900000000,
        sales=3000000,
        region='North America'
    ),
    MusicData(
        title='Levitating',
        artist='Dua Lipa',
        genre='Pop',
        release_date=datetime.strptime('2020-03-27', '%Y-%m-%d'),
        streams=1800000000,
        sales=2500000,
        region='Europe'
    ),
    MusicData(
        title='Smells Like Teen Spirit',
        artist='Nirvana',
        genre='Rock',
        release_date=datetime.strptime('1991-09-10', '%Y-%m-%d'),
        streams=1200000000,
        sales=1500000,
        region='North America'
    ),
    MusicData(
        title='Bohemian Rhapsody',
        artist='Queen',
        genre='Rock',
        release_date=datetime.strptime('1975-10-31', '%Y-%m-%d'),
        streams=1500000000,
        sales=7000000,
        region='Global'
    ),
    MusicData(
        title='Old Town Road',
        artist='Lil Nas X',
        genre='Hip-Hop',
        release_date=datetime.strptime('2019-12-03', '%Y-%m-%d'),
        streams=2000000000,
        sales=3000000,
        region='North America'
    ),
    MusicData(
        title='Rolling in the Deep',
        artist='Adele',
        genre='Pop',
        release_date=datetime.strptime('2010-11-29', '%Y-%m-%d'),
        streams=1300000000,
        sales=4500000,
        region='Global'
    ),
    MusicData(
        title='Bad Habits',
        artist='Ed Sheeran',
        genre='Pop',
        release_date=datetime.strptime('2021-06-25', '%Y-%m-%d'),
        streams=1000000000,
        sales=3500000,
        region='Global'
    ),
    MusicData(
        title='Dynamite',
        artist='BTS',
        genre='K-Pop',
        release_date=datetime.strptime('2020-08-21', '%Y-%m-%d'),
        streams=1200000000,
        sales=4000000,
        region='Asia'
    ),
    MusicData(
        title='Someone Like You',
        artist='Adele',
        genre='Pop',
        release_date=datetime.strptime('2011-01-24', '%Y-%m-%d'),
        streams=1500000000,
        sales=5000000,
        region='Europe'
    ),
    MusicData(
        title='Watermelon Sugar',
        artist='Harry Styles',
        genre='Pop',
        release_date=datetime.strptime('2019-11-16', '%Y-%m-%d'),
        streams=1400000000,
        sales=3600000,
        region='North America'
    ),
    MusicData(
        title='In the End',
        artist='Linkin Park',
        genre='Rock',
        release_date=datetime.strptime('2000-10-24', '%Y-%m-%d'),
        streams=1000000000,
        sales=4200000,
        region='Global'
    ),
    MusicData(
        title='Faded',
        artist='Alan Walker',
        genre='Electronic',
        release_date=datetime.strptime('2015-12-04', '%Y-%m-%d'),
        streams=1100000000,
        sales=3000000,
        region='Global'
    ),
    MusicData(
        title='Montero (Call Me By Your Name)',
        artist='Lil Nas X',
        genre='Hip-Hop',
        release_date=datetime.strptime('2021-03-26', '%Y-%m-%d'),
        streams=900000000,
        sales=2400000,
        region='North America'
    ),
    MusicData(
        title='Happier Than Ever',
        artist='Billie Eilish',
        genre='Alternative',
        release_date=datetime.strptime('2021-07-30', '%Y-%m-%d'),
        streams=800000000,
        sales=1900000,
        region='Europe'
    ),
    MusicData(
        title='Stay',
        artist='The Kid LAROI & Justin Bieber',
        genre='Pop',
        release_date=datetime.strptime('2021-07-09', '%Y-%m-%d'),
        streams=2200000000,
        sales=4800000,
        region='Global'
    ),
    MusicData(
        title='Savage Love',
        artist='Jawsh 685 x Jason Derulo',
        genre='Pop',
        release_date=datetime.strptime('2020-06-11', '%Y-%m-%d'),
        streams=1700000000,
        sales=3200000,
        region='Global'
    ),
    MusicData(
        title='Drivers License',
        artist='Olivia Rodrigo',
        genre='Pop',
        release_date=datetime.strptime('2021-01-08', '%Y-%m-%d'),
        streams=1800000000,
        sales=3000000,
        region='North America'
    ),
    MusicData(
        title='Rockstar',
        artist='Post Malone feat. 21 Savage',
        genre='Hip-Hop',
        release_date=datetime.strptime('2017-09-15', '%Y-%m-%d'),
        streams=1500000000,
        sales=4500000,
        region='Global'
    ),
  ]

  db.session.bulk_save_objects(music_data_entries)
  db.session.commit()


def undo_music_data():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.music_data RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM music_data"))

    db.session.commit()
