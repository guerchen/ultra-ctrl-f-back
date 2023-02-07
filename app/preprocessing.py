from mtcnn import MTCNN
import cv2
import numpy as np
import pandas as pd
from typing import List

detector = MTCNN()

def _face_detect(url:str) -> List[dict]:
    """Uses a MTCNN implementation to extract facial landmarks from a picture."""
    img = cv2.cvtColor(cv2.imread(url), cv2.COLOR_BGR2RGB)
    return detector.detect_faces(img)

def _featurize_face(face_dict:dict) -> dict:
    """Converts face landmarks into features through feature engineering."""
    features = {}
    features['face_ratio'] = face_dict['box'][3]/face_dict['box'][2]
    features['eyes_dist'] = np.sqrt((face_dict['keypoints']['right_eye'][1] - face_dict['keypoints']['left_eye'][1])**2 + (face_dict['keypoints']['right_eye'][0] - face_dict['keypoints']['left_eye'][0])**2)/face_dict['box'][2]
    features['mouth_size'] = np.sqrt((face_dict['keypoints']['mouth_right'][1] - face_dict['keypoints']['mouth_left'][1])**2 + (face_dict['keypoints']['mouth_right'][0] - face_dict['keypoints']['mouth_left'][0])**2)/face_dict['box'][2]
    x_mouth = (face_dict['keypoints']['mouth_right'][1] + face_dict['keypoints']['mouth_left'][1])/2
    y_mouth = (face_dict['keypoints']['mouth_right'][0] + face_dict['keypoints']['mouth_left'][0])/2
    features['mouth_to_nose'] = np.sqrt((face_dict['keypoints']['nose'][1] - y_mouth)**2 + (face_dict['keypoints']['nose'][0] - x_mouth)**2)/face_dict['box'][3]
    x_eyes = (face_dict['keypoints']['right_eye'][1] + face_dict['keypoints']['left_eye'][1])/2
    y_eyes = (face_dict['keypoints']['right_eye'][0] + face_dict['keypoints']['left_eye'][0])/2
    features['mouth_to_eyes'] = np.sqrt((y_eyes - y_mouth)**2 + (x_eyes - x_mouth)**2)/face_dict['box'][3]
    return features

def preprocess(image_url_list:list) -> pd.DataFrame:
    """Using site images, creates pandas dataframe that will be used to cluster faces."""
    dataset = []
    for image_url in image_url_list:
        faces = _face_detect(image_url)
        for face in faces:
            dataset.append(_featurize_face(face))
    return pd.DataFrame.from_dict(dataset)

print(preprocess(["D:\All\Fotos\WhatsApp Image 2021-03-07 at 13.23.42.jpeg"]))