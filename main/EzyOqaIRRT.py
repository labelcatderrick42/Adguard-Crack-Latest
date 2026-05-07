def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = text.split('. ')
    return len(sentences)

def average_word_length(text):
    words = text.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0

def average_sentence_length(text):
    sentences = text.split('. ')
    total_length = sum(len(sentence.split()) for sentence in sentences)
    return total_length / len(sentences) if sentences else 0

def get_word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def main():
    text = "This is a simple text. This text is for processing."
    print(f'Word Count: {count_words(text)}')
    print(f'Sentence Count: {count_sentences(text)}')
    print(f'Average Word Length: {average_word_length(text):.2f}')
    print(f'Average Sentence Length: {average_sentence_length(text):.2f}')
    print('Word Frequency:')
    for word, freq in get_word_frequency(text).items():
        print(f'{word}: {freq}')

if __name__ == '__main__':
    main()
