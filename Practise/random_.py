
text = "Python is easy and Python is powerful"

dictionary = {}

for word in text.lower().split():
    if len(word) > 4:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1 

print(dictionary)



print("\n==================================================================\n")



def count_words(text):
    dictionary = {}

    for word in text.lower().split():
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary



print("\n==================================================================\n")


def get_long_words(text):
    new_result = {}
    result = count_words(text)

    for i in result:
        if len(i) > 4:
           new_result.update({i: result[i]})

    return new_result

get_long_words(text)
















