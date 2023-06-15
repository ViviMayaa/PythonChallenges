phrase = "if the implementation is easy to explain , it may be a good idea"

# 1- printar a quantidade de vezes que a letra 'a' aparece na frase
# number of times the letter 'a' appears
count = 0
for value in phrase:
    if value == "a":
        count += 1
print(f"Number of A's {count}")

# 2 - printar a quantidade de palavras da frase
# counting the number of words
count = 0
phrase_format = phrase.replace(',', '').replace("  ", ' ')
list_phrase = phrase_format.split(' ')
count = len(list_phrase)

print(f"Number of Words {count}")


# 3 - printar a quantidade de vezes que cada letra aparece na frase
# counting how many times each word appears in the sentence, as the following example of output:
# {'i': 7, 'e': 7, 'a': 6, 't': 5, 'o': 4, 'm': 3, 'n': 3, 'p': 2, 'l': 2, 's': 2, 'y': 2, 'd': 2, 'f': 1, 'h': 1, 'x': 1, 'b': 1, 'g': 1}
count = 0
dict_words = {}
phrase_format = phrase.replace(',', '').replace(" ", '')
# quais letras estao na frase
list_of_words = list(set(phrase_format.lower()))
for i in range(0, len(list_of_words)):
    dict_words.update({list_of_words[i]: 0})
for value in phrase_format:
    dict_words[value] += 1

# saber quantas vezes aparecem
# dict_words = {}
# for value in phrase_format:
#     dict_words[value] += 1
#     dict_words[value] = 0

print(f"Number of letters {dict_words}")