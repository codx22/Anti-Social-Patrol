# ANTI-SOCIAL TWITTER API SCRIPT
from TwitterSearch import *
import csv
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['fun time ']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information


# it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'fBGSPdujguMXIOgqET8COdLil',
        consumer_secret = 'XWyHu5z4DsA10gKTN6iKNFp8geYG1iHU3uaCQHJui8yvEk8t3B',
        access_token = '835589233549037569-8NDPEwxfvDCYNGR4bIcAft9GEcFBwYT',
        access_token_secret = 'FwF6DBcc24kGOwFCTAmXEy74SsMPVv9cuPKdh0MHIKX7i'
     )

    f = csv.writer(open("TweetsTest.csv", "a"))

# this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        if "RT" not in (tweet['text']):
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            print (tweet['text'])
            f.writerow([tweet['text'].encode('utf-8')])



except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)