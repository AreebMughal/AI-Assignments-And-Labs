

def display_words():
    file = open('story.txt', 'r')
    data = file.read().split('. ')
    # data = file.readlines()
    print('The words which contain less than 4 characters: ')
    for line in data:
        for word in line.split():
            word = word.replace('.', '') if '.' in word else word
            if (len(word) < 4):
                print(word)
            
display_words()