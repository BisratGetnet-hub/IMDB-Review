import joblib
import sys
from src.utils import clean_text


if len(sys.argv) < 2:
    print("Please provide a text input.")
    sys.exit()

model = joblib.load("./Model/logistic_model.pkl")


def predict_sentiment(text):
    text = clean_text(text)
    pred = model.predict([text])[0]
    return "Positive" if pred == 1 else "Negative"


input_text = " ".join(sys.argv[1:])
pred = predict_sentiment(input_text)


print(f"Input: {input_text}")
print(f"Predicted Sentiment: {pred}")
