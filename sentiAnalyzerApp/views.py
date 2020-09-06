from django.shortcuts import render
import json
import numpy as np
from .apps import SentianalyzerappConfig
from django.http import JsonResponse
import pandas as pd
import numpy as np
import re
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer


# Home Page
def home(request):
    context = {
    }
    return render(request, 'sentiAnalyzerApp/home.html', context)

# Predict Method
def predict(request):
    if request.method == "POST":
        data = request.POST['data']
        response = SentianalyzerappConfig.loaded_model.predict(clear(data))
        print(response)
        return JsonResponse(str(response[0][0]), safe=False)

# Method to create clean text
def clear(text):
    tokenizer = SentianalyzerappConfig.tokenizer
    cleanText = pad_sequences(
    tokenizer.texts_to_sequences([preprocess_text(text)]),
    padding='post',
    maxlen=100
    )
    return cleanText


# Method to do some preprocessing
def preprocess_text(sen):
    # Removing html tags
    sentence = remove_tags(sen)
    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)
    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)
    return sentence

#This code replaces anything which is enclosed withon <---> with spaces.
TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)