from sklearn.cluster import DBSCAN
import pandas as pd
import numpy as np
from typing import List
from app.preprocessing import _face_detect, _featurize_face

def _preprocess_reference(image:str) -> pd.DataFrame:
    """Converts image url into clusterable dictionary."""
    reference_face = _face_detect(image,reference_image=True)

    if len(reference_face) != 1:
        raise Exception('Incorrect number of faces in reference image')
    
    return pd.DataFrame.from_dict([_featurize_face(reference_face[0])])

def find_similar(reference_image:str, dataset:pd.DataFrame) -> List[int]:
    """Finds most similar faces within dataset of faces. Returns index of similar images."""
    preprocessed_reference = np.array(_preprocess_reference(reference_image))
    dataset_matrix = np.array(dataset)

    similarity_vector = np.inner(preprocessed_reference,dataset_matrix)
    dataset['similarity'] = similarity_vector[0]
    index = dataset.sort_values(by=['similarity'],ascending=False).index[:5]
    return index
    