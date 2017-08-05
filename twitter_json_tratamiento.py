from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json


consumer_key = 'consumer_key_here'
consumer_secret = 'consumer_secret_here'
access_token = 'access_token_here'
access_token_secret = 'access_token_secret_here'

class MyListener(StreamListener):	
	def on_data(self,data):
		try:
			
			jsonData = json.loads(data)             
			createdAt = jsonData['created_at']             
			text = jsonData['text']             
			saveThis = createdAt + " :: " + text 
			encode = saveThis.encode('utf-8')
			print encode#.decode('unicode-escape')
			#####             
			saveFile = open('twitterDB4.json','a')
			saveFile.write(encode)
			saveFile.write('\n')
			saveFile.close()
			return True
			
		except BaseException, e:
			print 'Falla de datos,',str(e)
			time.sleep(5)
			
	def on_error(self, status):
		print status
		return True


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, MyListener())
twitterStream.filter(track = ["#hashtag_here"]) 

