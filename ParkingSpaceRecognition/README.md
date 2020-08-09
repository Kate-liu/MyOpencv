# Parking Space Recognition

This is Parking Space Recognition test project.


## Install package

- pip install keras==2.3.1

- pip install tensorflow==1.15.3

- pip install opencv-python==3.4.10.35
    
- pip install opencv-contrib-python==3.4.10.35

- ps：install version need equality.



## Project Introduce

We need use tensorflow to training the empty and occupied parking picture.

Then, use the training result  car1.h5 solve the test parking images and the video of parking space. 


## Implementation approach

### Program introduce

Training Data: [TrainData](../../../CodeStudy/Opencv/ParkingSpaceRecognition/TrainData)

Video Data: [VideoData](../../../CodeStudy/Opencv/ParkingSpaceRecognition/VideoData)

Test Data: [TestData](../../../CodeStudy/Opencv/ParkingSpaceRecognition/TestData)

Training program: [TrainingParking.py](../../../CodeStudy/Opencv/ParkingSpaceRecognition/TrainingParking.py)
(Warning: This code running can cover origin car-default.h5)

Parking Recognition Test program: [ParkingRecognitionTestData.py](../../../CodeStudy/Opencv/ParkingSpaceRecognition/ParkingRecognitionTestData.py)

Parking Recognition Video program: [ParkingRecognitionVideoData.py](../../../CodeStudy/Opencv/ParkingSpaceRecognition/ParkingRecognitionVideoData.py)



### Training runtime Error

If you find error of this `Exception: URL fetch failure on https://github.com/fchollet/deep-learning-mo .......`,

then you need to use the URL `https://github.com/fchollet/deep-learning-mo .......`

download the `xxx.h5` file.

then hand movement this download file to the `~/.keras/models`.

so, this error is solved.

If you can't download this h5 file, then use the link:

Baidu Netdisk link: https://pan.baidu.com/s/1KP-9wBcye-tl7Q15i2QR_Q
Code: v3sy


### Train Result

If you don't use yourself training result, can download this h5 result file.

Baidu Netdisk link: https://pan.baidu.com/s/1u951cynUZsLrlLMznU0B0A
Code: rdp7



### Content tree
    
    
        ├─  README.md
        ├─  DocumentOCR.py
        │
        ├─ DocumentData
        │   ├─  page.jpg
        │   ├─  receipt.jpg
        │
        ├─ OCRData
        │   ├─  scanDemo.jpg
        │
        └─ 



### Flow chart

![]()

