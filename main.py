from matplotlib.pyplot import imshow
from object_detection.utils import visualization_utils as vis_util
from object_detection.utils import label_map_util
from tensorflow.keras.models import load_model
import sys
import glob as glob
import tensorflow as tf
import os
import numpy as np
from collections import namedtuple
from PIL import Image
import altair as alt
import math
import pandas as pd
import streamlit as st
import subprocess
import warnings
warnings.filterwarnings('ignore')

MODEL_NAME = 'faster_rcnn_resnet50'

sys.path.append('PATH_TO_TENSORFLOW_OBJECT_DETECTION_FOLDER')

MODEL_PATH = os.path.join('model', MODEL_NAME)
PATH_TO_CKPT = os.path.join(
    MODEL_PATH, 'inference_graph/frozen_inference_graph.pb')


PATH_TO_LABELS = os.path.join('scripts', 'gtsdb3_label_map.pbtxt')

NUM_CLASSES = 3

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')


def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)


label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(
    label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)
print(label_map)

st.set_page_config(layout="centered",
                   page_title="Car Improvement Center", page_icon=":car:")

"""
# MERNcenaries Megathon Car Improvement Center

### Infotainment system:
"""

with st.echo(code_location='below'):
    my_speed = st.slider("Your current speed", 1, 120, 50)
    uploaded_file = st.file_uploader("Upload Image", type=".jpg")

    if uploaded_file:
        image = Image.open(uploaded_file)

        with detection_graph.as_default():
            with tf.Session(graph=detection_graph) as sess:
                image_np = load_image_into_numpy_array(image)
                image_np_expanded = np.expand_dims(image_np, axis=0)
                image_tensor = detection_graph.get_tensor_by_name(
                    'image_tensor:0')
                boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                scores = detection_graph.get_tensor_by_name(
                    'detection_scores:0')
                classes = detection_graph.get_tensor_by_name(
                    'detection_classes:0')
                num_detections = detection_graph.get_tensor_by_name(
                    'num_detections:0')
                (boxes, scores, classes, num_detections) = sess.run(
                    [boxes, scores, classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})

                count = 0
                for i in range(300):
                    if (scores[0, i] > 0.5):
                        count += 1

                for i in range(count):
                    yl = int(boxes[0, i, 0]*image.height)
                    xl = int(boxes[0, i, 1]*image.width)
                    yr = int(boxes[0, i, 2]*image.height)
                    xr = int(boxes[0, i, 3]*image.width)
                    img = image_np[yl:yr, xl:xr]
                    better = Image.fromarray(img).resize(
                        (30, 30), resample=Image.BOX)
                    better.save(f'test2/image.jpg')

                Detected_image = vis_util.visualize_boxes_and_labels_on_image_array(
                    image_np,
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    category_index,
                    use_normalized_coordinates=True,
                    line_thickness=6)

                st.image(Detected_image)

        try:
            subprocess.check_output(["/bin/python3", "infer.py"])
        except Exception as e:
            speeds = int(str(e).split()[-1][:-1])

        f"""
        ##### Your speed limit is: {speeds}
        ##### Your current speed is: {my_speed}
        """

        if (my_speed > speeds):
            st.error('Please reduce your speed now', icon="⚠️")

    st.stop()
