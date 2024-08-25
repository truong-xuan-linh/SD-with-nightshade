import streamlit as st
from src.sd import ImageGenerationService

revision_mapper = {
    "Normal": "d62e343a382bd08589041f478435ad4650c07004",
    "Attacked": "befa4d9743d6d470fc17e7cd29e1a074618c3c4a"
}
st.set_page_config(page_title="Image Generation Demo", page_icon="🌌")

st.markdown("# Image Generation Demo")
st.sidebar.header("Image Generation Demo")

with st.sidebar:
    with st.form(key="image_generation_form"):
        
        prompt = st.text_input(label="Prompt")
        model = st.selectbox(label="Model", options=['Normal', 'Attacked'])
        if st.session_state.get("model",  None) is None:
            st.session_state.model = ImageGenerationService(revision_mapper[model])
        elif st.session_state.model != model:
            st.session_state.model = ImageGenerationService(revision_mapper[model])
            
        if st.form_submit_button(label="Submit"):
            image_response = st.session_state.model.run(prompt)
            st.session_state.image = image_response
                
# if "image_url" in st.experimental_get_query_params():
if "image" in st.session_state:
    # image_url = st.experimental_get_query_params()["image_url"][0]
    image = st.session_state.image
    st.image(image)