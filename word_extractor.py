import csv

if __name__ == '__main__':
    wordlist = []
    with open('tweets.csv', 'r') as tweet_file:
        tweet_reader = csv.reader(tweet_file)
        for tweet in tweet_reader:
            if int(tweet[1]) == 1:
                wordlist += tweet[0].split(' ')
    wordset = set(wordlist)
    wordcount = []
    for word in wordset:
        wordcount.append((word, wordlist.count(word)))
    wordcount.sort(key=(lambda x: x[1]))
    wordcount = wordcount[100:]
    with open('wordcount.csv', 'w') as countfile:
        tweet_writer = csv.writer(countfile)
        wordcount.reverse()
        for word in wordcount:
            tweet_writer.writerow([word[0], str(wordlist.count(word[0]))])
 
