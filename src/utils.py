import re
import string
import html

def clean_text(text):
    text = html.unescape(text)                     
    text = re.sub(r'<.*?>', '', text)               
    text = text.translate(str.maketrans('', '', string.punctuation)) 
    text = re.sub(r'[^a-zA-Z]', ' ', text)          
    text = text.lower().strip()                     
    return text


