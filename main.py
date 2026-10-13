from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
pdf=PyPDFLoader("./resume_geetha.pdf")
v=pdf.load()
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
split=text_splitter.split_documents(v)
embeddings=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector_store=Chroma.from_documents(
    documents=split,
    embedding=embeddings
)
query="what are the technical skills"
llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash")
def vamsi(query:str):
    result=vector_store.similarity_search(query=query)
    context=""
    for i in result:
        context+=i.page_content +"\n"
    return {"context":context,"question":query}
prompt=PromptTemplate.from_template("""
      you are a assistant that give a correct answer based on the question. if u dont 
    know the answer say simply give related to pdf
    context={context}
    question={question}

""")
chain=vamsi| prompt| llm
res=chain.invoke("what are the name of the projects")
print(res.content)