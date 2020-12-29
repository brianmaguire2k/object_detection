import os
import glob

from lxml import etree
import tensorflow as tf
from utils.dataset_util import recursive_parse_xml_to_dict
from dataset_tools.create_pascal_tf_record import dict_to_tf_example

# get list of annotation files from data directory
data_dir = '/home/tensorflow/work/data'
annotation_files = glob.glob(os.path.join(data_dir, 'Annotations/*.xml'))

# define number of training/evaluation samples
trainval_split = 0.9 # use 90% for training
n_train = round(trainval_split*len(annotation_files))

# create label map dict
label_map_dict = {'background': 0, 'truck': 1}

# create training and evaluation TFRecord Writers
f_train_path = os.path.join(data_dir, 'train.record')
f_val_path = os.path.join(data_dir, 'eval.record')

with tf.io.TFRecordWriter(f_train_path) as f_train, tf.io.TFRecordWriter(f_val_path) as f_val:
    # iterate over annotations and write images/metadata to TFRecord
    for idx, ann in enumerate(annotation_files):
        # sanity check since this might take a while
        if idx % 100 == 0:
            print(f'Writing image {idx} of {len(annotation_files)}...')

        # load xml file via etree, get root, parse to dict with TF helper function
        tree = etree.parse(ann)
        data = recursive_parse_xml_to_dict(tree.getroot())['annotation']

        # modify folder value to absolute path since EVA defaulted to 'UAV_sample'
        data['folder'] = '/home/tensorflow/work/data'

        # add defaults to VOC fields tensorflow is expecting (that EVA didn't include)
        # eventually modify TF input to just ignore these
        for obj in data['object']:
            obj['difficult'] = 0
            obj['truncated'] = 0
            obj['occluded'] = 0
            obj['pose'] = 'Unspecified'

        # convert to TFExample, write to training or evaluation file depending on index
        data_example = dict_to_tf_example(data, data_dir, label_map_dict, True)

        if idx < n_train:
            f_train.write(data_example.SerializeToString())
        else:
            f_val.write(data_example.SerializeToString())