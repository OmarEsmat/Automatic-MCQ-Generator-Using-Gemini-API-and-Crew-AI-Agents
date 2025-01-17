import streamlit as st
import requests

# Set the title of the Streamlit app
st.title("Automatic MCQ Generator")

# Create a text area for user input
input_text = st.text_area("Enter your text:")

# Add a button to trigger MCQ generation
if st.button("Generate MCQs"):
    # Send a POST request to the MCQ generation API
    response = requests.post("http://127.0.0.1:5000/generate-mcq", json={"text": input_text})
    
    # Check if the request was successful
    if response.status_code == 200:
        st.write("Generated MCQs:")
        
        # Extract the MCQs from the response
        mcqs = response.json()["mcqs"]
        
        # Iterate over each MCQ and display it
        for mcq in mcqs:
            question = mcq["question"]
            options = mcq["options"]
            correct_answer = mcq["correct_answer"]
            
            # Display the question
            st.write(f"**Question:** {question}")
            
            # Display the options
            for i, option in enumerate(options):
                st.write(f"{chr(65 + i)}. {option}")
            
            # Display the correct answer
            st.write(f"**Correct Answer:** {correct_answer}")
            st.write("---")  # Add a separator between MCQs
    else:
        # Display an error message if the request failed
        st.error(f"Error generating MCQs. Status code: {response.status_code}")