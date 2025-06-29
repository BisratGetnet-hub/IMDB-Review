# IMDB Review Sentiment Analysis

This project is a machine learning application that performs **sentiment analysis** on IMDB movie reviews. It classifies reviews as either **positive** or **negative** using a trained **Logistic Regression** model and provides an interactive interface built with **Streamlit**.

To see the final UI of this project in StreamLit community cloud- [Click Here](https://imdb-review-fzmr9ukjlpnd34kcyb3aj2.streamlit.app/)

---

## 🚀 Features

- Cleaned and preprocessed IMDB movie review dataset
- Trained logistic regression model for sentiment prediction
- Utility functions for text preprocessing
- Streamlit-based web interface for live prediction

---

## 📁 Project Structure

```
IMDB-Review/
├── predict.py                  # Script to load model and predict
├── requirements.txt            # Project dependencies
├── Data/
│   └── IMDB Dataset.csv        # Raw dataset
├── Model/
│   └── logistic_model.pkl      # Trained ML model
├── src/
│   ├── main.ipynb              # Notebook for exploration/training
│   ├── utils.py                # Text preprocessing utilities
│   └── streamlit/
│       └── homepage.py         # Streamlit web app
```

---

## 🧠 Model

- **Algorithm**: Logistic Regression
- **Libraries**: Scikit-learn
- **Features**: TF-IDF vectorized text data
- **Target**: Binary sentiment (Positive / Negative)

---

## 🛠 Installation & Setup

1. **Clone the repository**:

```bash
git clone https://github.com/BisratGetnet-hub/IMDB-Review.git
cd IMDB-Review
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**:

```bash
streamlit run src/streamlit/homepage.py
```

---

## 📈 Usage

- Input any movie review text into the Streamlit app
- Get an instant prediction on whether the review is positive or negative

---

## 📊 Dataset

- **Source**: [IMDB Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- **Columns**: `review`, `sentiment`

---

## 📌 Requirements

- Python 3.8+
- scikit-learn
- pandas
- streamlit

(Full list in `requirements.txt`)

---

## ✍️ Author

**Bisrat Getnet**

- GitHub: [BisratGetnet-hub](https://github.com/BisratGetnet-hub)
- Gmail - bisratgetnet21@gmail.com

---

