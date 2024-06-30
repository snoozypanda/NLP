from collections import defaultdict
import math

with open('stop_word.txt', 'r', encoding='utf-8') as file:
    stop_word = set(file.read().split())

prefix_patterns = ["የ", "ወረ", "በ", "ና", "ስለ", "ከ", "ናው", "ለ", ""]
suffix_patterns = ["ና", "ዥም"]

def stemming(token):
    for suffix in suffix_patterns:
        if token.endswith(suffix):
            token = token[:-len(suffix)]
            break
    for prefix in prefix_patterns:
        if token.startswith(prefix):
            token = token[len(prefix):]
            break
    replacements = {
        "ን": "ን", "ሙ": "ም", "ውም": "ም", "ዣ": "ዥም", "ዎች": "ች", "ሱ": "ስ", "ታው": "ታ", "ናው": "ው", 
        "ችው": "ች", "ቷ": "ት", "ቱ": "ት", "ናዊ": "መ", "ያልጠ": "ን", "ቦቹ": "ባ", "ሚው": "ሚ", "ያው": "ያ", 
        "ታቸው": "ት", "ሻቸው": "ሽ", "ልህ": "ህ", "ሞች": "ም", "ታቸው": "ት", "ረኛ": "ር", "ሮች": "ር", "ትው": "ት", 
        "ማው": "ማ", "ፋው": "ፋ", "ትን": "ት", "ታን": "ታ", "ንም": "ን"
    }
    for old, new in replacements.items():
        if token.endswith(old):
            token = token[:-len(old)] + new
            break
    return token

def compute_document_vectors(documents):
    document_vectors = defaultdict(dict)
    for doc_id, doc_text in enumerate(documents):
        tokens = doc_text.split()
        filtered_tokens = [token for token in tokens if token not in stop_word]
        stemmed_tokens = [stemming(token) for token in filtered_tokens]
        term_freqs = {}
        for token in stemmed_tokens:
            term_freqs[token] = term_freqs.get(token, 0) + 1
        document_vectors[doc_id] = term_freqs
    return document_vectors

def compute_cosine_similarity(vector1, vector2):
    dot_product = sum(vector1[token] * vector2.get(token, 0) for token in vector1)
    magnitude1 = math.sqrt(sum(value ** 2 for value in vector1.values()))
    magnitude2 = math.sqrt(sum(value ** 2 for value in vector2.values()))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    return dot_product / (magnitude1 * magnitude2)

def vectorize_query(query):
    tokens = query.split()
    filtered_tokens = [token for token in tokens if token not in stop_word]
    stemmed_tokens = [stemming(token) for token in filtered_tokens]
    query_vector = defaultdict(int)
    query_freqs = defaultdict(int)
    for token in stemmed_tokens:
        query_vector[token] += 1
        query_freqs[token] += 1
    return query_vector, query_freqs

with open('doc1.txt', 'r', encoding='utf-8') as file:
    doc1 = file.read()
with open('doc2.txt', 'r', encoding='utf-8') as file:
    doc2 = file.read()
with open('doc3.txt', 'r', encoding='utf-8') as file:
    doc3 = file.read()

documents = [doc1, doc2, doc3]

document_vectors = compute_document_vectors(documents)

print("Term Frequency Weights for Each Document:")
for doc_id, term_freqs in document_vectors.items():
    print(f"Document {doc_id + 1}:")
    for term, freq in term_freqs.items():
        print(f" {term}: {freq}")

with open('query.txt', 'r', encoding='utf-8') as file:
    query = file.read()

query_vector, query_freqs = vectorize_query(query)

similarities = []
for doc_id, doc_vector in document_vectors.items():
    similarity = compute_cosine_similarity(query_vector, doc_vector)
    similarities.append((doc_id, similarity))

sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

print("\nFrequency of Each Query Word in Each Document:")
for term, freq in query_freqs.items():
    print(f"Query Term '{term}':")
    for doc_id, doc_vector in document_vectors.items():
        print(f"  Document {doc_id + 1}: {doc_vector.get(term, 0)}")

print("\nDocuments ranked by similarity to the query:")
for doc_id, similarity in sorted_similarities:
    print(f"Document {doc_id + 1}: {similarity}")
