# COVID-19 Prediction Model From Audio Data
-------------------------
Project Description
-----------------------
DSCI 400 COVID-19 Audio Project
This process is to create a predictive model for COVID-19 from a set of audio files.
Broadly, the steps are  data cleaning, generating and normalizing Mel-spectrograms and handcrafted features, testing and training a model composed of a CNN and a Perceptron, and validation of the results.

-------------------------------------------------------
Instructions
-------------------------------------------------------
1) Download the CovidNet_Final.ipynb notebook
2) Open this notebook in Google Colab
3) Create a shortcut to the 'DSCI 400' Google Drive folder (https://bit.ly/3nUvQyM) in your main Google Drive. The path should be '/content/gdrive/MyDrive/DSCI400'
5) Run the COVIDNet notebook. All other required APIs are included in the 'DSCI 400' folder provided in the link.

It is important to note that the only file needed to use COVIDNet is the CovidNet_Final.ipynb notebook. All the other files included in this repository are simply for ease of viewing, as they are a replica of the folder system in Google Drive. In the interest of saving memory, any interested user need not download the entire repository; they only need to download the CovidNet_Final.ipynb notebook.

Dependencies
-------------------------------------------------------
The Libraries required for this program are:

INTERNAL TO PYTHON VERSION 3.9.2
- os
- sys
- subprocess
- glob

EXTERNAL TO PYTHON VERSION 3.9.2
- google-colab 1.0.0 (2021)
- google 0.1.1 (2021)
- librosa version 0.8.0 (2021)
- pandas version 1.2.3 (2021)
- numpy version 1.20.0 (2021)
- surfboard 0.2.0 (2021)

Dataset
------------------------------------------------------
The dataset used for this project is under "Coswara Original Files". The files can also be sourced at "https://github.com/iiscleap/Coswara-Data".

