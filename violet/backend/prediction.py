import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Load the recycling_model.keras
model = tf.keras.models.load_model('recycling_model.keras')
# Load the saved class indices
# Dynamically recreate class indices using the training directory
train_data = ImageDataGenerator(rescale=1./255)
train_gen = train_data.flow_from_directory(
    directory=r'C:\Users\donov\.cache\kagglehub\datasets\saumyamohandas\garbage-classification-image-dataset\versions\1\dataset\Training', 
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)
# Reverse the mapping from index to class label
class_labels = {v: k for k, v in train_gen.class_indices.items()}

# Set up the image for processing (resizing and normalization)
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

# PUT IMAGE PATH HERE
img_path = r"C:\Users\donov\.cache\kagglehub\datasets\saumyamohandas\garbage-classification-image-dataset\versions\1\dataset\Testing\cardboard\cardboard363.jpg"
img_array = preprocess_image(img_path)
# Make prediction and get the type of material
predictions = model.predict(img_array)
predicted_class_index = np.argmax(predictions, axis=1)[0]
predicted_label = class_labels[predicted_class_index]
print(f"Predicted class: {predicted_label}")