from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def main():
    print("Welcome to Sentiment Analysis!")
    while True:
        text = input("Enter text (or type 'exit' to quit): ")
        if text.lower() == "exit":
            print("Goodbye!")
            break
        sentiment = analyze_sentiment(text)
        print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
