Image Steganography GUI – Encode and Decode Messages in Images

This project is a Python based GUI application developed using Tkinter.  
It allows users to hide a secret message inside an image and later retrieve the hidden message using steganography techniques.

The application supports both PNG and JPEG images.

------------------------------------------------------------

Features

Simple graphical user interface  
Encode secret text inside an image  
Decode hidden text from an image  
Supports PNG and JPEG image formats  
Full screen application  
Image preview before encoding and decoding

------------------------------------------------------------

Technologies Used

Python  
Tkinter  
Pillow  
stegano library

------------------------------------------------------------

Supported Formats

PNG  
Uses LSB method

JPEG  
Uses EXIF header method

------------------------------------------------------------

Requirements

Install the required libraries using

pip install -r requirements.txt

Tkinter comes pre installed with Python.

------------------------------------------------------------

How to Run

Keep the following files in the same folder

steganography.py  
bg1.jpg  
bg2.jpg  

Run the application using

python steganography.py

------------------------------------------------------------

Application Flow

After running the program you will see three buttons

Encode  
Decode  
Exit

------------------------------------------------------------

Encode Process

Click Encode  
Select an image file  
Select the image type as png or jpeg  
Enter the secret message  
Enter the output file name  
Click Encode  
A new image file will be created with the hidden message in the same folder as the selected image

------------------------------------------------------------

Decode Process

Click Decode  
Select the encoded image file  
Select the image type as png or jpeg  
Click Decode  
The hidden message will be shown on the screen

------------------------------------------------------------

Output

For PNG image  
The output file will be saved as filename.png

For JPEG image  
The output file will be saved as filename.jpg

------------------------------------------------------------

Important Notes

For PNG images the message is hidden using the LSB technique  
For JPEG images the message is hidden using the EXIF header technique  
Always select the correct image type while encoding and decoding  
Make sure the background image files bg1.jpg and bg2.jpg are present in the project folder

------------------------------------------------------------

Main Files

steganography.py  
bg1.jpg  
bg2.jpg  

------------------------------------------------------------

Common Issues

If the message is not shown while decoding  
Make sure the correct image type is selected  
Make sure the image was encoded using this application

If the image is not loading  
Check the file path  
Check that the image file exists

------------------------------------------------------------

Project Purpose

This project demonstrates image steganography, GUI development using Tkinter, file handling and basic image processing in Python.

------------------------------------------------------------

Author

Kaveri Padile
Information Technology Student
