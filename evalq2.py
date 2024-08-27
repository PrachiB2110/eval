from collections import Counter
import re

def most_repeated(string):
    cleaned_string = re.sub(r'[^\w\s]', '', string).lower()

    words = cleaned_string.split()
    letters = [char for char in cleaned_string if char.isalpha()]

    word_count = Counter(words)
    letter_count = Counter(letters)

    most_common_word, most_common_word_count = word_count.most_common(1)[0]
    if word_count ;
    else (None, 0);
    most_common_letter, most_common_letter_count = letter_count.most_common(1)[0]
    if letter_count;
    else (None, 0);

    return most_common_word, most_common_word_count, most_common_letter, most_common_letter_count

input_string = "Hello world! Hello everyone. Welcome to the world of programming."

most_common_word, word_count, most_common_letter, letter_count = most_repeated(input_string)

print(f"Most repeated word: '{most_common_word}' with {word_count} occurrences")
print(f"Most repeated letter: '{most_common_letter}' with {letter_count} occurrences")
