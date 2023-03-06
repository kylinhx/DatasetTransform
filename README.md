# DatasetTransform
  This repository contains some python scripts that is used to change the format of a dataset. This repository will be updated continuously.

### VOC_to_YOLO.py
  
  This Python program is used to convert object detection annotations in XML format to text files in YOLO format. It takes XML files containing object locations, class names, and image sizes and extracts the relevant information. The output is a set of text files that contain the same information in the YOLO format, which can be used for training object detection models.↳

The program first defines the paths to the input XML files and the output text files for training, validation, and testing. It also defines the classes for the objects being detected, and the percentages of the data to be used for training, validation, and testing.

The main functions of the program are:

- `readXML`: reads a single XML file and extracts the information about the object locations, class names, and image sizes. It saves this information in a dictionary called `box`, and appends this dictionary to a list called `boxes`.
- `getPath`: returns a list of all XML file names in the input path.
- `getBoxes`: calls `readXML` for all XML files in the input path, and returns a list of all `box` dictionaries.
- `gen_txt`: given a `box` dictionary, generates a text file in YOLO format with the same information.
- `gen_img`: given an image filename and the paths to the input and output image directories, copies the image file from the input directory to the output directory.
- `turn_to_Yolo`: converts the object location information from VOC format to YOLO format.
- `gen_index`: given an image filename and a number (0, 1, or 2), appends the filename to the corresponding text file for training, validation, or testing.

Finally, the program divides the dataset into training, validation, and testing sets according to the percentages defined earlier, and generates text files and copies image files for each set using the functions defined above.
  
  
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
