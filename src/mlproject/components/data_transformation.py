from mlproject.config.configuration import DataTransformConfig
from sklearn.model_selection import train_test_split
from mlproject import logger
import pandas as pd
import os

class DataTransformation:

    #Note: You can add different data ransformation techniques such as Scalar, PCA, and all 
    # You can perform all kinds of EDA in ML cycle here before passing this data to the model
    def __init__(self, config: DataTransformConfig) -> None:
        self.config = config

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index = False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'), index = False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)