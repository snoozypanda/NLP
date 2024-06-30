import matplotlib.pyplot as plt # type: ignore
import nltk
from collections import Counter


def index_words(amharic_text):
 with open('stop_word.txt', 'r', encoding='utf-8') as file:
    stop_word = file.read()   
    words = nltk.word_tokenize(amharic_text)
    remove_words_for_index = [word for word in words if word not in stop_word]
    print("------------Stop words Used For Indexing------------")
    print(stop_word)
    return remove_words_for_index
   
with open('amharic.txt', 'r', encoding='utf-8') as file:
    amharic_text = file.read()
indexed_words = index_words(amharic_text)
print("----indexed_words----------")
print(indexed_words)

words = nltk.word_tokenize(amharic_text)
print(words)

with open('stop_word.txt', 'r', encoding='utf-8') as file:
    stop_word = file.read()   
filtered_tokens = [word for word in words if word not in stop_word]



word_counts = Counter(word for word in words if word not in stop_word)
print("--------Words By Frequency-------")

print(word_counts)

ranked_words = word_counts.most_common()

product_of_rank_and_frequency = []

for i, (word, count) in enumerate(ranked_words):
    rank = i + 1  
    frequency = count
    product = rank * frequency
    product_of_rank_and_frequency.append(product)
    print(f"{i+1}. {word}: {count} (Product: {product})")

ranks = [i+1 for i, (_, _) in enumerate(ranked_words)]  
frequencies = [count for _, count in ranked_words]

print("--------Product of Rank and Frequency-------")

print(product_of_rank_and_frequency)

     





plt.plot(ranks, frequencies)


plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.title("Frequency vs. Rank of Words in Amharic Text")
plt.grid(True)  

plt.show()



