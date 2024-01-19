# DeePhafier: A Phage Lifestyle Classifier using a Multilayer self-attention neural network combining protein information
Version 1.1 <br>
Authors: Yan Miao, Zhenyuan Sun, Chen Lin, et.al. <br>
Maintainer: Yan Miao miaoyan17@mails.jlu.edu.cn 

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
    Before testing, users' own query contigs should be preprocessed to an available format using `preprocessing.py` and be condon embedded by `embedding.py` as Seq2Vec(https://github.com/crazyinter/Seq2Vec). The embedding matrix is the same as Virtifier from https://github.com/crazyinter/Seq2Vec/blob/master/supplementary_files/embedding_matrix.csv. The query sequences < 9000bp in the test file should be zero-padded to 9000bp. The query sequences > 9000bp in the test file should be cut-off to 9000bp.

To make a prediction by "test.py", users' own query contigs should be edited into a ".csv" file. Then run "test.py" or copy the code into jupyter notebook and run seperately.


# Citation
The manuscript is under review.
