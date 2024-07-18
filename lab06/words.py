import os

def read_words(filename):
    # ännu ej implementerad
    pass

def count_only(words, count_words):
    # ännu ej implementerad
    pass

def count_all_except(words, stopwords):
    # ännu ej implementerad
    pass

def filter_hist(hist, min_count):
    # ännu ej implementerad
    pass

def sorted_hist(hist):
    # ännu ej implementerad
    pass

# -----------------------------------------------------------

filename = 'nilsholg.txt'

# se till att vi öppnar filen i rätt katalog (slå samman 
# katalogen som scriptet ligger i med filnamnet på textfilen)
filepath = os.path.join(os.path.dirname(__file__), filename)

# öppna filen (utf-8 behövs för att hantera åäö rätt)
file = open(filepath, encoding='utf-8')

# skriv ut filens innehåll
for line in file:
    print(line)