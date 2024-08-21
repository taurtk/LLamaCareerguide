import streamlit as st
import openai

# Initialize OpenAI client (make sure to replace with your actual API key)
client = openai.OpenAI(
    api_key="421f355109e949dc979d133afcd079ee",  # Replace this with your actual API key
    base_url="https://api.aimlapi.com",
)

# Set up the Streamlit app layout
st.title("Llama AI Career Guidance Platform")
st.write("Get personalized career advice and explore various tools to advance your career!")

# Sidebar for different use cases
use_case = st.sidebar.selectbox(
    "Choose a service",
    [
        "Job Recommendation",
        "Career Path Exploration",
        "Industry Trends Analysis",
        "Skill Gap Analysis",
        "Cover Letter Assistance",
        "Career Progress Tracking",
        "Networking Tips",
        "Interview Follow-up Guidance",
        "Salary Negotiation Advice",
        "Mentorship Program"
    ]
)

# Text input for user query based on the selected use case
if use_case == "Job Recommendation":
    st.write("Get personalized job recommendations based on your profile.")
    user_content = st.text_input("Describe your skills, preferences, and desired job role:")

elif use_case == "Career Path Exploration":
    st.write("Explore different career paths that match your current skills and interests.")
    user_content = st.text_input("Describe your skills and interests:")

elif use_case == "Industry Trends Analysis":
    st.write("Get the latest insights on industry trends and job market changes.")
    user_content = st.text_input("Specify your industry or field of interest:")

elif use_case == "Skill Gap Analysis":
    st.write("Identify skill gaps in your profile and get recommendations on how to bridge them.")
    user_content = st.text_input("Upload your resume or describe your current skills:")

elif use_case == "Cover Letter Assistance":
    st.write("Get help writing a cover letter tailored to a specific job or industry.")
    user_content = st.text_input("Describe the job and your experience relevant to it:")

elif use_case == "Career Progress Tracking":
    st.write("Track your career progress and receive advice on the next steps to grow.")
    user_content = st.text_input("Describe your career achievements and goals:")

elif use_case == "Networking Tips":
    st.write("Receive tips on how to build and expand your professional network.")
    user_content = st.text_input("Describe your current networking strategy or challenges:")

elif use_case == "Interview Follow-up Guidance":
    st.write("Get advice on how to follow up after an interview.")
    user_content = st.text_input("Describe the interview and the company you applied to:")

elif use_case == "Salary Negotiation Advice":
    st.write("Consult Llama AI on how to negotiate a salary offer.")
    user_content = st.text_input("Describe the job offer and your current compensation:")

elif use_case == "Mentorship Program":
    st.write("Find a mentor or become one to guide others in their careers.")
    user_content = st.text_input("Describe your mentorship needs or offer:")

if st.button("Get Advice"):
    if user_content:
        # Prepare system content and call the OpenAI API
        system_content = f"You are a Career advice agent providing {use_case}. Be descriptive and helpful."

        chat_completion = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            temperature=0.7,
            max_tokens=256,
        )

        response = chat_completion.choices[0].message.content

        # Display the response in the app
        st.write("**Advice:**")
        st.write(response)
    else:
        st.warning("Please enter your details.")
