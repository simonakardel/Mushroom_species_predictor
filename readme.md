# Fungi-finder - Mushroom species predictor

This project is a web-based application designed to predict the species of mushrooms from uploaded images. It leverages a deep learning model for the predictions and provides a user-friendly interface for uploading images and displaying results. This project was developed as a final exam project for my machine learning class.

## Features
- **Image Upload:** Allows users to upload images of mushrooms.
- **Prediction:** Uses a trained deep learning model to predict the species of the mushroom.
- **Description:** Provides a description of the predicted species.
- **User Interface:** Simple and intuitive interface for ease of use.

## Project Structure
- **app.py:** Contains the Flask application code.
- **index.html:** The main HTML file for the web interface.
- **mushrooms_model.h5:** The trained deep learning model.
- **requirements.txt:** Lists the dependencies needed for the project.

## Installation

Clone the repository:

```bash
git clone https://github.com/simonakardel/Mushroom_species_predictor.git
cd Mushroom_species_predictor
```

Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the flask application:
```bash
python app.py
```

## Usage

- Navigate to the Application
- Open your web browser and go to http://127.0.0.1:5000/.
- Upload an Image
- Click on the "Choose File" button.
- Select an image of a mushroom from your device.
- Click on the "Predict" button.
- The application will display the predicted species of the mushroom along with a description.


## Dependencies

The project requires the following Python packages:

- Flask==3.0.3
- numpy==1.26.4
- tensorflow==2.16.2
- h5py==3.11.0
- and other dependencies listed in requirements.txt.

## CNN Model
The CNN model used in this project was trained on images of 9 different mushroom species:

- Agaricus
- Amanita
- Boletus
- Cortinarius
- Entoloma
- Hygrocybe
- Lactarius
- Russula
- Suillus

### Model Architecture
The model architecture includes several types of layers, each serving a specific purpose to ensure efficient learning and accurate predictions:

**Convolutional Layers:** These layers apply convolution operations to the input data, extracting important features such as edges, textures, and shapes. Each convolutional layer uses filters (kernels) that slide over the input image to create feature maps. These feature maps highlight important characteristics of the input image, making it easier for the model to learn distinguishing features of different mushroom species.

**ReLU (Rectified Linear Unit) Activation:** After each convolutional layer, a ReLU activation function is applied. This introduces non-linearity to the model, allowing it to learn more complex patterns. The ReLU function sets all negative values in the feature maps to zero while keeping positive values unchanged, which helps in reducing the likelihood of vanishing gradients during training.

**Max Pooling Layers:** These layers perform down-sampling by selecting the maximum value from each region of the feature maps. Max pooling reduces the spatial dimensions (width and height) of the feature maps while retaining the most important information. This not only reduces the computational load but also makes the model more robust to variations and distortions in the input images.

**Dropout Layers:** During training, dropout layers randomly set a fraction of input units to zero at each update step. This helps prevent overfitting by ensuring that the model does not rely too heavily on specific neurons. Dropout layers force the model to learn more general and robust features, improving its performance on unseen data.

**Flatten Layer:** This layer converts the 2D feature maps into a 1D vector, making it suitable for input into fully connected (dense) layers. Flattening prepares the data for the final classification stage.

**Dense Layers:** Fully connected layers, or dense layers, take the flattened vector and apply learned weights to output the final predictions. These layers combine features learned by previous layers to classify the input image into one of the 9 mushroom species.

**Softmax Activation:** The final dense layer uses a softmax activation function to produce a probability distribution over the 9 classes. This indicates the likelihood of the input image belonging to each species, with the class having the highest probability being the predicted species.

### Training Process
- **Data Preprocessing:** Cleaned and preprocessed the images to ensure consistency and quality for training.
- **Data Augmentation:** Applied techniques such as rotation, scaling, and flipping to artificially increase the size of the dataset and improve the model's ability to generalize.
- **Model Training:** Trained the model using TensorFlow and Keras, optimizing hyperparameters and monitoring performance through validation loss and accuracy.
- **Model Evaluation:** Evaluated the model on a separate test set to ensure its accuracy and generalization capabilities.

## License

[MIT](https://choosealicense.com/licenses/mit/)