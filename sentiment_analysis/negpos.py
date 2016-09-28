import psycopg2
import numpy as np
import config
from nltk.sentiment.vader import SentimentIntensityAnalyzer

vader_analyzer = SentimentIntensityAnalyzer()
cnx = psycopg2.connect(**config.DB_INFO)
cursor = cnx.cursor()
query = '''SELECT id,contents FROM raw_tweets WHERE sentiment IS NULL; '''
cursor.execute(query)
tweets = cursor.fetchall()
for tweet in tweets:
  data = tuple([vader_analyzer.polarity_scores(tweet[1])['compound'],tweet[0]])
  add_log = ("UPDATE raw_tweets "
                  "SET sentiment = %s"
                  "WHERE id = %s")
  cursor.execute(add_log,data)
cnx.commit()
cursor.close()
cnx.close()
