# Steganography
A simple implementation of encoding and decoding text into images and image into images using python.

### Project Description: 

Steganography is an art that involves communication of secret data in an appropriate carrier, e.g., image, audio, TCP/IP header files. For hiding secret data in digital images, large varieties of stenographic techniques are available, but we will be mainly focus on LSB technique where we will hide data in the least significant bit of a pixel (by pixel we represent the image). This Method works by adding random noises to the signal, the information is concealed inside carrier and spread across the frequency spectrum.  
Least Significant Bit (LSB) embedding is a simple strategy to implement steganography. Like all steganographic methods, it embeds the data into the cover so that it cannot be detected by a casual observer. The technique works by replacing some of the information in a given pixel with information from the data in the image. While it is possible to embed data into an image on any bit-plane, LSB embedding is performed on the least significant bit(s). This minimizes the variation in colors that the embedding creates. For example, embedding into the least significant bit changes the color value by one.  
Steganography avoids introducing as much variation as possible, to minimize the likelihood of detection. In a LSB embedding, we always lose some information from the cover image. This is an effect of embedding directly into a pixel. To do this we must discard some of the cover’s information and replace it with information from the data to hide. LSB algorithms have a choice about how they embed that data to hide. They can embed losslessly, preserving all information about the data, or the data may be generalized so that it takes up less space.

##### Example:

The letter 'A' has an ASCII code of 65(decimal), which is 1000001 in binary. It will need three consecutive pixels for a 24-bit image to store an 'A':  
Let's say that the pixels before the insertion are:  
10000000.10100100.10110101, 10110101.11110011.10110111, 11100111.10110011.00110011  
Then their values after the insertion of an 'A' will be:  
10000001.10100100.10110100, 10110100.11110010.10110110, 11100110.10110011.00110011  

### Modules and working: 

##### Text Hide:

*	In this module, we will first calculate the size of the text which is to be embedded in an image.
*	Size of the image is converted into binary format and then insert the binary value in the target image.
*	Bit stuffing: Stuffed a 16 bit ‘0’ after the size of text so that the retrieval of the information will be easy.
*	Now after this, we will simply convert the text in binary format and put it in the LSB of the 2 bytes.

##### Text Unhide:


*	We will take the stego image which we created earlier.
*	Starting from the top left corner of an image we will extract 16bit and then check if it is 16 bit ‘0’ or not.
*	If it is 16 bit ‘0’ then we stop the process of extracting the LSB bits from an image. 
*	Then the number which we have got now will be combined and the length or the size of the image is determined
*	To extract the actual text we will run a forloop from 16 bit ‘0’ till the size of the text and then we will combine it and get the actual text which we have embedded earlier in an image.

##### Image Hide:

*	In this module, we will first calculate the size of the image which is to be embedded in an image.
*	Size of the image is converted into binary format.
*	We divide the targeted image in 3 channels RGB and insert the binary value in the first channel and then move to the next channel and so on.
*	Bit stuffing: Stuffed a 16 bit ‘0’ after the size of image so that the retrieval of the information will be easy.
*	Now after this, we will simply convert the image information in binary format and put it in the LSB of the 2 bytes.

##### Image Unhide:

*	We will take the stego image which we created earlier.
*	Starting from the top left corner of an image with the Red as a current channel and then B and G respectively we will extract 16bit and then check if it is 16 bit ‘0’ or not.
*	If it is 16 bit ‘0’ then we stop the process of extracting the LSB bits from an image. 
*	Then the number which we have got now will be combined and the length or the image which is embedded in the stego image is determined
*	To extract the actual image we will run a for loop from 16 bit ‘0’ till the size of the image and then we will combine it and get the actual image which we have embedded earlier in target image.


