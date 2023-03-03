# This py program is used to get xml labels into boxes
# For each box in boxes
# boxes =[box]
# box = {
#   filename: str       the filename of picture
#   size:[width,height,depth]   the size of picture
#   bboxes: [[imgcls,xmin,ymin,xmax,ymax]]       the location of object
# }
# boxes=[
#   {
#       filename:str
#       bboxes:[[imgcls,xmin,ymin,xmax,ymax]]
# }
#   {
#       filename:str
#       bboxes:[[imgcls,xmin,ymin,xmax,ymax]]
# }
# ...
# ]
from xml.dom.minidom import parse
import os
import random
import shutil

# Define the path
Annotations_Path = 'Annotations'
Image_Path = 'JPEGImages'

Train_Path_img = 'images/train'
Val_Path_img = 'images/val'
Test_Path_img = 'images/test'

Train_Path_label = 'labels/train'
Val_Path_label = 'labels/val'
Test_Path_label = 'labels/test'

# Define classes
Classes = ['Platelets', 'RBC', 'WBC']


# This function can read single xml label document and add a single box into boxes
def readXML(XMLPATH, boxes):
    box = {}
    bboxes = []
    bbox = []
    dom = parse(XMLPATH)
    rootNode = dom.documentElement

    # Get filename
    filename = rootNode.getElementsByTagName('filename')[0].firstChild.data
    print(filename)
    box['filename'] = filename

    # Get size of the picture
    sizes = rootNode.getElementsByTagName('size')
    for size in sizes:
        width = size.getElementsByTagName('width')[0].firstChild.data
        height = size.getElementsByTagName('height')[0].firstChild.data
        depth = size.getElementsByTagName('depth')[0].firstChild.data
    box['size'] = [width, height, depth]

    # Get imgcls and box
    locations = rootNode.getElementsByTagName('object')
    for location in locations:
        # Get imgcls
        imgcls = location.getElementsByTagName('name')[0].firstChild.data
        # Get box
        xmin = location.getElementsByTagName('xmin')[0].firstChild.data
        ymin = location.getElementsByTagName('ymin')[0].firstChild.data
        xmax = location.getElementsByTagName('xmax')[0].firstChild.data
        ymax = location.getElementsByTagName('ymax')[0].firstChild.data

        # Save bbox in bboxes
        bbox = [imgcls, int(xmin), int(ymin), int(xmax), int(ymax)]
        bboxes.append(bbox)
    # Save bboxes
    box['bboxes'] = bboxes

    # Get a box in boxes
    boxes.append(box)


# This function can get all filenames in the path
def getPath(Annotations_Path):
    XMLNAMES = os.listdir(Annotations_Path)
    return XMLNAMES


# This function can get all box contained in boxes
def getBoxes():
    boxes = []
    # Get all xml names
    Xml_Names = getPath(Annotations_Path)

    # Read all xml
    for xmlname in Xml_Names:
        xmlpath = Annotations_Path + '/' + xmlname
        readXML(xmlpath, boxes)

    return boxes


# This function is used to generate txt document
def gen_txt(box, path):
    save_path = path + '/' + box['filename'].split('.')[0] + '.txt'
    size = box['size']
    with open(save_path, 'w', encoding='utf-8') as f:
        for bbox in box['bboxes']:
            bbox = turn_to_Yolo(size, bbox)
            bbox[0] = Classes.index(bbox[0])
            f.write(
                str(bbox[0]) + ' ' + str(bbox[1]) + ' ' + str(bbox[2]) + ' ' + str(bbox[3]) + ' ' + str(bbox[4]) + '\n')
    f.close


# This function is used to generate img document
def gen_img(filename, path_old, path_new):
    oldpath = path_old + '/' + filename
    newpath = path_new + '/' + filename

    shutil.copy(oldpath, newpath)


# This function is used to turn VOC to Yolo
# Yolo_datasets is (x_center, y_center, w, h)
def turn_to_Yolo(size, bbox):
    cls = bbox[0]

    # Get number
    dw = 1./int(size[0])
    dh = 1./int(size[1])

    xmin = int(bbox[1])
    ymin = int(bbox[2])
    xmax = int(bbox[3])
    ymax = int(bbox[4])

    # Calculate
    dx_center = (xmin + xmax) / 2.0
    dy_center = (ymin + ymax) / 2.0
    x_center = dx_center * dw
    y_center = dy_center * dh

    w = xmax - xmin
    h = ymax - ymin
    w = w * dw
    h = h * dh

    return [cls, x_center, y_center, w, h]


def gen_index(filename, num):
    clas = ['train.txt', 'test.txt', 'val.txt']
    path = clas[num]
    with open(path, 'a', encoding='utf-8') as f:
        f.write(filename + '\n')
    f.close


# This function is used to decide which part of your dataset is used in train or val or test
def div_dataset(boxes):
    for box in boxes:
        filename = box['filename']
        randNum = random.randint(1, 10)
        if randNum == 1:
            gen_txt(box, Val_Path_label)
            gen_img(filename, Image_Path, Val_Path_img)
            gen_index(filename, 2)
        elif randNum > 8:
            gen_txt(box, Test_Path_label)
            gen_img(filename, Image_Path, Test_Path_img)
            gen_index(filename, 1)
        else:
            gen_txt(box, Train_Path_label)
            gen_img(filename, Image_Path, Train_Path_img)
            gen_index(filename, 0)

def detect_path():
    path_list = ['images/train', 'images/val', 'images/test',
                 'labels/train', 'labels/val', 'labels/test',
                 'test.txt', 'train.txt', 'val.txt']
    for path in path_list:
        if os.path.exists(path):
            # path exists
            print(os.listdir(path))
            items = os.listdir(path)
            for item in items:
                os.remove(path+'/'+item)
                print(path + '/' + item + ' has been removed')
        else:
            # path do not exist
            print("path not found, creating path: " + path)
            if path in ['test.txt', 'train.txt', 'val.txt']:
                file = open(path, 'w', encoding='utf-8')
                file.close()
            else:
                os.makedirs(path)
if __name__ == '__main__':
    detect_path()
    boxes = getBoxes()
    div_dataset(boxes)