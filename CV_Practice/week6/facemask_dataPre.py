import os
from xml.dom import minidom
import random


if __name__ == '__main__':
    path = 'J:/HouChang/PublicMaskDetect/week5/PyTorch-YOLOv3/data/facemask/Annotations'
    train_rate = 0.9
    list_files = os.listdir(path)
    nlen = len(list_files)
    print(len(list_files))

    label_path = path.replace('Annotations','labels')
    images_path = path.replace('Annotations','JPEGImages')
    val_index = random.sample(range(0,nlen),int((1-train_rate)*nlen))
    train_txt = path.replace('Annotations','train.txt')
    val_txt = path.replace('Annotations', 'val.txt')
    ftrain = open(train_txt, 'w')
    fval = open(val_txt, 'w')
    for i in range(0,len(list_files)):
        print(i)
        temp_path = list_files[i]
        if (i in val_index):
            fval.write(os.path.join(images_path,temp_path.replace('xml','jpg')))
            fval.write('\n')
            fval.flush()
        else:
            ftrain.write(os.path.join(images_path, temp_path.replace('xml', 'jpg')))
            ftrain.write('\n')
            ftrain.flush()

        xml_path = os.path.join(path,temp_path)
        xml_data = minidom.parse(xml_path)
        roots = xml_data.documentElement
        root = xml_data.getElementsByTagName('width')[0]
        w = int(root.childNodes[0].data)
        root = xml_data.getElementsByTagName('height')[0]
        h = int(root.childNodes[0].data)
        root = xml_data.getElementsByTagName('depth')[0]
        c = int(root.childNodes[0].data)

        objects = xml_data.getElementsByTagName("object")

        annotations_txt = os.path.join(label_path,temp_path.replace('xml','txt'))
        fanno = open(annotations_txt, 'w')
        for object in objects:
            root = object.getElementsByTagName('name')[0]
            target = root.childNodes[0].data
            if target =='face':
                nGT = 0
            elif target =='face_mask':
                nGT = 1
            # else:
            #     nGT = 0

            root = object.getElementsByTagName('xmin')[0]
            x1 = int(root.childNodes[0].data)
            root = object.getElementsByTagName('ymin')[0]
            y1 = int(root.childNodes[0].data)
            root = object.getElementsByTagName('xmax')[0]
            x2 = int(root.childNodes[0].data)
            root = object.getElementsByTagName('ymax')[0]
            y2 = int(root.childNodes[0].data)

            #print((x2+x1)/2/w)
            fanno.write("%d %f %f %f %f\n" % (nGT, (int(x2)+int(x1))/2/w, (int(y1)+int(y2))/2/h, (int(x2)-int(x1))/w, (int(y2)-int(y1))/h))
            fanno.flush()
        fanno.close()



