from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import SigmoidLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml.networkreader import NetworkReader
import csv
import serial

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
    ser = serial.Serial('/dev/ttyACM0')
    samples = []
    index = 0
    with open('samples.csv', 'r') as samplefile:
        samplereader = csv.reader(samplefile)
        for sample in samplereader:
            samples += sample
    samplecount = len(samples)
    max_index = samplecount - 1
    while True:
        text = raw_input('Next Tweet? ')
        if text.lower() == 'done':
            break
        if index == max_index:
            index = 0
        else:
            index += 1
        print(samples[index])
        meanness = str(int(net.activate(count_vector(samples[index], words))[0]*5))
        if meanness == '0':
            meanness = '1'
        print(meanness)
        ser.write(meanness)
    ser.close()

