from msilib.schema import Error
from sklearn.cluster import DBSCAN
import pandas as pd
from typing import List
from app.preprocessing import _face_detect, _featurize_face

def _cluster(dataset:pd.DataFrame) -> object:
    """Returns clustered object already fitted with dataset."""
    return DBSCAN(min_samples=2).fit(dataset)

def _preprocess_reference(image:str) -> pd.DataFrame:
    """Converts image url into clusterable dictionary."""
    reference_face = _face_detect(image)
    if len(reference_face) != 1:
        raise Exception('Incorrect number of faces in reference image')
    return pd.DataFrame.from_dict(_featurize_face(reference_face[0]))

def find_similar(reference_image:str, dataset:pd.DataFrame) -> List[int]:
    """Finds most similar faces within dataset of faces."""
    cluster_object = _cluster(dataset)
    dataset['cluster'] = cluster_object.labels_
    interest_cluster = cluster_object.predict(_preprocess_reference(reference_image))
    return dataset[dataset.cluster == interest_cluster].index
    

