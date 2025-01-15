from collections import Counter
import string

paragraph = input('Enter a paragraph : ');

paragraph_cleaned = paragraph.lower().translate(str.maketrans('','',string.punctuation));

words = paragraph_cleaned.split();

word_count = len(words);
print(word_count);

# letter_count = 0;
# for word in words :
#     letter_count += len(word);
# print(letter_count)

letter_count = sum(len(word) for word in words);

word_frequency = Counter(words);




# for word,count in word_frequency.items():
#     if count > 1:
#         repeated_words = {word:count};
#         print(repeated_words);

repeated_words = { word:count for word,count in word_frequency.items() if count > 1 }
print(repeated_words);