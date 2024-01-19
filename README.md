# DeePhafier: A Phage Lifestyle Classifier using a Multilayer self-attention neural network combining protein information
Version 1.1 <br>
Authors: Yan Miao, Zhenyuan Sun, Chen Lin, Haoran Gu, Chenjing Ma, Chunxue Yang, and Guohua Wang <br>
Maintainer: Yan Miao miaoyan@nefu.edu.cn 

# Description
Bacteriophages is known as viruses that infect bacterial cells. They are the most entities on earth and play important roles in microbiome. According to the phage lifestyle, phages can be divided into the virulent phages and the temperate phages. Classifying virulent and temperate phages is crucial for further understanding of phage-host interactions. Although there are several methods designed for phage lifestyle classification, they either consider sequence features or gene features merely, leading to low accuracy. A new computational method, DeePhafier, is proposed to improve classification performance on phage lifestyle. Built by several multilayer self-attention neural network, a global self-attention neural network and being combined by protein features of PSSM matrix, DeePhafier improves the classification accuracy and outperforms two benchmark methods. 

# Dependencies
To utilize DeePhafier, numpy, h5py, TensorFlow, Keras are needed to be previously installed. Some other packages are also needed to make sure the code running correctly such as "os", "ast", etc.

In convenience, you can download Anaconda from https://repo.anaconda.com/archive/, where contains most of needed packages. If there are still some special packages that are missed when running, you can use "pip install" to install the specific packages. 

To install tensorflow, start "cmd.exe" and enter <br>
```
pip install tensorflow
```
To insatll Keras, start "cmd.exe" and enter <br>
```
pip install Keras
```
To insatll h5py, start "cmd.exe" and enter <br>
```
pip install h5py
```
Our codes are all edited by Python 3.6.7 with TensorFlow 1.4.0 and Keras 2.1.3.

# Usage
It is simple to use DeePhafier for users' database. <br>
You can clone DeePhafier package by <br>
```
git clone https://github.com/ceazyinter/DeePhafier.git
```
and change your directory to DeePhafier. 
Then execute the command:
```
./DeePhafier <input_file_folder>/input_file.fna <output_file_folder>/output_file.csv
```


# Citation
The manuscript is under review.
