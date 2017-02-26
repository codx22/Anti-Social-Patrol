import csv

if __name__ == '__main__':
    with open('wordcount.csv', 'r') as wordcount:
        reader = csv.reader(wordcount)
        with open('wordlist.csv', 'w') as wordlist:
            writer = csv.writer(wordlist)
            for word_row in reader:
                writer.writerow([word_row[0]])
