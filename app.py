import streamlit as st
from backend import playGround , custum_prompt

st.set_page_config(page_title= "Prompt playGround", page_icon="ball-pit.png")
st.title("Prompt playGround")
st.subheader('Learn with Fun')

input_message = st.text_input("Enter your prompt here")

role=st.sidebar.selectbox("role",["Teacher","Interviewer","Technical Writer","Friendly Assistant"])
task=st.sidebar.selectbox("task",["Explain","Summarize","Generate","Rewrite"])
constraint=st.sidebar.selectbox("constraint",["Simple Language","Bullet Points","Examples","Professional Tone"])
length=st.sidebar.selectbox("length",["Short","Medium","Detailed"])
output=st.sidebar.selectbox("output",["Constructed Prompt","Generated Response"])
button=st.sidebar.button("submit")
  
if button:
    if role and task and constraint and length and output and input_message :
        st.write("Your custmize prompt : ")
        f=custum_prompt(role,task,constraint,length,output,input_message)
        st.write(f)
        st.spinner("processing")
        st.write("Result")
        result =playGround(role,task,constraint,length,output,input_message)
        st.write(result) 
    
    else:
        st.write("please fill all the field")
else:
    pass