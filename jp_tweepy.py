from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pymongo
from pymongo import MongoClient

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""


class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print data
		#set up mongodb connection
        client   = MongoClient()
        database_name = "AnnabelleTweets"
        database = client[database_name]
        collection_name = "tweets"
        collection = database[collection_name]
        collection.insert(data)
        return True

    def on_error(self, status):
        print status
        #return True #To continue listening
		
#	def on_timeout(self):
#		print "Timeout...."
#		print "\n"
#		return True #To Continue 

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#Annabelle'])