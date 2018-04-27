import os
import glob
import xml.etree.ElementTree as ET
import argparse

'''
this module used to convert pascal xml annotations to label map tensorflow.
for example :
    python generate_labelmap_from_xml_pascal.py -p /home/nodeflux/tensorflow_detector/dsw/data/tf_wider_train/annotations/xmls -l wider_label_map.pbtxt

'''

def __get_data_name_from_pascal_xml(path):
    list_name = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            list_name.append( member[0].text)

    return list_name

def convert(xml_path, pbtxt_path):

    list_name = __get_data_name_from_pascal_xml(xml_path)
    unique_name= list(set(list_name))


    with open(pbtxt_path, 'w+') as f_out:
        proto_string = "\nitem{{\n\tid: {}\n\tname: '{}' \n }}\n"
        for i, c in enumerate(unique_name):
            f_out.write(proto_string.format(i + 1, c))

    print(list(set(list_name)))

    print('> label map  -  Successfully saved in', pbtxt_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Converts a training dataset from pascal format to tfrecord to be used with tensorflow object detectors")
    parser.add_argument('-p', '--xmlpascal', help="path to the training/test list file used by pascal annotations", required=True)
    parser.add_argument('-l', '--labelMap', help="where the label map file will be saved, label_map.pbtxt for default",
                        default='label_map.pbtxt')
    args = parser.parse_args()


    convert( args.xmlpascal, args.labelMap)
