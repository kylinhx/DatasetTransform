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
  
  使用说明：

1. 首先将需要转化为YOLO格式的标注文件以及对应的图片文件放在同一个文件夹中，例如“Annotations”和“JPEGImages”。
2. 修改代码中“Annotations_Path”和“Image_Path”为对应文件夹的路径。
3. 可以在“Classes”中定义物体的类别，根据实际情况修改。
4. 根据需要调整“train_percent”和“test_percent”来设置训练集和测试集的比例。
5. 运行代码，将会生成三个文件夹：train，test，val。其中train文件夹包含用于训练的图片，test文件夹包含用于测试的图片，val文件夹包含用于验证的图片。
6. 每张图片会对应一个txt标注文件，文件格式为每行为一个物体的标注，由五个数字组成：第一个数字是物体类别的序号，后四个数字是物体在图片中的位置信息，分别为中心坐标x、中心坐标y、宽度和高度。
7. 如果需要查看数据分割的结果，可以在“train.txt”，“test.txt”，“val.txt”中查看对应的图片文件名。

注意事项：

1. 请务必备份原始数据，以免误操作造成数据丢失。
2. 需要安装minidom模块，如果未安装请先安装该模块。
3. 需要确保所有的标注文件的格式符合VOC数据集格式，即文件格式为.xml，文件中包含了对应图片的标注信息。
