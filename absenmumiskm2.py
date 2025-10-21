import streamlit as st
import pandas as pd
import os

# File to store submissions
CSV_FILE = "submissions.csv"

st.title("Text Submission App")

# Text input
user_input = st.text_input("Enter your text:")

# Submit button
if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter some text before submitting.")
    else:
        # Load or create dataframe
        if os.path.exists(CSV_FILE):
            df = pd.read_csv(CSV_FILE)
        else:
            df = pd.DataFrame(columns=["Text"])

        # Add new submission
        new_row = pd.DataFrame({"Text": [user_input]})
        df = pd.concat([df, new_row], ignore_index=True)

        # Save to CSV
        df.to_csv(CSV_FILE, index=False)

        st.success("✅ Text successfully saved!")

# Display current submissions
if os.path.exists(CSV_FILE):
    st.subheader("Current Submissions:")
    df_display = pd.read_csv(CSV_FILE)

    # Function to censor from second word onward
    def censor_from_second_word(text):
        words = str(text).split()
        if len(words) > 1:
            censored = [words[0]] + ["*" * len(w) for w in words[1:]]
            return " ".join(censored)
        else:
            return text

    # Add censored version
    df_display["Censored_Text"] = df_display["Text"].apply(censor_from_second_word)

    st.dataframe(df_display[["Censored_Text"]])
