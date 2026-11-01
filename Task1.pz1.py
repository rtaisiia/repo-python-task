def text(input_string):
    dictionary = {}
    for word in input_string.split():
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary

my_text = "the cat is sitting on the window. the cat sees a bird. the cat is purring. the cat is sleeping in the sun."
result = text(my_text)
print("\nSlovnuk sliv:\n", result)

povtor_sliv = []
for word, count in result.items():
    if count > 3:
        povtor_sliv.append(word)
print("\nSlova, scho povtoryytsya bilshe 3 raziv:\n", povtor_sliv)

