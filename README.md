# Speed Announcer

Posts your current internet speed, using speedtest.net, to Twitter.

# Usage
 - Create a credentials.txt file. It should contain 4 lines.
   - Line 1 is your API key
   - Line 2 is your API secret
   - Line 3 is your OAUTH token
   - Line 4 is your OAUTH token secret
   All are provided by Twitter. Simply go [here](https://apps.twitter.com/app/new) and make a new app, then generate your keys.
  
# To Do:
	- Error handling
	- Mention current ISP in Tweet stating the current download/upload speeds are not up to par with whatever the current internet plan being paid for details
		- (i.e. If you're paying $70 a month for 50 MBps down, but only got 10 MBps down in the speedtest, complain to customer service through the Tweet)
	- Increase posting duration. Currently only posting once every hour
	- Make the program a little more object-oriented
	
Example output can be found on my [test Twitter account feed](https://twitter.com/simonwolde) (@simonwolde)