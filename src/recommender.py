from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from config.config import OPENAI_API_KEY
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self,retriever,api_key:str,model_name:str):
        self.llm = ChatOpenAI(model="gpt-4o-mini",api_key=OPENAI_API_KEY, temperature=0.7,verbose= True)



        self.prompt = get_anime_prompt()

        self.qa_chain = RetrievalQA.from_chain_type(
            llm = self.llm,
            #it will pull the relevant documents from the vector store
            chain_type = "stuff",
            retriever = retriever,
            return_source_documents = True,
            chain_type_kwargs = {"prompt":self.prompt}
        )

    def get_recommendation(self,query:str):
        result = self.qa_chain({"query":query})
        return result['result']