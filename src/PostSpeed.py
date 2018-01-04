import time, subprocess, re, sys, os
from datetime import datetime
from twython import Twython

def progress(count, total):
	bar_len = total // 3600 # 1 bar filled = 1 hour
	filled_len = int(round(bar_len * count / float(total)))
	percents = round(100.0 * count / float(total), 1)
	bar = '=' * filled_len + '-' * (bar_len - filled_len)
	time_passed = "%f" % (count / total) 
	time_passed = float(time_passed) * total
	sys.stdout.write('\r[%s] %s%s | %s seconds have passed\r' % (bar, percents, '%', round(time_passed, 10)))
	sys.stdout.flush()

def main():
	time_delay = 30 # Tweet every 8 hours (28800 seconds)
	last_tweet = "Never"
	instance = 0
	
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
		twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
		if instance > 0:
			print("Last tweet was sent: {}".format(last_tweet))
		
		# Conduct a speed test 
		print("Conducting speed test...")
		speedtest_result = subprocess.getoutput('speedtest-cli')
		print("Parsing speed test...")
		
		# Parse the result
		pattern = re.compile("\d+[.]\d+")
		num_values = pattern.findall(speedtest_result)
		server = speedtest_result.split("(")[2].split(")")[0]
		isp = "XFINITY by Comcast"
		current_time = datetime.now()
		tweet = """
		Speedtest.net Results for ISP {}:
		Test server: Hosted by ScaleMatrix - ({})[{} km]
		Ping: {} ms
		Download Speed: {} Mbit/s
		Upload Speed: {} Mbit/s
		Time: {}
		""".format(isp, server, num_values[2], num_values[3], num_values[4], num_values[5], current_time)
		
		# Send a Tweet
		twitter.update_status(status=tweet)
		last_tweet = current_time
		instance +=1
		print("Tweet Sent!")
		print("Waiting {} seconds until next speed test.".format(time_delay))
		
		i = 0
		while i < time_delay:
			progress(i, time_delay)
			time.sleep(1)
			i +=1
if __name__ == "__main__":
	main()