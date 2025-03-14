import streamlit as st
import time

# Set Page Configuration
st.set_page_config(page_title="Streamlit Fun Features", page_icon="🎈")

# Title and Description
st.title("🎉 Experiment with Streamlit Fun Features!")
st.write("Click the buttons to see cool Streamlit effects. 🚀")

# 1. Balloons 🎈
if st.button("Release Balloons!"):
    st.balloons()

# 2. Snow Effect ❄️
if st.button("Make it Snow!"):
    st.snow()

# 3. Toast Notification 🔔
if st.button("Show Toast Notification"):
    st.toast("🎉 This is a toast message!")

# 4. Progress Bar ⏳
if st.button("Start Progress Bar"):
    progress_bar = st.progress(0)
    for percent in range(100):
        time.sleep(0.02)
        progress_bar.progress(percent + 1)

# 5. Status Message ✅
if st.button("Show Status Message"):
    with st.status("Processing... ⏳"):
        time.sleep(2)
        st.success("✅ Done!")

# 6. Success, Warning, and Error Messages 🚨
if st.button("Show Alerts"):
    st.success("🎉 Success! Your action was completed.")
    st.warning("⚠️ Warning! Check your inputs.")
    st.error("❌ Error! Something went wrong.")

# 7. Code Block Display 🖥️
st.subheader("📜 Code Block Example")
st.code("print('Hello, Streamlit!')", language="python")

# 8. Metric Display 📊
st.subheader("📊 Live Metrics Example")
st.metric(label="Stock Price", value="$1,234.56", delta="+5.3%")

# 9. Expander for Hidden Content 📂
with st.expander("See More Details"):
    st.write("Here is some hidden content!")

# 10. Audio & Video Playback 🎵🎥
st.subheader("🎵 Play Audio")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.subheader("🎥 Play Video")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")

st.write("Enjoy experimenting with Streamlit! 🚀")
