import streamlit as st;
import openai
import requests
from streamlit_lottie import st_lottie;
 
openai.organization = ""
openai.api_key = "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"

## Header Section ##
with st.container():
    st.header("Welcome to TrendSum")
    st.title("This allow you to put the name of the topic and It will give you the summary of the trending news on that topic")
    st.markdown("This tool help you to get the summary of latest trending news")
    st.write("[More work you'll find here >] (https://www.github.com/karankulshrestha)")

def getNews(query):
    url = "https://bing-news-search1.p.rapidapi.com/news/search"
    querystring = {"q":query, "count":"5", "freshness":"Day","textFormat":"Raw","safeSearch":"Off"}
    headers = {
        "X-BingApis-SDK": "true",
        "X-RapidAPI-Key": "abf7b3d6c1msh12054559a640e40p133beejsnbf7a1e578511",
        "X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    output = response.json()
    with open('temp.txt', 'w') as f:
        for data in output['value']:
            st.write(data['description'])  
            f.writelines(data['description'])
            f.write('\n')
    f.close()  
    
    return 'temp.txt'
    

def getSummary(query):
    tldr_tag = "\n\nTl;dr"
    filetxt = getNews(query)
    text_file = open(filetxt, "r")
    data = text_file.read() + tldr_tag
    text_file.close()
    response = openai.Completion.create(engine="text-davinci-002",prompt=data,temperature=0.3,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0,
    )
    st.subheader("Here is your summary!")
    st.write(response["choices"][0]["text"])


## Middle Part ##
with st.container():
    text_input = st.text_input(
        "Please put the topic 👇",
        placeholder="write the topic",
    )
        
    if text_input:
       getSummary(text_input)
