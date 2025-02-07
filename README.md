First, I used Teachable Machine by Google to train an image classification model. I uploaded images for two classes: the first represents an iPhone, and the second represents a laptop. After training, I downloaded the model in TensorFlow format.

Libraries Used:
- TensorFlow through Keras is used to load the trained model (load_model) and use it for predicting the categories based on the input images. It is also used in the prediction process using model.predict() to obtain predictions based on the processed data.
  Keras: To load and use the trained model.
- PIL (Pillow): For image processing and converting images to the required format.
- NumPy: For handling and preparing the data before feeding it to the model.

Steps Performed in the Code:

1. Loading the Model
I loaded the trained model stored in an .h5 file, which contains the model's architecture and learned weights.

2. Reading Class Labels
I opened the labels.txt file to read the class names, where each line represents a class label.

3. Preparing Image Data
- The first image was opened and converted to RGB format.
- The image was resized to the required dimensions (224x224 pixels) using a resizing function.
- The image was converted into a numerical array to be compatible with the model.
- The image was normalized, scaling pixel values to a range between -1 and 1 to match the model's training conditions.

4. Predicting the Class
- The processed image data was fed into the model for prediction.
- The most probable class was identified using an operation to find the highest confidence score, and the model outputs the class with the highest probability.
- The predicted class name (with the highest confidence score) and the confidence score were printed.

5. Predicting the Second Image
The same steps were repeated for the second image located in a different path, and its class was predicted accordingly. After running the code on both images, I obtained the following prediction results for the two classes, as shown in the terminal output:

-First image (iPhone):
  - Predicted class: Class 1 (iPhone)
  - Confidence score: 0.9999856 (99.99856%)

- Second image (Laptop):
  - Predicted class: Class 2 (Laptop)
  - Confidence score: 0.9999449 (99.99449%)

These results indicate that the model can accurately recognize images classified within the categories it was trained on, with a very high level of confidence. The model predicts the class with the highest probability, and the confidence score for both images is extremely close to 1, showing reliable classification results.

![image alt](https://github.com/aishah8/model.py./blob/9b4fc6230d9895c2db495727354494e76dbf21bc/Screenshot%202025-01-22%20135604.png)
![image alt](https://github.com/aishah8/model.py./blob/6c77ba02d5cde0f0aeeb3c53e10c98a986b46d38/Screenshot%20(1).png)
![image alt](https://github.com/aishah8/model.py./blob/8ab55f5d61f1e3e3f2a1c8504a5931e0f366db4c/Screenshot%20(2).png)

