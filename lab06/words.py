import os
import re
import string

def read_words(filename):
    list = [line.split() for line in filename]
    words = []
    for line in list:
        for word in line:
                word = word.lower()
                word = word.strip(string.punctuation + string.whitespace)
                words.append(word)
    return words

def count_only(words, count_words):
    
    counts = [0]*len(count_words)
    my_zip = zip(count_words,counts)
    counts = dict(my_zip)

    for word in words:
        if word in count_words:
            counts[word] = counts[word] + 1
    return counts

def count_all_except(words, stopwords):
    counts = [0]*len(words)
    my_zip = zip(words, counts)
    counts = dict(my_zip)

    for word in words:
        if word not in stopwords:
            counts[word] = counts[word] + 1
    return counts

def filter_hist(hist, min_count):
    hist = [x for x in hist if x[1] > min_count]
    return hist

def sorted_hist(hist):
    list = [(k, v) for k, v in hist.items()]
    list.sort(key=lambda a: a[1])
    return list

# -----------------------------------------------------------

# uppg 1, 2

filename = 'nilsholg.txt'

# se till att vi öppnar filen i rätt katalog (slå samman 
# katalogen som scriptet ligger i med filnamnet på textfilen)
filepath = os.path.join(os.path.dirname(__file__), filename)

# öppna filen (utf-8 behövs för att hantera åäö rätt)
file = open(filepath, encoding='utf-8')

# skriv ut filens innehåll
#for line in file:
    #print(line)
    
#print(read_words(file))

# -----------------------------------------------------------

# uppg 3

filename = 'nilsholg.txt'
filepath = os.path.join(os.path.dirname(__file__), filename)
file = open(filepath, encoding='utf-8')
words = read_words(file)

filename = 'landskap.txt'
filepath = os.path.join(os.path.dirname(__file__), filename)
file = open(filepath, encoding='utf-8')
provinces = read_words(file)

hist = count_only(words, provinces)
print(hist['skåne'])

# -----------------------------------------------------------

# uppg 4

filename = 'undantagsord.txt'
filepath = os.path.join(os.path.dirname(__file__), filename)
file = open(filepath, encoding='utf-8')
stopwords = read_words(file)

hist = count_all_except(words, stopwords)
print(hist['han'])

# -----------------------------------------------------------

# uppg 5

hist = sorted_hist(hist)
index = len(hist)-1
while index >= len(hist)-10:
    print(hist[index])
    index = index - 1

# -----------------------------------------------------------

# uppg 6

hist = filter_hist(hist, 100)
print(hist)