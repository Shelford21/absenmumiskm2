import streamlit as st
import pandas as pd
import os

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
# File to store submissions
CSV_FILE = "submissions.csv"
# Set your admin password here
ADMIN_PASSWORD = "fauzann"

st.set_page_config(page_title="Absen Mumi SKM 2",
                   page_icon="✨",
                   layout="wide")

st.markdown(
        """
        <div class="transparent-container">
            <h1>✨ Absen Mumi SKM 2 </h1>
            <h4>
            يٰٓاَيُّهَا الَّذِيْنَ اٰمَنُوْٓا اِنْ تَنْصُرُوا اللّٰهَ يَنْصُرْكُمْ وَيُثَبِّتْ اَقْدَامَكُمْ <br><br> 💡"Wahai orang-orang yang beriman, jika kamu menolong (agama) Allah, niscaya Dia akan menolongmu dan meneguhkan kedudukanmu"
    </h4>
    
        """,
        unsafe_allow_html=True
    )

# Text input
user_input = st.text_input("Ketik nama: (contoh: fauzan / bagas ijin kerja / rehan sakit demam)")

# Submit button
if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Tidak boleh kosong ok!")
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
        st.success("✅ جَزَاكُمُ اللهُ خَيْرًا")

# Display current submissions
if os.path.exists(CSV_FILE):
    st.subheader("Kehadiran hari ini:")
    df_display = pd.read_csv(CSV_FILE)

    # Function to censor from second word onward
    def censor_from_second_word(text):
        words = str(text).split()
        if len(words) > 1:
            censored = [words[0]] + ["*" * len(w) for w in words[1:]]
            return " ".join(censored)
        else:
            return text

    df_display["Absen"] = df_display["Text"].apply(censor_from_second_word)
    st.dataframe(df_display[["Absen"]])

# Divider
st.markdown("---")

# Admin section
st.subheader("Khusus Admin")

# Ask for password first
admin_password = st.text_input("Masukan password untuk menggunakan fitur:", type="password")

# If password is correct, show expander
if admin_password == ADMIN_PASSWORD:
    with st.expander("🧹 Clear all data"):
        if st.button("Clear Data"):
            if os.path.exists(CSV_FILE):
                os.remove(CSV_FILE)
                st.success("✅ All data cleared successfully!")
            else:
                st.info("No data file found to clear.")
else:
    if admin_password != "":
        st.error("❌ Incorrect password.")












