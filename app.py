import streamlit as st
from transformers import pipeline

# Alpha.ai Configuration
st.set_page_config(page_title="Alpha.ai", page_icon="🤖")
st.title("Alpha.ai")
st.subheader("The Ultimate Global AI Assistant")

# Free Model loading (GPT-2)
@st.cache_resource
def load_alpha_engine():
    # Ye model free hai aur fast chalta hai
    return pipeline("text-generation", model="gpt2")

alpha_engine = load_alpha_engine()

# User Input Box
user_query = st.text_input("Aap Alpha.ai se kya poochhna chahte hain?", placeholder="Yahan likhein...")

if user_query:
    with st.spinner('Alpha.ai soch raha hai...'):
        # AI response generate ho raha hai
        result = alpha_engine(user_query, max_length=100, num_return_sequences=1)
        st.write("### Alpha.ai ka Jawab:")
        st.success(result[0]['generated_text'])

st.divider()
st.caption("© 2026 Alpha.ai | Global Empowerment through Intelligence")
