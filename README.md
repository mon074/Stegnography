# Steganography-Based Secret Message Encryption and Decryption

## Overview

This Python project demonstrates the use of steganography to hide secret messages within an image and retrieve them upon providing the correct passcode. The program leverages OpenCV for image processing and provides a custom encryption and decryption method.

## Features

- **Steganography**: Hide a secret message within an image discreetly.
- **Custom Encryption**: Unique method using ASCII values for encoding.
- **User Interaction**: Engaging program with user inputs.
- **Image Manipulation**: Advanced tasks using OpenCV.
- **Security**: Passcode protection for message access.
- **Error Handling**: Ensures graceful program exit.

## Requirements

- Python 3.x
- OpenCV (`cv2`)

##Install the required dependencies:

bash
pip install opencv-python

1). Follow the prompts to:

 *Enter the image filename (e.g., 'mypic.png').

 *Enter the secret message.

 *Enter the passcode for encryption.

2). The program will save the encrypted image as encryptedImage.png and open it.

3). To decrypt the message, follow the prompt to enter the passcode. If the passcode matches, the secret message will be displayed.
