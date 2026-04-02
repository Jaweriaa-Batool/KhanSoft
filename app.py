import streamlit as st
import joblib

# 1. Load the models
try:
    cat_model = joblib.load('category_model.pkl')
    pri_model = joblib.load('priority_model.pkl')
except:
    st.error("Model files (.pkl) not found! Please check if the files are in the correct folder.")

# 2. UI Title
st.title("🚀 Smart Task Predictor & Analyzer")
st.write("Write your task and AI will tell you its category and what its priority should be.")

# 3. User Input
task_input = st.text_input("Enter your task here:", placeholder="e.g., Finish the financial report")

if st.button("Predict"):
    if task_input:
        # Prediction logic
        category_pred = cat_model.predict([task_input])[0]
        priority_pred = pri_model.predict([task_input])[0]
        
        # Result Display
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"**Category:** {category_pred}")
        with col2:
            st.info(f"**Priority:** {priority_pred}")
            
        # Bonus NLP Analysis (Short Logic)
        st.write("---")
        st.write(f"**Analysis:** Task length is {len(task_input)} characters.")
    else:
        st.warning("Please enter a task first!")