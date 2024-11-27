from app.models import db, Report, environment, SCHEMA
from sqlalchemy.sql import text



def seed_reports():
  reports = [
    Report(
      title='Global Pop Trends',
      description='Analyzes total streams and sales for Pop genre globally.',
      query='{"genre": "Pop", "region": "Global"}',
      generated_data='{"totalStreams": 5000000000, "totalSales": 9000000}',
    ),
    Report(
      title='Regional Performance - North America',
      description='Breakdown of streams and sales for all genres in North America.',
      query='{"region": "North America"}',
      generated_data='{"totalStreams": 2000000000, "totalSales": 4000000}',
    ),
    Report(
      title='Rock Music Trends in Europe',
      description='Insights into the Rock genre performance in Europe.',
      query='{"genre": "Rock", "region": "Europe"}',
      generated_data='{"totalStreams": 1800000000, "totalSales": 5000000}',
    ),
    Report(
      title='Hip-Hop Domination in North America',
      description='Analysis of the Hip-Hop genre in North America.',
      query='{"genre": "Hip-Hop", "region": "North America"}',
      generated_data='{"totalStreams": 1500000000, "totalSales": 3000000}',
    ),
    Report(
      title='Electronic Music Popularity in Asia',
      description='Evaluates the Electronic genre streams and sales in Asia.',
      query='{"genre": "Electronic", "region": "Asia"}',
      generated_data='{"totalStreams": 800000000, "totalSales": 2000000}',
    ),
    Report(
      title='Pop Music Trends in Europe',
      description='Total streams and sales data for the Pop genre in Europe.',
      query='{"genre": "Pop", "region": "Europe"}',
      generated_data='{"totalStreams": 1400000000, "totalSales": 6000000}',
    ),
    Report(
      title='K-Pop Market in Asia',
      description='Focuses on the K-Pop genre performance in Asia.',
      query='{"genre": "K-Pop", "region": "Asia"}',
      generated_data='{"totalStreams": 2500000000, "totalSales": 7000000}',
    ),
    Report(
      title='Top Genres in Global Market',
      description='Global overview of top genres and their performance.',
      query='{"region": "Global"}',
      generated_data='{"Pop": 7000000000, "Rock": 3000000000, "Hip-Hop": 4000000000}',
    ),
    Report(
      title='Billboard Rock Performance - North America',
      description='Detailed breakdown of Rock genre streams and sales in North America.',
      query='{"genre": "Rock", "region": "North America"}',
      generated_data='{"totalStreams": 1200000000, "totalSales": 4000000}',
    ),
    Report(
      title='Rising Pop Artists in Global Markets',
      description='Identifies new Pop artists dominating global markets.',
      query='{"genre": "Pop", "region": "Global", "newArtists": true}',
      generated_data='{"totalStreams": 3000000000, "totalSales": 8000000}',
    ),
    Report(
      title='Legacy Artists in Rock Genre',
      description='Performance analysis of legacy Rock artists globally.',
      query='{"genre": "Rock", "legacyArtists": true, "region": "Global"}',
      generated_data='{"totalStreams": 500000000, "totalSales": 1000000}',
    ),
    Report(
      title='Streaming vs Sales for Hip-Hop',
      description='Comparison of streams and sales for Hip-Hop globally.',
      query='{"genre": "Hip-Hop", "region": "Global"}',
      generated_data='{"streamsToSalesRatio": 5.5}',
    ),
    Report(
      title='European Market Growth in Pop Genre',
      description='Growth metrics for the Pop genre in European markets.',
      query='{"genre": "Pop", "region": "Europe", "growth": true}',
      generated_data='{"growthRate": "8%"}',
    ),
    Report(
      title='Global Music Streams by Region',
      description='Analyzes total music streams broken down by region.',
      query='{"region": "Global"}',
      generated_data='{"North America": 3000000000, "Europe": 2500000000, "Asia": 2000000000}',
    ),
    Report(
      title='Top 10 Albums in North America',
      description='Lists the top 10 albums by streams and sales in North America.',
      query='{"region": "North America", "top": 10, "type": "albums"}',
      generated_data='{"totalStreams": 1000000000, "totalSales": 2000000}',
    ),
    Report(
      title='Viral Trends in Hip-Hop',
      description='Highlights viral trends and their impact on Hip-Hop streams.',
      query='{"genre": "Hip-Hop", "viral": true}',
      generated_data='{"totalStreams": 1500000000, "impact": "high"}',
    ),
    Report(
      title='Pop Genre Sales in Asia',
      description='Insights into sales trends for the Pop genre in Asia.',
      query='{"genre": "Pop", "region": "Asia"}',
      generated_data='{"totalSales": 4000000}',
    ),
    Report(
      title='Alternative Genre Streams in Europe',
      description='Analysis of streams for the Alternative genre in Europe.',
      query='{"genre": "Alternative", "region": "Europe"}',
      generated_data='{"totalStreams": 700000000}',
    ),
    Report(
      title='Youth-Oriented Genres in North America',
      description='Examines genres popular among youth in North America.',
      query='{"region": "North America", "ageGroup": "youth"}',
      generated_data='{"Pop": 500000000, "Hip-Hop": 700000000}',
    ),
    Report(
      title='Revenue from Streaming Platforms',
      description='Revenue data by genre from streaming platforms globally.',
      query='{"region": "Global", "metric": "revenue"}',
      generated_data='{"Pop": 7000000, "Hip-Hop": 4000000, "Rock": 2000000}',
    ),
  ]

  db.session.bulk_save_objects(reports)
  db.session.commit()

def undo_reports():
    if environment == "production":
      db.session.execute(f"TRUNCATE table {SCHEMA}.reports RESTART IDENTITY CASCADE;")
    else:
      db.session.execute(text("DELETE FROM reports"))
        
    db.session.commit()
