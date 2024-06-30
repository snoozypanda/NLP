import json

with open('stop_word.txt', 'r', encoding='utf-8') as file:
    stop_word = file.read()

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
        "ን": "ን",
        "ሙ": "ም",
        "ውም": "ም",
        "ዣ": "ዥም",
        "ዎች": "ች",
        "ሱ": "ስ",
        "ታው": "ታ",
        "ናው": "ው",
        "ችው": "ች",
        "ቷ": "ት",
        "ቱ": "ት",
        "ናዊ": "መ",
        "ያልጠ": "ን",
        "ቦቹ": "ባ",
        "ሚው": "ሚ",
        "ያው": "ያ",
        "ታቸው": "ት",
        "ሻቸው": "ሽ",
        "ልህ": "ህ",
        "ሞች": "ም",
        "ታቸው": "ት",
        "ረኛ": "ር",
        "ሮች": "ር",
        "ትው": "ት",
        "ማው": "ማ",
        "ፋው": "ፋ",
        "ትን": "ት",
        "ታን": "ታ",
        "ንም": "ን"
    }

    for old, new in replacements.items():
        if token.endswith(old):
            token = token[:-len(old)] + new
            break

    return token

def create_inverted_index(documents):
    inverted_index = {}
    
    for doc_id, doc_text in enumerate(documents, start=1):
        tokens = doc_text.split()
        filtered_tokens = [token for token in tokens if token not in stop_word]
        stemmed_tokens = [stemming(token) for token in filtered_tokens]

        for token in stemmed_tokens:
            if token in inverted_index:
                if inverted_index[token][-1]['doc_id'] == doc_id:
                    inverted_index[token][-1]['frequency'] += 1
                else:
                    inverted_index[token].append({"doc_id": doc_id, "frequency": 1})
            else:
                inverted_index[token] = [{"doc_id": doc_id, "frequency": 1}]

    return inverted_index

with open('doc1.txt', 'r', encoding='utf-8') as file:
    doc1 = file.read()
with open('doc2.txt', 'r', encoding='utf-8') as file:
    doc2 = file.read()
with open('doc3.txt', 'r', encoding='utf-8') as file:
    doc3 = file.read()

documents = [doc1, doc2, doc3]

inverted_index = create_inverted_index(documents)

print("Inverted Index:")
for word, postings in inverted_index.items():
    print(f"{word}: {postings}")

with open("inverted_index.json", "w", encoding="utf-8") as f:
    json.dump(inverted_index, f, ensure_ascii=False)
