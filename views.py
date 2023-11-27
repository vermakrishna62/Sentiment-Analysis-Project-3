
from .models import SentimentAnalyzer

def sentiment_analysis(request):
    
    sentiment = None
    if request.method == 'POST':
        text = request.POST.get('input_text')
        analyzer = SentimentAnalyzer()
        score = analyzer.analyze_statement(text)
        
        return render(request,'sentiment_analysis.html',{'score':score})
    
    return render(request,'sentiment_analysis.html')
