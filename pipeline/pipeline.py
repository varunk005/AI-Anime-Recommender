from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import OPENAI_API_KEY
from utils.logger import get_logger
from utils.custom_exception import CustomException

#INITIALIZING LOGGER
logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self,persist_dir="chroma_db"):
        try:
            logger.info("Intializing Recommdation Pipeline")
            #loading the vector store from the persist directory thsts why given empty path
            vector_builder = VectorStoreBuilder(csv_path="" , persist_dir=persist_dir)
            
            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever,OPENAI_API_KEY,"gpt-4o-mini")
            

            logger.info("Pipeline intialized sucesfully...")

        except Exception as e:
            logger.error(f"Failed to intialize pipeline {str(e)}")
            raise CustomException("Error during pipeline intialization" , e)
        
    def recommend(self,query:str) -> str:
        try:
            logger.info(f"Received a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated successfully...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation" , e)
        


        