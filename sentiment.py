from textblob import TextBlob
from twitter import TwitterData


class SentimentAnalysis:
    def __init__(self):
        self.twitter_data = TwitterData()

    # Finds trend with matching name and requests related tweet text, which is analyzed for polarity
    def analyze_sentiment(self, trend_name):
        for i in self.twitter_data.get_trend_object():
            if i['name'].lower() == trend_name.lower():
                query = i['query']

        tweet_list = self.twitter_data.get_tweets(query)

        score = []
        for tweet in tweet_list:
            score.append(TextBlob(tweet).sentiment.polarity)

        return (sum(score) / len(score)) if sum(score) else sum(score)