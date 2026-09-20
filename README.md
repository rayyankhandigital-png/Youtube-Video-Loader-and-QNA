# 🎥 YouTube Video Loader and QNA

## 📌 Description

**YouTube Video Load and QNA** is a simple Streamlit-based application that allows users to load a YouTube video's transcript and ask questions about its content. The application uses the **YouTube Transcript API** to retrieve the transcript from a provided YouTube URL.

The user first enters a YouTube video link and clicks the **Load Video** button. The application extracts the video ID from the URL and retrieves the available transcript. The transcript is then displayed on the screen and stored using Streamlit session state.

After loading the video, the user can enter a question related to the video's content. The application compares the words in the question with sentences from the transcript and finds sentences containing relevant keywords. These matching sentences are then displayed as the answer.

The project uses **Python**, **Streamlit**, **YouTube Transcript API**, and **Regular Expressions**. It provides a simple and beginner-friendly example of working with YouTube transcripts and building an interactive question-answering application.

Although the current version uses keyword matching instead of an AI language model, it can be extended in the future with **LLMs, embeddings, vector databases, and RAG (Retrieval-Augmented Generation)** to provide more accurate and contextual answers.

This project is useful for learning how to build simple web applications with Streamlit and how to retrieve and process YouTube video transcripts.


## 🚀 Features

* 🎥 Enter a YouTube video URL
* 📝 Load the video's transcript
* 📄 Display the transcript in the app
* ❓ Ask questions about the video
* 🔍 Search the transcript for relevant information
* 💡 Display matching answers
* ⚠️ Shows helpful messages when the transcript or video URL is invalid

## 🛠️ Technologies Used

### **Streamlit**

**Streamlit** is used to create the web interface for the application. It provides text boxes, buttons, messages, and transcript display without requiring HTML or CSS.

### **YouTube Transcript API**

The **YouTube Transcript API** is used to retrieve the transcript of a YouTube video using its video ID.

### **Regular Expressions (re)**

The `re` library is used to extract the YouTube video ID from the provided URL.

### **Python**

Python is used to build the complete application and implement the transcript loading and question-answering logic.

## ⚙️ How It Works

1. The user enters a YouTube video URL.
2. The application extracts the video ID from the URL.
3. The YouTube Transcript API retrieves the video's transcript.
4. The transcript is stored in Streamlit's session state.
5. The user enters a question about the video.
6. The application compares words from the question with sentences in the transcript.
7. Matching sentences are collected.
8. The relevant sentences are displayed as the answer.

## 📂 Project Structure

```text
YouTube-Video-QNA/
│
├── app.py
├── requirements.txt
└── README.md
```

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/rayyankhandigital-png/Youtube-Video-Loader-and-QNA/edit/main/README.md
```



## ▶️ Run the Application

Run the following command:

```bash
streamlit run app.py
```

The application will open in your web browser.

## 💻 Example

Enter a YouTube URL such as:

```text
https://www.youtube.com/watch?v=libKVRa01L8
```

Click **Load Video**, and the transcript will be displayed.

Then enter a question such as:

```text
What is the video about?
```

Click **Ask Question** to search the transcript for relevant sentences.

## ⚠️ Limitations

* The video must have an available YouTube transcript.
* The question-answering system uses keyword matching rather than an AI language model.
* Answers depend on words from the question appearing in the transcript.
* It may not understand the meaning or context of complex questions.

## 📄 Requirements

Create a `requirements.txt` file containing:

```text
streamlit
youtube-transcript-api
```

## 🙌 Conclusion

This project demonstrates how **Streamlit** and the **YouTube Transcript API** can be combined to create a simple application for loading YouTube transcripts and answering questions using transcript-based keyword matching. It is a good starting point for building more advanced AI-powered video Q&A applications.
