from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import SigmoidLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml.networkreader import NetworkReader
import csv

def get_words():
    result = []
    with open('wordlist.csv', 'r') as wordlist:
       wordreader = csv.reader(wordlist)
       for word in wordreader:
           result += word
    return result

def count_vector(tweet, words):
    return [ int(word in tweet) for word in words ]

if __name__ == '__main__':
    net = NetworkReader.readFrom('tweet_network.xml')
    words = get_words()
    while True:
        text = raw_input('Enter tweet--> ')
        if text.lower() == 'done':
            break
        meanness = str(int(net.activate(count_vector(text, words))[0]*5))
        print('Meaness: ' + meanness)

