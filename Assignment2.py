with open('stop_word.txt', 'r', encoding='utf-8') as file:
    stop_word = file.read()   

with open('amharic.txt', 'r', encoding='utf-8') as file:
    amharic_text = file.read()

tokens = amharic_text.split()
filtered_tokens = [token for token in tokens if token not in stop_word]

prefix_patterns = ["የ", "ወረ", "በ", "ና", "ስለ", "ከ", "ናው", "ለ", ""]
suffix_patterns = ["ና", "ዥም"]

suffix_replacements = {
    "ቡ": "ብ", "ደ": "ድ", "ሙ": "ም", "ውም": "ም", "ዣ": "ዥም", "ዎች": "ች", "ሱ": "ስ", 
    "ታው": "ታ", "ናው": "ው", "ችው": "ች", "ቷ": "ት", "ቱ": "ት", "ናዊ": "መ", "ያልጠ": "ን", 
    "ቦቹ": "ባ", "ሚው": "ሚ", "ያው": "ያ", "ታቸው": "ት", "ሻቸው": "ሽ", "ልህ": "ህ", 
    "ሞች": "ም", "ረኛ": "ር", "ሮች": "ር", "ትው": "ት", "ማው": "ማ", "ፋው": "ፋ", 
    "ትን": "ት", "ታን": "ታ", "ንም": "ን", "ንን": "ን"
}

stemmed_tokens = []
for token in filtered_tokens:
    for suffix in suffix_patterns:
        if token.endswith(suffix):
            token = token[:-len(suffix)]
            break

    for prefix in prefix_patterns:
        if token.startswith(prefix):
            token = token[len(prefix):]
            break

    for old_suffix, new_suffix in suffix_replacements.items():
        if token.endswith(old_suffix):
            token = token[:-len(old_suffix)] + new_suffix
            break

    stemmed_tokens.append(token)

stemmed_text = " ".join(stemmed_tokens)
print(stemmed_text)
