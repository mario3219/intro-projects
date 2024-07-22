import os

def read_words(filename):
    list = [line.split(" ") for line in filename]
    words = []
    for line in list:
        for string in line:
            string = string.strip("\n") and string.strip()
            words.append(string)
    return words

def count_only(words, count_words):
    counts = dict(count_words)
    print(counts)
    for word in words:
        if word in count_words:
            counts[word] += 1
    return counts

def count_all_except(words, stopwords):
    pass

def filter_hist(hist, min_count):
    # ännu ej implementerad
    pass

def sorted_hist(hist):
    # ännu ej implementerad
    pass

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
