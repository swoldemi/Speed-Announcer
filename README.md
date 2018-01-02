[![](https://img.shields.io/badge/python-3.6.3-blue.svg)](https://www.python.org/downloads/release/python-363/)

# Speed Announcer

Posts your current internet speed, using speedtest.net, to Twitter.

# Usage
1. Create a credentials.txt file. It should contain 4 lines.
   - Line 1 is your API key
   - Line 2 is your API secret
   - Line 3 is your OAUTH token
   - Line 4 is your OAUTH token secret
   All are provided by Twitter. Simply go [here](https://apps.twitter.com/app/new) and add a new app, then generate your keys.

2. Install the requirements with:
```
pip install -r requirements.txt
```

Note: `cx_Freeze` is only needed if you want to make your own Windows executable and requires the usual Visual Studio runtime libraries. You can build your own binary, after editing `src/PostSpeec.py` to your liking, by running `python setup.py build`.

3. Run Announce.bat.

4. Check your Twitter feed.
  
# To Do
- Error handling
- *Mention current ISP in Tweet stating the current download/upload speeds are not up to par with whatever the current internet plan being paid for details*
	- (i.e. If you're paying $70 a month for 50 MBps down, but only got 10 MBps down in the speedtest, complain to customer service through the Tweet)
	- There's speculation that ISPs are in cahoots with "speed testing services", slashing your current bandwidth-delay product by a factor when a speedtest.net request is made. 
- Increase posting duration. Currently only posting once every hour.
- Make the program a little more object-oriented.
- Add support for other social media outlets.
	
Example output can be found on my [test Twitter account feed](https://twitter.com/simonwolde) (@simonwolde)
