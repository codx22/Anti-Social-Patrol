from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import SigmoidLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.datasets import SupervisedDataSet
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
    words = get_words()
    net = buildNetwork(len(words), 10, 1, outclass=SigmoidLayer)
    ds = SupervisedDataSet(len(words), 1)
    with open('tweets.csv', 'r') as tweet_file:
        tweet_reader = csv.reader(tweet_file)
        for tweet in tweet_reader:
            input_vector = count_vector(tweet[0], words)
            print(tweet)
            desired_output = int(tweet[1])
            ds.addSample(tuple(input_vector), (desired_output,))
    
    trainer = BackpropTrainer(net, ds)
    for i in range(200):
        print(trainer.train())
    print(net.activate(count_vector("FUCK YOU BITCH", words)))
    print(net.activate(count_vector("Having fun at Desert Hacks", words)))
    NetworkWriter.writeToFile(net, 'tweet_network.xml')

