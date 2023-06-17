from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import streamlit as st
import os
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI


os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "0e61bd3790a25a856c8cb99d7222909256496ce2a12519b954773b8121675af7"

def read_text(pdfreader):
	raw_text = ''
	for i, page in enumerate(pdfreader.pages):
		content = page.extract_text()
		if content:
			raw_text += content
	return raw_text
	
def pdf_processing(uploaded_file):
	pdfreader = PdfReader(uploaded_file)
	raw_text = read_text(pdfreader)
	text_splitter = CharacterTextSplitter(
		separator = "\n",
		chunk_size = 800,
		chunk_overlap  = 200,
		length_function = len)
	texts = text_splitter.split_text(raw_text)
	
	embeddings = OpenAIEmbeddings()
	document_search = FAISS.from_texts(texts, embeddings)
	chain = load_qa_chain(OpenAI(), chain_type="stuff")
	return chain,document_search
# Set the title of the Streamlit app
st.title("Hey! Ask me about your data!")

# Add a link to the Github repository that inspired this app
st.markdown("Inspired from AI applications created using LangChain")

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

if uploaded_file is not None:
	chain,document_search = pdf_processing(uploaded_file)

# Add a text input box for the user's question
user_question = st.text_input(
    "Enter Your Question : ",
    placeholder = "Cyanobacteria can perform photosynthetsis , are they considered as plants?",
)

# Generating the final answer to the user's question using all the chains
if st.button("Tell me about it", type="primary"):
	docs = document_search.similarity_search(user_question)
	#chain.run(input_documents=docs, question=query)
	st.success(chain.run(input_documents=docs, question=user_question))
