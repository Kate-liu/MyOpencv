# Face Shape Predictor

This is Face Shape Predictor test project.


## Install package

- pip install opencv-python==3.4.10.35
    
- pip install opencv-contrib-python==3.4.10.35

- ps：install version need equality.


## Project Introduce

### Facial point annotations

- [Facial point annotations](https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/)

- [Dlib of the predictor](http://dlib.net/files/)

- The 68 points mark-up used for our annotations

![](./Data/figure_68_markup.jpg)



#### Introduce

- Main program: [FacialPointAnnotations.py](./FacialPointAnnotations/FacialPointAnnotations.py)

PS: Shape predictor: Need Download in the Baidu Netdisk: 
link: [shape_predictor_68_face_landmarks.dat](https://pan.baidu.com/s/1IMVeL9iG0RCTS8i3oneRrw).
Code: dr42

then, put it to the Data directory.




### Fatigue Monitoring

#### Introduce

- Main program: [FatigueMonitoring.py](./FatigueMonitoring/FatigueMonitoring.py)

- Paper: [Real-Time Eye Blink Detection using Facial Landmarks.pdf](./Paper/2016-Real-Time Eye Blink Detection using Facial Landmarks.pdf)
- link: [Real-Time Eye Blink Detection using Facial Landmarks.pdf](http://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf)


PS: Test vide: Need Download in the Baidu Netdisk: 
link:[test.mp4](https://pan.baidu.com/s/1IMVeL9iG0RCTS8i3oneRrw).
Code: dr42

then, put it to the Data directory.


## Content tree

    .
    │  README.md
    │
    ├─Data
    │      figure_68_markup.jpg
    │      liudehua.jpg
    │      liudehua2.jpg
    │      shape_predictor_68_face_landmarks.dat
    │      test.mp4
    │
    ├─FacialPointAnnotations
    │      FacialPointAnnotations.py
    │
    ├─FatigueMonitoring
    │      FatigueMonitoring.py
    │
    └─Paper
            2016-Real-Time Eye Blink Detection using Facial Landmarks.pdf


