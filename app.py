import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://lottie.host/132629c4-543a-408a-a08e-f70827f9f62c/QfvRMPOBRm.json")
lottie_contact = load_lottieurl("https://lottie.host/0b6e4f04-a36d-4d53-8107-b77f1567d3ef/oEIMyfTOZc.json")

st.write("##")
st.subheader("Hey Guys:wave:")
st.title("My Portfolio Website")
st.write(''' 
I am gona explain berifly about how and from where I started my journey''')
st.write('---')

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About','Projects','Contacts'],
        icons = ['person','code-slash','chat-left-text-fill'],
        orientation = 'horizontal'
        )

if selected == 'About':
    col1, col2 = st.columns(2)
    with col1:
        st.write('##')
        st.subheader("I am Mukul Singh Jadoun")
        st.title("Aspiring Data Scientist")
    with col2:
        st_lottie(lottie_coder, height= 600, width= 400)


    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader('''
            Education
            - JNU
                - Bachelor of science - Mathametics
                - Grade: xyz
            - M.N Mordern public school
                - PCM
                - Grade: xyz
            ''')
        with col4:
            st.subheader('''
            Work Experience
            - CCE At Teleperformance Process Amazon
                - Duration(11/2019 - 05/2020)
                - Location: Jaipur, Rajasthan
            - Dispatcher at Ekart Logistic PVT.LTD
                - Duration(08/2020 - 11/2021)
                - Location: Jaipur, Rajasthan                                   
            - HR(Payroll Executive)
                - Duration(04/2022 - Recently Working)
                - Location: Jaipur, Rajasthan
            ''')

if selected =="Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col6= st.columns(1)
        with col6:
            st.subheader("Walmart data analysis project")
            st.write('''The Walmart Data Analysis Project is a comprehensive data exploration and visualization endeavor conducted with Python and the Pandas library. This project aims to extract valuable insights from the vast amounts of data collected by Walmart, one of the world's largest retail giants. By leveraging the powerful capabilities of Python's Pandas library, this analysis provides a detailed examination of various aspects of Walmart's business operations, enabling stakeholders to make informed decisions and drive strategic planning.''')
            st.markdown("[Visit Github Repo](https://github.com/Jadounshab/Walmart)")

if selected =="Contacts":
    st.header("Get in touch")
    st.write("##")


    contact_form = '''
    <form action="https://formsubmit.co/9929980456mp@gmail.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
    </form>'''                

    left_col, right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html= True)
    with right_col:
        st_lottie(lottie_contact, height= 600, width= 400)
