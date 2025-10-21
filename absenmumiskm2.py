import streamlit as st
import pandas as pd
import os

# File name for storing data
EXCEL_FILE = "submissions.xlsx"

st.title("Absen Mumi SKM 2 ✨")

# Create input field
user_input = st.text_input("Ketik nama: (contoh: fauzan / bagas ijin kerja / rehan sakit demam)")

# Submit button
if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Jazakumullohukhoiro")
    else:
        # Check if Excel file already exists
        if os.path.exists(EXCEL_FILE):
            df = pd.read_excel(EXCEL_FILE)
        else:
            df = pd.DataFrame(columns=["Text"])

        # Append new row
        new_row = pd.DataFrame({"Text": [user_input]})
        df = pd.concat([df, new_row], ignore_index=True)

        # Save back to Excel
        df.to_excel(EXCEL_FILE, index=False)

        st.success("✅ جَزَاكُمُ اللهُ خَيْرًا")

if os.path.exists(EXCEL_FILE):
    st.subheader("Kehadiran:")
    df_display = pd.read_excel(EXCEL_FILE)

    # Function to censor all words except the first
    def censor_from_second_word(text):
        words = str(text).split()
        if len(words) > 1:
            # Keep first word, replace others with *****
            censored = [words[0]] + ["*" * len(w) for w in words[1:]]
            return " ".join(censored)
        else:
            return text

    # Create censored column for display
    df_display["Absen"] = df_display["Text"].apply(censor_from_second_word)

    st.dataframe(df_display[["Absen"]])
