# DatasetTransform
  This repository contains some python scripts that is used to change the format of a dataset. This repository will be updated continuously.

### VOC_to_YOLO.py
  I'll explain how the script is used. 
  
  First you need to create two folders in the working directory, one is Annotations and the other is JPEGImages. Annotataions contains all the tag information in VOC format, it is an xml file, JPEGImages contains all images, note that the name of your tag file and the image file should be same.
  
  Then you should put the script in your working directory, just run and you will get two new floders which can be used in yolo5 or yolo8 training.
