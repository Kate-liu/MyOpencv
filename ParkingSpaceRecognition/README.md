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

Training Data: [TrainData](./TrainData)

Training Result: [TrainResult](./TrainResult)

Test Data: [TestData](./TestData)

Test Result: [TestResult](./TestResult)

CNN Data: [CNNData](./CNNData)

Video Data: [VideoData](./VideoData)

Training program: [TrainingParking.py](./TrainingParking.py)
(Warning: This code running can cover origin car-default.h5)

Parking Recognition Test program: [ParkingRecognitionTestData.py](./ParkingRecognitionTestData.py)

Parking Recognition Video program: [ParkingRecognitionVideoData.py](./ParkingRecognitionVideoData.py)



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
    
    .
    │  
    ├── Parking.py
    ├── ParkingRecognitionTestData.py
    ├── ParkingRecognitionVideoData.py
    ├── TrainingParking.py
    ├── README.md
    │ 
    ├── CNNData
    │   └── CNNData-default.txt
    ├── TestData
    │   ├── scene1380.jpg
    │   ├── scene1410.jpg
    │   └── spot_dict.pickle
    ├── TestResult
    │   └── with_parking.jpg
    ├── TrainData
    │   ├── test
    │   │   ├── empty
    │   │   │   ├── spot1.jpg
    │   │   │   ├── ...
    │   │   │   └── spot89.jpg
    │   │   └── occupied
    │   │       ├── spot100.jpg
    │   │       ├── ...
    │   │       └── spot98.jpg
    │   └── train
    │       ├── empty
    │       │   ├── spot84.jpg
    │       │   ├── ...
    │       │   └── spot87.jpg
    │       └── occupied
    │           ├── spot10.jpg
    │           ├── ...
    │           └── spot99.jpg
    ├── TrainResult
    │   └── car-default.h5
    └── VideoData
        └── parking_video.mp4
    




