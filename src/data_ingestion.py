import os
import pandas as pd
from google.cloud import storage
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self,config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_names = self.config["bucket_file_names"]

        os.makedirs(RAW_DIR,exist_ok=True)

        logger.info("Data Ingestion Started....")

    def download_csv_from_gcp(self):
        try:

            client  = storage.Client()
            bucket = client.bucket(self.bucket_name)

            for file_name in self.file_names:
                file_path = os.path.join(RAW_DIR,file_name)

                blob = bucket.blob(file_name)
                blob.download_to_filename(file_path)

                logger.info("Downloading Smaller Files ie anime and anime_with synopsis")
        
        except Exception as e:
            logger.error("Error while downloading data from GCP")
            raise CustomException("Failed to download data",e)
        
    def run(self):
        try:
            logger.info("Starting Data Ingestion Process....")
            self.download_csv_from_gcp()
            logger.info("Data Ingestion Completed...")
        except CustomException as ce:
            logger.error(f"CustomException : {str(ce)}")
        finally:
            logger.info("Data Ingestion DONE...")


if __name__=="__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()