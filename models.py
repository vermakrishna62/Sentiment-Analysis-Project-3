
from textblob import TextBlob


class SentimentAnalyzer(models.Model):
    
    def analyze_statement(self,data):
        analysis = TextBlob(data)
        
        data_score = analysis.sentiment.polarity
        
        if data_score > 0:
            sentiment = "positive"
        elif data_score < 0:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        return sentiment
