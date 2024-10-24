import tensorflow as tf
print(tf.__version__)


##import tensorflow as tf
##from tensorflow.keras.preprocessing import image
##from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
##import numpy as np
##import sys
##
### Load the model (replace 'your_model.h5' with the actual model path)
##model_path = 'your_model.h5'
##model = tf.keras.models.load_model(model_path)
##
### Load an image file that contains the object to be identified
##image_path = 'your_image.jpeg'
##img = image.load_img(image_path, target_size=(224, 224))  # Resize to the input size expected by the model
##
### Convert the image to a numpy array
##img_array = image.img_to_array(img)
##
### Add an extra dimension for batch size
##img_array = np.expand_dims(img_array, axis=0)
##
### Preprocess the image based on the model's requirements (VGG16 example)
##img_array = preprocess_input(img_array)
##
### Make a prediction
##predictions = model.predict(img_array)
##
### Decode the prediction (for classification models, assuming it's a classification task)
### If you're using a custom model, you might have different post-processing.
##decoded_predictions = decode_predictions(predictions, top=3)[0]
##
### Print top-3 predictions
##for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
##    print(f"{i + 1}: {label} ({score:.2f})")
##
