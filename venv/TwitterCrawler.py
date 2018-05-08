import config
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)

api = tweepy.API(auth)


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('TwitterCrawl.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


myStream = Stream(auth, MyListener())
myStream.filter(track=['python'])





