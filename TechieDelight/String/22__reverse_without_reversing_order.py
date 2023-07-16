def reverseSentence(s):
    # ch = ''
    l = 0

    word = ''

    for i in reversed(range(len(s))):
        if s[i] != " ":
            word = s[i] + word

        else:
            print(word, end=" ")
            word = ""

    print(word)

if __name__ == "__main__":
    s = 'Preparation Interview Technical'
    reverseSentence(s)
        

