# DatasetTransform
  This repository contains some python scripts that is used to change the format of a dataset. This repository will be updated continuously.

### VOC_to_YOLO.py
  
  This Python code is used to convert XML labels generated by the popular annotation tool called LabelImg into text files in YOLO format. The YOLO format is a common way of representing object detection datasets, where each row in the text file represents an object in an image, along with its class label and bounding box coordinates. The code reads the XML files that LabelImg generates and extracts information about the images and their bounding boxes, converts the bounding boxes into YOLO format, and writes the results into text files. Additionally, it copies the images into separate directories for training, validation, and testing sets, and generates index files that list the file names for each set. The code also allows for specifying the percentage of the dataset to be allocated to the training, validation, and testing sets.
  
  I'll explain how the script is used. 
  
  First you need to create two folders in the working directory, one is Annotations and the other is JPEGImages. Annotataions contains all the tag information in VOC format, it is an xml file, JPEGImages contains all images, note that the name of your tag file and the image file should be same.
  
  Then you should put the script in your working directory, just run and you will get two new floders which can be used in yolo5 or yolo8 training.
  
  
  
  这是一个将XML标签转换为边框框的Python程序，用于机器学习中物体检测的数据集制作。

  该程序主要实现以下功能：

  1.从XML标签中读取单个标签文件，并将单个边框添加到“boxes”列表中；
  
  2.获取指定路径中的所有XML文件名，读取所有XML文件，并将所有边框添加到“boxes”列表中；
  
  3.将“boxes”列表中的边框转换为YOLO格式，并生成txt文件；
  
  4.按照一定的比例将数据集分为训练集、测试集和验证集，并将它们保存到不同的路径中；

  5.根据所得到的训练集、测试集和验证集的文件名生成索引文件train.txt、test.txt和val.txt，便于后续训练模型。

  该程序使用了以下库：

  1.os：与操作系统交互；
  
  2.xml.dom.minidom：用于解析XML文件；
  
  3.random：生成随机数；
  
  4.shutil：高级文件操作工具。
