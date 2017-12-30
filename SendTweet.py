import time, sys
from twython import Twython

# Load credentials
filename=open('credentials.txt','r')
f=filename.readlines()
filename.close()

# Authenticate with Twitter
APP_KEY = f[0].split('\n')[0]
APP_SECRET = f[1].split('\n')[0]
OAUTH_TOKEN = f[2].split('\n')[0]
OAUTH_TOKEN_SECRET = f[3].split('\n')[0]
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Send a Tweet
twitter.update_status(status="I just started using Twython!")
#time.sleep(900)#Tweet every 15 minutes