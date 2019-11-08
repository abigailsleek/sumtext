from flask import Flask, jsonify, request, render_template
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

# nltk.download('stopwords')

app = Flask(__name__)


def create_frequency_table(text_string) -> dict:
    # removing stop words
    stop_words = set(stopwords.words("english"))

    words = word_tokenize(text_string)

    # reducing words to their root form
    ps = PorterStemmer()

    # creating dictionary for the word frequency table
    frequency_table = dict()
    for word in words:
        word = ps.stem(word)
        if word in stop_words:
            continue
        if word in frequency_table:
            frequency_table[word] += 1
        else:
            frequency_table[word] = 1

    return frequency_table


def score_sentences(sentences, freqTable) -> dict:
    """
    score a sentence by its words
    Basic algorithm: adding the frequency of every non-stop word in a sentence divided by total no of words in a sentence.
    :rtype: dict
    """

    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        word_count_in_sentence_except_stop_words = 0
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                word_count_in_sentence_except_stop_words += 1
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        if sentence[:10] in sentenceValue:
            sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] / word_count_in_sentence_except_stop_words

        '''
        Notice that a potential issue with our score algorithm is that long sentences will have an advantage over short sentences. 
        To solve this, we're dividing every sentence score by the number of words in the sentence.

        Note that here sentence[:10] is the first 10 character of any sentence, this is to save memory while saving keys of
        the dictionary.
        '''

    return sentenceValue


def find_average_score(sentenceValue) -> int:
    """
    Find the average score from the sentence value dictionary
    :rtype: int
    """
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original text
    average = (sumValues / len(sentenceValue))

    return average


def generate_summary(sentences, sentence_value, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:10] in sentence_value and sentence_value[sentence[:10]] >= threshold:
            summary += " " + sentence
            sentence_count += 1

    return summary


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/summary', methods=['POST'])
def summary() -> str:
    # data = request_json(force=True)
    # request.get_json(force=True)
    # print(story)
    story = request.form.get('story')
    freq_table = create_frequency_table(story)

    # Tokenize the sentences
    sentences = sent_tokenize(story)

    # Important Algorithm: score the sentences
    sentence_scores = score_sentences(sentences, freq_table)

    # Find the threshold
    threshold = find_average_score(sentence_scores)
    print(sentence_scores)
    # Important Algorithm: Generate the summary
    output = generate_summary(sentences, sentence_scores, 0.8 * threshold)
    return render_template('index.html', summarized_text='The summarized text is: {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
