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




# Display results
print(f"\nTotal number of words: {word_count}")
print(f"Total number of letters: {letter_count}")
print("\nWord frequencies:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")
if repeated_words:
    print("\nRepeated words and their counts:")
    for word, count in repeated_words.items():
        print(f"{word}: {count}")
else:
    print("\nNo repeated words found.")