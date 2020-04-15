import re
def word_count(stri):
    #remove with regular expression
    # stri = re.sub(r'[^\w\s]','',stri)
    #or we can wihout using additional lib
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    removed = ""
    for char in stri:
        if char not in punctuations:
            removed = removed + char

    counts = dict()
    words = removed.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


if __name__ == "__main__":
    temp1 = 'even even even this is is sentence..'
    print(word_count(temp1))
    temp2 = 'What is this book about? This book is about python coding'
    print(word_count(temp2))

#FIXED