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
then you must press 'space' or 'enter' key, now you will find the amazing tracker of the object.





## Mobile Net SSD Model MultiTracker

### Install package and download

- pip install opencv-python==4.3.0.38
    
- pip install opencv-contrib-python==4.3.0.38

- pip install dlib

- About dlib knowledge link:
    - How to install Dlib for Python 3 on Windows: https://pysource.com/2019/03/20/how-to-install-dlib-for-python-3-on-windows/

    - How to install dlib v19.9 or newer (w/ python bindings) from github on macOS and Ubuntu: https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf

    - Links for dlib: https://pypi.org/simple/dlib/

- download video data or read [README-VideoData.md](./MobileNetSSDMultiTracker/VideoData/README-VideoData.md) file.

        Baidu Netdisk link: https://pan.baidu.com/s/11hJbSslRSYAJDBTtKF21HQ
        
        Code: jn5g

- download Mobile Net SSD Model or read [README-VideoData.md](./MobileNetSSDMultiTracker/MobileNetSSDModel/README-MobileNetSSDModel.md) file.

        Baidu Netdisk link: https://pan.baidu.com/s/1qtbH8ZhBBmFHDFCCGVfL-A
        
        Code: 2qzc



        
###  Project Introduce

We want to draw some rectangle of object, then tracking these.



### Program introduce

Main program: [NetMultiTracker.py](MobileNetSSDMultiTracker/NetMultiTracker.py)

Main program-multiprocessing: [NetMultiTrackerMultiprocessing](MobileNetSSDMultiTracker/NetMultiTrackerMultiprocessing.py)

Utils program: [Utils.py](MobileNetSSDMultiTracker/Utils.py)

Video Data: [VideoData](MobileNetSSDMultiTracker/VideoData)

Mobile Net SSD Model: [MobileNetSSDModel](MobileNetSSDMultiTracker/MobileNetSSDModel)



## Content tree
    
        
    ├─ README.md
    │
    ├─MobileNetSSDMultiTracker
    │  │  NetMultiTracker.py
    │  │  NetMultiTrackerMultiprocessing.py
    │  │  Utils.py
    │  │
    │  ├─MobileNetSSDModel
    │  │      MobileNetSSD_deploy.caffemodel
    │  │      MobileNetSSD_deploy.prototxt
    │  │      README-MobileNetSSDModel.md
    │  │
    │  └─VideoData
    │         race.mp4
    │         race_output_fast.avi
    │         race_output_slow.avi
    │         README-VideoData.md
    │ 
    └─OpenCVMultiTracker
        │  MultiTracker.py
        │
        └─VideoData
                los_angeles.mp4
                nascar.mp4
                soccer_01.mp4
                soccer_02.mp4
                README-VideoData.md


