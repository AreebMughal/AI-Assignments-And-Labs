
def count_words_with_last_e():
    file = open('story.txt', 'r')
    count = 0
    data = file.read().split('. ')
    # data = file.readlines()
    for line in data:
        for word in line.split():
            word = word.replace('.', '') if '.' in word else word
            if (word[len(word) - 1] == 'e'):
                # print(word)
                count += 1   
    
    return count
            
print(f"Total number of words ending with 'e' is: {count_words_with_last_e()}")

 