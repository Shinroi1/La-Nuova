import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

# Initialize WordNetLemmatizer for stemming words
lemmatizer = WordNetLemmatizer()

# Load intents from JSON file
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# Load the pre-trained model
model = load_model('chatbot_simplilearnmodel.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.15
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    if len(intents_list) > 0:
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                if tag == 'menu_recommendation':
                    response = random.choice(i['responses'])    
                    response = response.replace('{menu1}', i.get('menu1', ''))
                    response = response.replace('{menu2}', i.get('menu2', ''))
                    response = response.replace('{menu3}', i.get('menu3', ''))                
                else:
                    response = random.choice(i['responses'])
                break
    else:
        response = "I don't understand..."
    return response

print("YES! Bot is running!")

while True:
    message = input("You: ")
    if message.lower() in ['quit', 'bye', 'exit']:
        print("Bot: Goodbye!")
        break
    else:
        ints = predict_class(message)
        res = get_response(ints, intents)
        print("Bot:", res)
