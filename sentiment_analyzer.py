
import pickle
import string

from tensorflow.keras.preprocessing.sequence import pad_sequences


maxLen = 150

stop_words = [ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", 
             "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during",
             "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", 
             "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into",
             "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or",
             "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", 
             "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
             "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up",
             "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's",
             "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've",
             "your", "yours", "yourself", "yourselves" ]

"""
Preprocessing function
"""
def cleaning(text, tokenizer):
    # remove stopwords
    text = ' '.join([i for i in text.lower().split() if i not in (stop_words)])
    # remove html tags
    text = text.replace('<.*?>', '')
    # remove punctuations
    text = text.replace('[{}]'.format(string.punctuation), ' ')
    # remove words with single letter
    text = ' '.join([i for i in text.split() if len(i)>1])
    
    text = tokenizer.texts_to_sequences([text])
    text = pad_sequences(text, maxlen=maxLen, padding='post')
    return text

"""
Function to perform sentiment analysis
"""
def sentiment_analyzer(text, model, tokenizer):
    text = cleaning(text, tokenizer)
    score = model.predict(text)[0][0]
    if score > 0.5:
        sentiment = "POSITIVE"
    else:
        sentiment = "NEGATIVE"
    return score, sentiment
    



