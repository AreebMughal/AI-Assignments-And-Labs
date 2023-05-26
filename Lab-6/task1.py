

file = open('story.txt', 'r')
data = file.read().split('. ') # if file is in one paragraph
# data = file.readlines()
count = 0
for line in data:
    if (line[0] != 'T'):
        count += 1
        
print(f'The number of lines not starting with "T" is: {count}')