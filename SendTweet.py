import time, subprocess, re
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


# Conduct a speed test 
speedtest_result = subprocess.getoutput('speedtest-cli')

# Parse the result
pattern = re.compile("\d+[.]\d+")
num_values = pattern.findall(speedtest_result)
server = speedtest_result.split("(")[2].split(")")[0]
isp = "XFINITY by Comcast"
tweet = """
Speedtest.net Results for ISP {}:
Test server: Hosted by ScaleMatrix - ({})[{} km]
Ping: {} ms
Download Speed: {} Mbit/s
Upload Speed: {} Mbit/s
""".format(isp, server, num_values[2], num_values[3], num_values[4], num_values[5])


# Send a Tweet
twitter.update_status(status=tweet)
#time.sleep(900)#Tweet every 15 minutes