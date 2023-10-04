from flask import Flask, render_template, request

import tensorflow as tf
import cv2
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('F:\portfolio_projects\h5_CNN_SVHN.h5') # path to the model to be loaded


@app.route('/', methods=['GET'])
def hello_word():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile= request.files['imagefile']
    image_path = "./images/" + imagefile.filename #saves the image to 'images' folder
    imagefile.save(image_path)

    # Load and preprocess the image
    image = cv2.imread(image_path)
    
    # Calculate the mean of the RGB channels
    image = np.mean(image, axis=2, dtype=np.uint8)

    # Resize the image to 32x32
    image = cv2.resize(image, (32, 32))
    image = image.reshape((1, 32, 32, 1))  # Reshape for model input
    #image = image.astype('float32') / 255.0  # Normalize to [0, 1]

    # make predictions
    predictions = model.predict(image)

    # Assuming predictions are class probabilities, finding the class with the highest probability
    predicted_class = np.argmax(predictions)

    # Rounding the associated probability with two decimal points
    max_probability = np.max(predictions)
    probability = round(max_probability * 100, 2)


    classification = '%s (%.2f%%)' % (predicted_class, probability)



    return render_template('index.html', prediction=classification)


if __name__ == '__main__':
    app.run(port=3000, debug=True)