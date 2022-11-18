import streamlit as st;
import openai
from pytube import YouTube 
import whisper

openai.organization = ""
openai.api_key = "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"

with st.container():
    st.header("Youtube Summary")
    st.title("Get the summary of any YouTube video in any language")
    

## input url of video ##

with st.container():
    st.write("---")
    text_input = st.text_input(
        "Please paste the url of the video 👇",
        placeholder="paste the url",
    )
        
    if text_input:
        try: 
            # object creation using YouTube
            # which was imported in the beginning 
            with st.spinner('Wait for it...'):
                tldr_tag = "\n\nTl;dr"
                yt = YouTube(text_input)
                yt.streams.filter(file_extension='mp3')
                stream = yt.streams.get_by_itag(139)
                stream.download('',"audio.mp3")
                model = whisper.load_model("base")
                result = model.transcribe("audio.mp3")
                content = result["text"]
                st.write(content)
                response = openai.Completion.create(engine="text-davinci-002",prompt=content + tldr_tag,temperature=0.3,
                max_tokens=200,
                top_p=1.0,
                frequency_penalty=0,
                presence_penalty=0,
            )
                st.subheader("Here is your summary!")
                st.write(response["choices"][0]["text"]) 
            st.success('Done!')
        except: 
            print("Connection Error")
             
