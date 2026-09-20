import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import re

st.title("🎥 YouTube Video Load and QNA")

# YouTube URL
url = st.text_input("https://www.youtube.com/watch?v=libKVRa01L8")

# Question
question = st.text_input("Ask a question about the video")


def get_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([\w-]+)", url)

    if match:
        return match.group(1)

    return None


if st.button("Load Video"):

    video_id = get_video_id(url)

    if video_id:

        try:
            api = YouTubeTranscriptApi()

            transcript = api.fetch(video_id)

            text = " ".join(
                item.text for item in transcript
            )

            st.session_state["video_text"] = text

            st.success("Video loaded successfully!")

            st.subheader("Video Transcript")

            st.text_area(
                "Transcript",
                text,
                height=300
            )

        except Exception:
            st.error("Transcript is not available.")

    else:
        st.error("Please enter a valid YouTube link.")


if st.button("Ask Question"):

    if "video_text" not in st.session_state:

        st.warning("First load a YouTube video.")

    elif not question:

        st.warning("Please enter a question.")

    else:

        text = st.session_state["video_text"]

        # Split transcript into sentences
        sentences = text.split(". ")

        # Find sentences containing words from question
        question_words = question.lower().split()

        answers = []

        for sentence in sentences:

            sentence_lower = sentence.lower()

            matches = 0

            for word in question_words:

                if len(word) > 3 and word in sentence_lower:
                    matches += 1

            if matches > 0:
                answers.append(sentence)

        st.subheader("💡 Answer")

        if answers:
            st.write(". ".join(answers[:5]))
        else:
            st.write(
                "I could not find an answer to this question "
                "in the video transcript."
            )
