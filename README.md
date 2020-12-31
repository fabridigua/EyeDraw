# EyeDraw
Small computer vision software that allows you to draw with your own eyes

***

Preview GIF {TODO}

Table of contents {TODO}

## Basic Overview
This project aims to investigate the potential of computer vision in eyes detection for the development of a real-time application with the use of a simple webcam. **OpenCV** is used for both the GUI and the algorithmic part. 

The execution consists of 3 phases:

| 1. Threshold Settings                                        | 2. Calibration                                               | 3. Draw                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="imgs/1.threshold.png" style="zoom:33%;" />         | <img src="imgs/2.calibration.png" style="zoom:33%;" />       | <img src="imgs/3.paint.png" style="zoom:33%;" />             |
| Your face and eyes are detected in real-time. You must set two important threshold to improve and stabilize the detection. | The calibration is performed making you follow the circle with your eyes for about 30 seconds. | You can draw! Move the cursor on the canvas and draw what you want. Custom options and colors are available. |

**Language**: *Python*

**Frameworks**: *OpenCV*

**Algorithms**: *Haar cascade classifier*, *Blob Detection* , *Homography*

## System Requirements

- **Python 3.8**

- **OpenCV 4.0.1** 

  - Be sure  that OpenCV's haarcascade models '*haarcascade_frontalface_default.xml*' and '*haarcascade_eye.xml*' are properly installed in OpenCV root folder in your Python environment. 

    Files should be in the path returned by this snippet:

    ```python
    >>> import cv2
    >>> from os.path import realpath, normpath
    >>> normpath(realpath(cv2.__file__) + '../../../../Library/etc/haarcascades/')
    ```

    If the path doesn't exist, find the right folder containing the cascade xml filles and change the path in line 7 of `Detector.py` file. 

## Projects structure

```
project
│   README.md
│   LICENSE   
│
└───imgs
│   │   1.threshold.png
│   │   2.calibration.png
│   │   3.paint.png
│
│   main.py		Main file to execute the software
│   Detector.py		Class for face and eye detection			
│   Homography.py	Class for calculation of the homography map
│   GUI.py		Class for the drawing and rendering of the user interface 			
```



## How it works
1 
2
3

# GUI explination

#related

-------------

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple Lorem ipsum dolor generator.
	
## Technologies
Project is created with:
* Lorem version: 12.3
* Ipsum version: 2.33
* Ament library version: 999
	
## Setup
To run this project, install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```