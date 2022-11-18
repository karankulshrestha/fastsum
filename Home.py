import requests;
import streamlit as st;
from streamlit_lottie import st_lottie;

st.set_page_config(page_title="TrendSum", page_icon=":cyclone:", layout="wide")

st.sidebar.success("select a page above")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

## load_css
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style/style.css")

## loading assets
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_PmGV4skHBv.json")

## Header Section ##
with st.container():
    st.subheader("Hi, I am Karan Kulshrestha :wave: and I welcome you from Team NAVIS")
    st.title("TrendSum and YoutubeSum > Smart way to live in a New World")
    st.subheader(":kissing_smiling_eyes: TrendSum help you to read top trending news on any topic in a very small time period")
    st.write("---")
    st.subheader(":heart_eyes: YoutubeSum help you to read short summary of any youtube video in any language")
    st.write("[More work you'll find here >] (https://www.github.com/karankulshrestha)")


## What I do ##
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How it works ?")
        st.write(
            """
            This is basically build with gpt-3 ml model by OpenAI, NEWS API and Whisper again OpenAI model.
            - First audio get retrieve from video and converted into text using Whisper (YoutubeSum)
            - input query request sent to API and we retrive the News data in the response (TrendSum)
            - then we collect and process the news.
            - We use GPT-3 model to summarize the news using it's Deep learning technology.
            - finally, output received by our users.

            If it all seems cool please don't forget to check the project repo > (https://github.com/KaranKulshrestha/navis)
            """
        )
    
    with right_column:
        st_lottie(lottie_coding, height=350, key="ai")

## project details ##

def myBootstrapEvent():
        st.header("A Button was clicked !")

with st.container():
    st.write("---")
    st.subheader("Project Details")
    st.header("Pitch Video")
    st.video("https://youtu.be/yVV_t_Tewvs")
        

## contact form ##

with st.container():
    st.write("---")
    st.header("Contact Me :smiley:")

    contact_form = """
        <form action="https://formsubmit.co/karankul2003@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """

    left_col, right_col = st.columns(2)
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st.empty()
