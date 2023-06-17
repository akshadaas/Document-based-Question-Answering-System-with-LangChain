# Document-based-Question-Answering-System-with-LangChain
Built a Document-based Question Answering System with LangChain, OpenAI and streamlit webapp.

# What is langchain models?
It is an open source framework that allows AI developers to combine large language models like GPT4 with custom data to perform downstream tasks like summarization, Question-Answering, chatbot etc.

# Limitations of LLM models:
  1. LLM models are general in nature
  2. They trained on data upto specific period
  
 LangChain overcomes these limitations by connection LLM models to custom data. It allows LLM models to access recent information in the form of documents, reports and website info.
 
 # How does Langchain work with LLM models?
   LangChain takes a big source of data (here: 50 pages PDF) and breaking it down into smallar chunks which are then embedded into vector space. These vector representation of documents used in conjunction with LLM to retrieve only the relevant information that is referenced when creating a prompt-completion pair. LangChain will query the vectorized representation of prompt to store in vector space for relevant information. Its like mini-google to your documnet. The relevant information then feed to LLM models to generate our output.
    

![Langchain architecture](https://github.com/akshadaas/Document-based-Question-Answering-System-with-LangChain/assets/36268039/38541249-afd3-4a7d-a152-35d1eaddef02)

# How to run?
1. Make sure to install all dependencies with pip install -r requirements.txt
2. Put your OpenAI API key and SerpAPI key before running the application
3. Run as streamlit run application.py

Output of Application:

![Screenshot (4)](https://github.com/akshadaas/Document-based-Question-Answering-System-with-LangChain/assets/36268039/eebf91c3-08c6-4e90-b962-2da91579dcb0)
