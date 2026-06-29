import re

#What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'


words_list = re.findall('\\w+', paragraph.lower())
word_counts = {}

for words in words_list:
    if words in word_counts:
        word_counts[words] += 1
    else:
        word_counts[words] = 1
        
tuple_list = [(count, word) for word, count in word_counts.items()]
tuple_list.sort(key=lambda x: x[0], reverse=True)

print(tuple_list)

#The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

points = re.findall(r'-?\d+',txt)
sorted_points = [int(point) for point in points]

print(sorted_points)


difference = sorted_points[len (sorted_points) - 1] - sorted_points[0]
print (difference)

#Write a pattern which identifies if a string is a valid python variable

def is_valid_variable(name: str):

    if re.search(r'^[0-10]',name):
       print(False)
    elif re.findall(r'\W[^-]',name):
        print(False)
    else:
        print(True)


is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True    


#Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'
word_counts2 = {}

def text_cleaner(txt: str):
    cleaned = re.sub(r'[%&@$#]', '',txt)
    return cleaned.lower()

def most_frequent_words(words: str) -> dict:  
    word_counts = {}
    cleaned_txt = text_cleaner(words)
    cleaned_txt = re.sub(r'[^\w\s]', '', cleaned_txt)

    words_list = cleaned_txt.split()

    for word in words_list:
        if word in word_counts:
            word_counts[word] += 1
        else: 
            word_counts[word] = 1 

    return word_counts       


print(text_cleaner(sentence))

word_frequencies = most_frequent_words(sentence)
tuple_list = [(count, word) for word, count in word_frequencies.items()]
tuple_list.sort(key=lambda x: x[0], reverse= True)

print (tuple_list[:3])

