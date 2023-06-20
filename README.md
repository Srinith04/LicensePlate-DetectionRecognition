


<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->




<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->
<div align="center">
<h1 align="center">LicensePlate Detection and text Recognition</h1>
</div>

   



<!-- ABOUT THE PROJECT -->
## About

This project is a working deep learning model which can detect license plates and recognise the text in them in photos , videos and live feed as well.
<ol>
  <li> The project uses yolov5 architecture , specifically uses yolov5m pretrained model and trains it on the custom training dataset.
  <li> You can find the official repository for yolov5 here (yolov5)[https://github.com/ultralytics/yolov5] from which this project is changed and trained upon.
  <li> To test this model, you will have first clone the repository mentioned above and include the files mentioned below into the cloned repository.
  <li> You can download my custom trained weights for this model from [custom-weights](https://drive.google.com/file/d/1-VNWbHFKWhwuIJGIQeHu48iegcqX4T4Z/view?usp=sharing)
  <li> You can find inference on a test image by the model in this repository (test-image.jpg).
</ol>

## Files to include 
<ol>
  <li> Include the modified detect.py file (detect-modified.py) present in this repo.
  <li> Include the ocr-recognition.py file as well.
  <li> Include the downloaded custom weights mentioned above as well.
</ol>

## Inference
<ol>
  <li> cd into the cloned repository and Execute the following command : 
  <li> python detect-modified.py --source "source image relative path" -- weights "relative path to custom weights " --save-crop
</ol>


## Training
<ol>
  <li> To train your own model you can use look into LicensePlate-train jupyter notebook , which is used to train my model.
  <li> I used a kaggle dataset to train my model , you can find many such datasets on the internet , or you can create your own dataset.
</ol>

## Text Recognition
<ol>
  <li> The  LicensePlate-train jupyter notebook also has code which shows steps to how we are recovering text from the license plate crop using pytesseract.
</ol>
    
<p align="right">(<a href="#readme-top">back to top</a>)</p>






