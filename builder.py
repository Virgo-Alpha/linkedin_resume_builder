import streamlit as st
from scraper import main

def main_app():
    st.title("LinkedIn Resume Builder")

    # Get LinkedIn credentials
    email = st.text_input("Enter your LinkedIn email:")
    
    password = st.text_input("Enter your LinkedIn password:", type="password")

    # Get LinkedIn profile URL
    linkedin_url = st.text_input("Enter your LinkedIn profile URL:")

    

    # Button to trigger resume generation
    if st.button("Generate Resume"):
        # check if email and url are valid
        if not email or not linkedin_url:
            st.error("Please enter a valid email and LinkedIn profile URL.")
            return
        # Check email validity
        elif "@" not in email:
            st.error("Please enter a valid email.")
            return
        # Check LinkedIn URL validity
        elif "linkedin.com" not in linkedin_url:
            st.error("Please enter a valid LinkedIn profile URL.")
            return
        else:
            # Call your function to generate the resume
            main(profile_url=linkedin_url, password=password, email=email)

            # Download the resume (file in this folder with .docx extension
            with open("resume.docx", "rb") as f:
                bytes = f.read()
                st.download_button(
                    label="Download Resume",
                    data=bytes,
                    file_name="resume.docx",
                    mime="application/octet-stream",
                    # Make sure to use the right label and file name
                )

# Run the Streamlit app
if __name__ == "__main__":
    main_app()
