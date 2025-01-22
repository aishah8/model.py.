from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your first image
image1 = Image.open("C:/Users/96655/Desktop/LAP1/OIP 333.jpg").convert("RGB")

# Resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image1 = ImageOps.fit(image1, size, Image.Resampling.LANCZOS)

# Turn the image into a numpy array
image_array1 = np.asarray(image1)

# Normalize the image
normalized_image_array1 = (image_array1.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array1

# Predict the first image
prediction1 = model.predict(data)
index1 = np.argmax(prediction1)
class_name1 = class_names[index1]
confidence_score1 = prediction1[0][index1]

# Print prediction and confidence score for the first image
print("Class for image1:", class_name1[2:], end="")
print("Confidence Score for image1:", confidence_score1)

# Replace this with the path to your second image
image2 = Image.open("C:/Users/96655/Desktop/LAP1/OIP (53).jpg").convert("RGB")

# Resizing the image to be at least 224x224 and then cropping from the center
image2 = ImageOps.fit(image2, size, Image.Resampling.LANCZOS)

# Turn the image into a numpy array
image_array2 = np.asarray(image2)

# Normalize the image
normalized_image_array2 = (image_array2.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array2

# Predict the second image
prediction2 = model.predict(data)
index2 = np.argmax(prediction2)
class_name2 = class_names[index2]
confidence_score2 = prediction2[0][index2]

# Print prediction and confidence score for the second image
print("Class for image2:", class_name2[2:], end="")
print("Confidence Score for image2:", confidence_score2)

