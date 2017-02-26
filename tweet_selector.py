import csv
import random
if __name__ == '__main__':
    sampletweetlist = []
    tweetlist = []
    with open('TweetsTest(1).csv', 'r') as tweet_file:
        tweet_reader = csv.reader(tweet_file)
        for tweet in tweet_reader:
            print(tweet)
            tweetlist += tweet
    for count in range(500):
        sample = random.choice(tweetlist)
        sampletweetlist.append(sample)
        tweetlist.remove(sample)
    with open('tweets.csv', 'w') as tweet_file:
        tweet_writer = csv.writer(tweet_file)
        for tweet in sampletweetlist:
            tweet_writer.writerow([tweet])
