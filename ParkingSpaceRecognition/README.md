# Parking Space Recognition

This is Parking Space Recognition test project.


## Install package

- pip install keras==2.3.1

- pip install tensorflow==1.15.3

- pip install opencv-python==3.4.10.35
    
- pip install opencv-contrib-python==3.4.10.35

- ps：install version need equality.



## Project Introduce

We need use Canny, findContours, Perspective Transform to preproccess,

then use tesseract OCR tools, get result text.



## Implementation approach

### Program introduce

Main program: [DocumentOCR.py](DocumentOCR.py)

Document source: [DocumentData](./DocumentData)

OCR data source: [OCRData](./OCRData)

OCR result source: [OCRResult](./OCRResult)



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

