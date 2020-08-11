# Target Tracking

This is Target Tracking test project.

And here is two method solve the target tracking.


## OpenCV MultiTracker

### Install package and download

- pip install opencv-python==4.3.0.38
    
- pip install opencv-contrib-python==4.3.0.38

- If found this error:

        Traceback (most recent call last):
          File "E:/PYTHON_Space/opencv/TargetTracking/OpenCVMultiTracker/multi_object_tracking.py", line 16, in <module>
            "csrt": cv2.TrackerCSRT_create,
        AttributeError: module 'cv2.cv2' has no attribute 'TrackerCSRT_create'

- you need uninstall opencv and use terminal install package, then it will be OK!

        pip uninstall opencv-python
        pip uninstall opencv-contrib-python
        
        pip install opencv-python -i https://mirrors.aliyun.com/pypi/simple/
        pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/ 

- download video data or read [README-VideoData.md](./OpenCVMultiTracker/VideoData/README-VideoData.md) file.

        Baidu Netdisk link: https://pan.baidu.com/s/16cZNYcIog6wy8X1hJ5_PMQ
        
        Code: mgv7



###  Project Introduce

We want to draw some rectangle of object, then tracking these.


### Program introduce

Main program: [MultiTracker.py](OpenCVMultiTracker/MultiTracker.py)

Video source: [VideoData](./OpenCVMultiTracker/VideoData)

- PS: run main program, then press word 'a', and select roi area of the frame, 
then you must press 'space' key, now you will find the amazing tracker of the object.


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


