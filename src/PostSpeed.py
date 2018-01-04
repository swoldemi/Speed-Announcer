import time, subprocess, re, sys, os
from datetime import datetime
from twython import Twython
from progress.bar import Bar


def main():
	time_delay = 600 # Tweet every 8 hours (28800 seconds)
	
	# Get file name
	credentials = sys.argv[1]
	
	# Load credentials
	filename = open(credentials, 'rt')
	f = filename.readlines()
	filename.close()

	# Authenticate with Twitter
	APP_KEY = f[0].split('\n')[0]
	APP_SECRET = f[1].split('\n')[0]
	OAUTH_TOKEN = f[2].split('\n')[0]
	OAUTH_TOKEN_SECRET = f[3].split('\n')[0]
	
	# Begin "event loop"
	while True:
	
		os.system("cls") # should add support for multiple operating systems
		bar = Bar('Seconds until next Tweet', max=time_delay)
		twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
		
		# Conduct a speed test 
		print("Conducting speed test...")
		speedtest_result = subprocess.getoutput('speedtest-cli')
		print("Parsing speed test...")
		
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
		Time: {}
		""".format(isp, server, num_values[2], num_values[3], num_values[4], num_values[5], datetime.now())

		# Send a Tweet
		twitter.update_status(status=tweet)
		print("Tweet Sent!")
		for x in range (0, time_delay):
			time.sleep(1)
			bar.next()
		bar.finish()
if __name__ == "__main__":
	main()