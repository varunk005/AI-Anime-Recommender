import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")

