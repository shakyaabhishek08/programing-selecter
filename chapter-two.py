import streamlit as st
st.title("chai maker aap")
if st.button("make chai"):
  st.success("your chai is being brewed")

add_masala=st.checkbox("add masala") 
if add_masala:
 st.write("masala added to your chai")
tea_type =st.radio("pick your chai base:",["milk","water","almond milk"])
st.write(f"selected base {tea_type}")

flavour=st.selectbox("choose flavour:",["adrak","mint","tulsi","kesar"])
st.write(f"selected your flavour{flavour}")
sugar =st.slider("sugar level:",0,10,3)
st.write(f"selected sugar level {sugar}")
cups=st.number_input("how many cups",min_value=1,max_value=10,step=1)
st.write(f"selected sugar level{cups}")
name =st.text_input("enter your name")
if name:
    st.write(f"welcome,{name} !youe chai is on the way")
dob=st.date_input("select your daet of brith")
st.write(f"select your daet of birht {dob}")
