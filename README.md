# Sign Language to Text Conversion

This project uses computer vision and deep learning to convert American Sign Language finger spelling into text in real-time. It allows deaf and hard of hearing individuals to more easily communicate with others not familiar with sign language.

## Prerequisites

- Python 3.8+
- OpenCV
- TensorFlow 2.0+
- Keras
- Numpy
- Tkinter
- Hunspell

## Installation

1. Clone the repo:
   ```sh
   git clone https://github.com/yourusername/Sign-Language-to-Text.git 
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   .\venv\Scripts\activate # Windows 
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the main application script:

```sh
python app_working.ipynb
```

This will open the sign language to text conversion application window:

![Application Window][]

Position your hand within the detection frame and perform ASL finger spelling gestures. The application will recognize the signs in real-time and display:
- The predicted letter
- The predicted word
- The predicted sentence

Suggested word completions are displayed at the bottom which can be selected to autocomplete the current word.

## Methodology

The high-level methodology is:

1. Frame capture and ROI extraction 
2. Preprocessing (grayscale, blur, thresholding)
3. Prediction using CNN model
4. Post-processing of predictions
5. Displaying results

### Preprocessing

Each captured frame undergoes:
1. Grayscale conversion 
2. Gaussian blur
3. Adaptive thresholding
4. Binary thresholding

This isolates the hand gesture and reduces noise.![Preprocessing][]

### CNN Model

The core of the system is a Convolutional Neural Network which classifies the preprocessed image into one of 26 classes (A-Z).

The model architecture is:

- Conv2D layer (32 filters, 3x3 kernel)
- Max Pooling (2x2) 
- Conv2D layer (32 filters, 3x3 kernel)
- Max Pooling (2x2)
- Flatten
- Dense layer (128 units, ReLU) 
- Dropout (0.4)
- Dense layer (96 units, ReLU)
- Dropout (0.4)
- Dense layer (64 units, ReLU)
- Output Dense layer (27 units, Softmax)

The model is trained on a custom dataset of ASL finger spelling images. Data augmentation is used to improve robustness.

### Prediction Flow

For each frame:
1. Preprocess frame
2. Get CNN prediction
3. If high confidence, update current letter
4. Else if timeout, update word and sentence
5. Display results
6. Get word suggestions from Hunspell
7. Display suggestions

### Example

Suppose the user finger spells "H-E-L-L-O". 

1. "H" is held, CNN predicts "H". Current letter becomes "H".
2. "E" is held, CNN predicts "E". Current letter becomes "E", word becomes "HE".
3. "L" is held, CNN predicts "L". Current letter becomes "L", word becomes "HEL".
4. "L" is held, CNN predicts "L". Current letter stays "L", word becomes "HELL".
5. "O" is held, CNN predicts "O". Current letter becomes "O", word becomes "HELLO".
6. Hunspell suggests completions like "HELLOS", "HELLOED", etc.
7. User can select a suggestion or continue finger spelling.

The sentence continues to grow until the user clears it with a keyboard interrupt.

## Conclusion

This real-time sign language to text conversion system using deep learning enables easier communication between deaf/hard of hearing individuals and others. The CNN model accurately classifies ASL finger spelling gestures, while the Hunspell integration provides intelligent word completions for faster communication.

Future work could expand this to complete ASL gestures beyond finger spelling, and potentially other sign languages as well. It could also be ported to mobile devices for even greater accessibility.
