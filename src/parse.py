import tinysegmenter as ts
import tika
tika.initVM()
from tika import parser


# Take a tokenized list as input and return a dict containing
# unique words in the list as the key and number of appearances as
# the value
def get_frequency(words):
    # Hold unique words and the number of times they appear in the
    # input list
    unique_word_count = {}

    # Iterate through input and count the number of appearances of
    # each unique word
    for word in words:
        # if this ends up being 5 then skip the word
        skip = 0
        # Hiragana
        if max(word) < u'\u3040' or max(word) > u'\u309f':
            skip += 1
        # Katakana
        if max(word) < u'\u30a0' or max(word) > u'\u30ff':
            skip += 1
        # Full-width roman chars, half-width katakana
        if max(word) < u'\uff00' or max(word) > u'\uffef':
            skip += 1
        # Common and uncommon kanji
        if max(word) < u'\u4e00' or max(word) > u'\u9faf':
            skip += 1

        # Skip word, it's not Japanese
        if skip == 4:
            continue

        # Check if word is already accounted for
        if word in unique_word_count:
            unique_word_count[word] += 1
        else:
            unique_word_count[word] = 1

    return sorted(unique_word_count.items(), key=lambda kv: kv[1], reverse=True)


# Load a pdf and create a frequency list from the text in the pdf
def freq_from_pdf(filepath):
    # Load pdf and get the text from it
    pdf_text = parser.from_file(filepath)

    return get_frequency(ts.tokenize(pdf_text["content"]))


# Load a list of blacklisted words from a file
def load_blacklist():
    # Load blacklist from file

    return


# Save list to file
def save_blacklist():
    # TODO: Save list to file

    return


# Add a word to the blacklist
def add_word_to_blacklist(word):
    # TODO: add word to blacklist
    return


test_str = "私の名前は中野です"

print(get_frequency(ts.tokenize(test_str)))

text = parser.from_file("/home/brkurzawa/PycharmProjects/jpankiwords/src/nihong_hanashikata.pdf")

print(get_frequency(ts.tokenize(text["content"])))

print(freq_from_pdf("/home/brkurzawa/PycharmProjects/jpankiwords/src/nihong_hanashikata.pdf"))

# TODO: Account for the fact that newlines split up words, which causes tinysegmenter to not work properly in some cases
