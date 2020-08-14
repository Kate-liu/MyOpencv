# Convolutional Neural Network (CNN)

This is Convolutional Neural Network test.


## Install package

- pip install opencv-python==4.3.0.38
    
- pip install opencv-contrib-python==4.3.0.38

- pip install scikit-image

- ps：install opencv version need equality.



## Introduce of Convolution

- link: [Convolutional neural network](https://en.wikipedia.org/wiki/Convolutional_neural_network)

- link: [A Comprehensive Guide to Convolutional Neural Networks — the ELI5 way](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)

- link: [Convolution arithmetic](https://github.com/vdumoulin/conv_arithmetic)


- Architecture:

![](./ReadmeData/A%20CNN%20sequence%20to%20classify%20handwritten%20digits.jpeg)


- Input Image:

![](./ReadmeData/4x4x3%20RGB%20Image.png)

- Convolution Layer — The Kernel:

        Kernel/Filter, K = 
        1  0  1
        0  1  0
        1  0  1

![](./ReadmeData/Convoluting%20a%205x5x1%20image%20with%20a%203x3x1%20kernel%20to%20get%20a%203x3x1%20convolved%20feature.gif)

- Movement of the Kernel

![](./ReadmeData/Movement%20of%20the%20Kernel.png)


- Convolution operation on a MxNx3 image matrix with a 3x3x3 Kernel:

![](./ReadmeData/Convolution%20operation%20on%20a%20MxNx3%20image%20matrix%20with%20a%203x3x3%20Kernel.gif)


- Stride Length:

![](./ReadmeData/Convolution%20Operation%20with%20Stride%20Length%20=%202.gif)


- padding:

![](./ReadmeData/SAME%20padding%205x5x1%20image%20is%20padded%20with%200s%20to%20create%20a%206x6x1%20image.gif)






## Implementation approach

### Program introduce

Main program: [ConvolutionalNeuralNetwork.py](ConvolutionalNeuralNetwork.py)

Data source: [Data](Data)




### Content tree
    
    
    .
    │      ConvolutionalNeuralNetwork.py
    │      README.md
    │
    └─Data
            lanpangzi.jpg





