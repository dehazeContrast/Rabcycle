import kagglehub
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
import os

# Download kaggle dataset for recyclable materials
path = kagglehub.dataset_download("ashwinshrivastav/most-common-recyclable-and-nonrecyclable-objects")
print("Path to dataset files:", path)

# Create training and validation sets from the dataset
train_dir = os.path.join(path, 'train') 
validation_dir = os.path.join(path, 'validation')
train_data = ImageDataGenerator(rescale=1./255)
validation_data = ImageDataGenerator(rescale=1./255)

train_gen = train_data.flow_from_directory(
    directory=train_dir,
    target_size=(224, 224),
    batch_size=100,
    class_mode='categorical',
    shuffle=True
)
validation_gen = validation_data.flow_from_directory(
    directory=validation_dir,
    target_size=(224, 224),
    batch_size=25,
    class_mode='categorical',
    shuffle=False  # Validation data should not be shuffled
)

# CNN model
model = Sequential([
    # Use a pre-trained MobileNetV2 model for feature extraction
    tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet'),
    # Freeze layers of base model
    tf.keras.layers.GlobalAveragePooling2D(),
    
    # Add custom fully connected layers
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.5),  # Dropout to avoid overfitting
    tf.keras.layers.Dense(len(train_gen.class_indices), activation='softmax')  # Output layer (number of classes)
])

# Freeze the base model
model.layers[0].trainable = False

# Step 6: Compile the model
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Step 7: Train the model
history = model.fit(
    train_gen,
    epochs=50,  # Adjust the number of epochs as needed
    validation_data=validation_gen
)

# Step 8: Evaluate the model
validation_loss, validation_accuracy = model.evaluate(validation_gen)
print(f"Validation Loss: {validation_loss}")
print(f"Validation Accuracy: {validation_accuracy}")

# Step 9: Save the model
model.save('recycling_model.h5')

# Type of recyclable for each image
class_names = ['Bottle', 'Can', 'Juice Box', 'Milk Carton', 'Stytrofoam', 'Utensil']