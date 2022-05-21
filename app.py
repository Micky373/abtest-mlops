import streamlit as st
from multiapp import MultiApp
from apps import dataset_display,model_accuracy_display # import your app modules here

app = MultiApp()

st.sidebar.markdown('# **A/B testing for SmartAd BIO**')
st.sidebar.markdown("""
The repo is all about A/B testing by using two groups the exposed and control group. The exposed group were given the smart ad about brand LUX where as the control groups were given some dummy ad about the brand LUX. Classical and Statistical A/B testing has been used to test. After all the tests our aim is to increase the efficiency of our BIO (Brand Impact Optimization)
""")

# Add all your application here
app.add_app("Data sets", dataset_display.app)
app.add_app("Model and accuracies", model_accuracy_display.app)
# The main app
app.run()