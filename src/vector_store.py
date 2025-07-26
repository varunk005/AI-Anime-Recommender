from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
#for loading CSV files
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

class VectorStoreBuilder:
    #storing vector store in persist directory
    def __init__(self,csv_path:str,persist_dir:str="chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")
    
    #create a vector store from the CSV file
    def build_and_save_vectorstore(self):
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding='utf-8',
            metadata_columns=[]
        )
        #load the data from the CSV file
        #and store ind data variable
        data = loader.load()

        #splitting the data into chunks
        splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
        #splitted texts
        texts = splitter.split_documents(data)
        
        #creating into embeddings
        db = Chroma.from_documents(texts,self.embedding,persist_directory=self.persist_dir)
        db.persist()
    
    #load the vector store from the persist directory
    #? why passing embedding s again 
    def load_vector_store(self):
        return Chroma(persist_directory=self.persist_dir,embedding_function=self.embedding)



