import tweepy
import config


class TwitterData:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
        self.api = tweepy.API(self.auth)

    # Requests current US trends and returns trend objects
    def get_trend_object(self, WOEID=23424977):
        return self.api.get_place_trends(WOEID)[0]['trends']

    def get_trend_names(self, WOEID=23424977):
        return [i['name'] for i in self.api.get_place_trends(WOEID)[0]['trends']]

    # Requests tweets with key word query and returns a list of text from tweets
    def get_tweets(self, query):

        tweets = tweepy.Cursor(self.api.search_tweets,
                               q=query,
                               result_type='popular',
                               count=100,
                               lang='en',
                               tweet_mode='extended').items()

        return [i.full_text for i in tweets]