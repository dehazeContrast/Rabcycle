import kagglehub
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

# Download kaggle dataset for recyclable materials
path = kagglehub.dataset_download("saumyamohandas/garbage-classification-image-dataset")
print("Path to dataset:", path)

# Create training and validation sets from the dataset
# IMPORTANT: CHANGE PATH FOR USER
train_dir = 'C:\Users\donov\.cache\kagglehub\datasets\saumyamohandas\garbage-classification-image-dataset\versions\1\dataset\Training'
validation_dir = 'C:\Users\donov\.cache\kagglehub\datasets\saumyamohandas\garbage-classification-image-dataset\versions\1\dataset\Testing'

# Variation for better training on recognizing less "clean" photos
train_data = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)
validation_data = ImageDataGenerator(rescale=1./255)

train_gen = train_data.flow_from_directory(
    directory=train_dir,
    target_size=(224, 224),
    class_mode='categorical',
    shuffle=True
)
validation_gen = validation_data.flow_from_directory(
    directory=validation_dir,
    target_size=(224, 224),
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

# Freeze base model
model.layers[0].trainable = False

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train
history = model.fit(
    train_gen,
    epochs=50, # run-throughs
    validation_data=validation_gen
)

# Evaluate
validation_loss, validation_accuracy = model.evaluate(validation_gen)
print(f"Validation Loss: {validation_loss}")
print(f"Validation Accuracy: {validation_accuracy}")

# Save
model.save('recycling_model.keras')