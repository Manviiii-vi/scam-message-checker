import streamlit as st

st.set_page_config(page_title="Scam Message Checker", layout="centered")

st.title("🔍 Scam Message Checker")

message = st.text_area("Paste the message you received:", height=200)

scam_keywords = ["kyc", "otp", "click here", "update your account", "bank suspended", "verify now", "upi", "pan card", "urgent", "blocked", "account frozen", "immediate action"]

if st.button("Check Message"):
    if any(keyword in message.lower() for keyword in scam_keywords):
        st.error("⚠️ This message looks suspicious. Don't share personal info.")
    else:
        st.success("✅ This message seems safe.")
