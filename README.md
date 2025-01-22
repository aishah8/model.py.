First, I used Teachable Machine by Google to train an image classification model. I uploaded images for two classes: the first represents an iPhone, and the second represents a laptop. After training, I downloaded the model in TensorFlow format.  

 Libraries Used:  
- Keras: To load and use the trained model.  
- PIL (Pillow): For image processing and converting images to the required format.  
- NumPy: For handling and preparing the data before feeding it to the model.  

Steps Performed in the Code:  
1. Loading the Model  
   - I loaded the trained model stored in an .h5 file, which contains the model's architecture and learned weights.  

2. Reading Class Labels  
   - I opened the labels.txt file to read the class names, where each line represents a class label.  

3. Preparing Image Data 
   - The first image was opened and converted to RGB format.  
   - The image was resized to the required dimensions (224x224 pixels) using a resizing function.  
   - The image was converted into a numerical array to be compatible with the model.  
   - The image was normalized, scaling pixel values to a range between -1 and 1 to match the model's training conditions.  

4. Predicting the Class  
   - The processed image data was fed into the model for prediction.  
   - The most probable class was identified using an operation to find the highest confidence score.  
   - The predicted class name and the confidence score were printed.  

5. Predicting the Second Image 
   - The same steps were repeated for the second image located in a different path, and its class was predicted accordingly.
     After running the code on both images, I obtained the following prediction results for the two classes, as shown in the terminal output:

1. First image (iPhone):  
   - Predicted class: iPhone  
   - Confidence score: 0.9999 ( 99.99%)  

2. Second image (Laptop): 
   - Predicted class: Laptop  
   - Confidence score: 0.9999 ( 99.99%)  

These results indicate that the model can accurately recognize images classified within the categories it was trained on, with a high level of confidence.
![image alt](https://github.com/aishah8/model.py./blob/0c07a406e80d0c6466c9aeff5d71cecfaefb0638/Screenshot%20(1).png)
![image alt](

