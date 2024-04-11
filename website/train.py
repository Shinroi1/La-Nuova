import random
import json
import pickle
import numpy as np
import tensorflow as tf

import nltk
from nltk.stem import WordNetLemmatizer

# Initialize WordNetLemmatizer for stemming words
lemmatizer = WordNetLemmatizer()

# Load intents from JSON file
intents = json.loads(open('intents.json').read()) 

# Initialize lists to store words, classes, and documents
words = []
classes = []
documents = []
# Define a list of characters to ignore
ignore_letters = ['?', '!', '.', ',']

# Iterate through intents and their patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize each pattern into words
        word_list = nltk.word_tokenize(pattern)
        # Extend words list with tokenized words
        words.extend(word_list)
        # Append tuple of word list and intent tag to documents list
        documents.append((word_list, intent['tag']))
        # Add intent tag to classes list if not already present
        if intent['tag'] not in classes:
            classes.append(intent['tag'])  

# Lemmatize words and filter out ignore_letters
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
# Sort and make a set of words
words = sorted(list(set(words)))

# Sort and make a set of classes
classes = sorted(list(set(classes)))

# Save words and classes into pickle files
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Initialize training data
training = []
# Create empty list with length equal to the number of classes
output_empty = [0] * len(classes)

# Iterate through documents to create bag of words
for document in documents:
    bag = []
    word_patterns = document[0]
    # Lemmatize and lowercase words in patterns
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    # Create a bag of words representation
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    # Create output row with 1 at the index of the class and 0s elsewhere
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    # Append bag and output row to training data
    training.append([bag, output_row])
    
# Shuffle training data
random.shuffle(training)
# Unzip training data into trainX (input) and trainY (output)
trainX, trainY = zip(*training)

# Convert trainX and trainY to numpy arrays
trainX = np.array(trainX)  # Input data
trainY = np.array(trainY)  # Output data

# Define input layer
inputs = tf.keras.Input(shape=(len(trainX[0]),))
# Add a dense layer with ReLU activation
x = tf.keras.layers.Dense(128, activation='relu')(inputs)
# Add dropout layer to prevent overfitting
x = tf.keras.layers.Dropout(0.5)(x)
# Add another dense layer with ReLU activation
x = tf.keras.layers.Dense(64, activation='relu')(x)
# Output layer with softmax activation
outputs = tf.keras.layers.Dense(len(trainY[0]), activation='softmax')(x)

# Create the model using the Functional API
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Define the optimizer without 'decay' argument
opt = tf.keras.optimizers.SGD(momentum=0.9, nesterov=True)

# Compile the model with categorical crossentropy loss and defined optimizer
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# Train the model
hist = model.fit(trainX, trainY, epochs=200, batch_size=5, verbose=1)

# Save the model
model.save('chatbot_simplilearnmodel.h5', hist)

# Print "Done" when everything is finished
print("Done")
