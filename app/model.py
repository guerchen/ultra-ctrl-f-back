from sklearn.cluster import DBSCAN
import pandas as pd
from typing import List
from app.preprocessing import _face_detect, _featurize_face

def _cluster(dataset:pd.DataFrame) -> object:
    """Returns clustered object already fitted with dataset."""

    return DBSCAN(min_samples=2).fit_predict(dataset)

def _preprocess_reference(image:str) -> pd.DataFrame:
    """Converts image url into clusterable dictionary."""
    reference_face = _face_detect(image,reference_image=True)

    if len(reference_face) != 1:
        raise Exception('Incorrect number of faces in reference image')
    
    return pd.DataFrame.from_dict([_featurize_face(reference_face[0])])

def find_similar(reference_image:str, dataset:pd.DataFrame) -> List[int]:
    """Finds most similar faces within dataset of faces. Returns index of similar images."""
    preprocessed_reference = _preprocess_reference(reference_image)

    dataset = pd.concat([dataset,preprocessed_reference], ignore_index=True)
    dataset['cluster'] = _cluster(dataset)
    interest_cluster = dataset['cluster'].tail(1).item()
    dataset = dataset.iloc[:-1]

    return dataset[dataset.cluster == interest_cluster].index
    

