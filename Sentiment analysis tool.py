from textblob import TextBlob

def analyze_sentiment(statement):
    blob = TextBlob(statement)
    polarity = blob.sentiment.polarity  # Range is from -1 (negative) to +1 (positive)

    # Map polarity to scores
    if polarity > 0:
        positive_score = int(polarity * 100)
        negative_score = 0
    elif polarity < 0:
        positive_score = 0
        negative_score = int(abs(polarity) * 100)
    else:
        positive_score = 0
        negative_score = 0

    # Neutral score is higher when polarity is closer to 0
    neutral_score = int((1 - abs(polarity)) * 100)

    return {
        "Positive Score": positive_score,
        "Negative Score": negative_score,
        "Neutral Score": neutral_score
    }