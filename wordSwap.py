import random


def main():
    # Take input sentence from user
    sentence = input("Enter a sentence: ")

    # Split the sentence into a list of words
    words = sentence.split()

    # Create an empty dictionary to hold the words and their replacements
    word_dict = {}

    # Loop over the words in the sentence
    for word in words:
        # If the word is not already in the dictionary, add it
        if word not in word_dict:
            # Choose a random replacement word from the sentence
            replacement = random.choice(words)
            # Add the word and its replacement to the dictionary
            word_dict[word] = replacement

    # Print the word dictionary
    print(word_dict)

    # Loop over the words in the sentence again and replace each one with its replacement
    new_words = []
    for word in words:
        new_word = word_dict.get(word, word)
        new_words.append(new_word)

    # Print the new sentence with the replaced words
    new_sentence = ' '.join(new_words)
    print()
    print(new_sentence)


if __name__ == "__main__":
    main()

