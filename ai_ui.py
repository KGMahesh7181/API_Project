import streamlit as st
from groq import Groq

# 1. Page Configuration (The "Look" of the app)
st.set_page_config(page_title="My Groq AI", page_icon="⚡", layout="centered")

st.title(" Mahesh AI Interface")
st.subheader("Fastest LLM responses using Groq")

# 2. Setup Groq Client
# Replace with your actual key
client = Groq(api_key="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")

# 3. Create the UI Layout
# A sidebar for settings
with st.sidebar:
    st.title("Settings")
    model = st.selectbox("Choose a Model", ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"])
    temp = st.slider("Creativity (Temperature)", 0.0, 1.0, 0.7)

# 4. The Prompt Input
user_input = st.text_input("Ask me anything:", placeholder="Type your message here...")

# 5. The Magic: Fetching and Displaying
if user_input:
    with st.spinner("AI is thinking..."):
        try:
            # The API Call
            completion = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": user_input}],
                temperature=temp
            )
            
            response = completion.choices[0].message.content

            # 6. Display the response in a colorful box
            st.success("Response Received!")
            st.markdown(f"""
            <div style="background-color: #FFFFFF; padding: 20px; border-radius: 10px; border-left: 5px solid #7f00ff;">
                <p style="color: black; font-family: sans-serif;">{response}</p>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Error: {e}")

# Add a footer
st.divider()
st.caption("Powered by Groq LPUs & Streamlit")