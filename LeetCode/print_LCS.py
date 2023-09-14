def printLCS(word, subWords, sub_word , i=0):
    if i == len(word):
        print(sub_word)
        subWords.append(sub_word)
        return

    printLCS(word, subWords , sub_word + word[i], i + 1)
    printLCS(word, subWords, sub_word, i + 1)
    return subWords


if __name__ == '__main__':
    word = 'abcde'
    subWords = []
    words = printLCS(word, subWords, "")

    print(words)





    