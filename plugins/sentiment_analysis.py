import re
from textblob import TextBlob


class SentimentAnalysis:

    def __init__(self, text):
        self.text = text

    # only for english language
    def execute(self):
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.text)

        # set sentiment
        if analysis.sentiment.polarity > 0:
            data = {'text': self.text, 'sentiment': 'positive'}
        elif analysis.sentiment.polarity == 0:
            data = {'text': self.text, 'sentiment': 'neutral'}
        else:
            data = {'text': self.text, 'sentiment': 'negative'}

        return data


if __name__ == "__main__":
    # calling main function
    SentimentAnalysis('hard to learn NLTK').execute()
