# ChatRAGI

ChatRAGI is an AI-powered chatbot that leverages **Retrieval-Augmented Generation (RAG)** to provide insightful and context-aware responses. Built with **LlamaIndex**, **Gemini AI**, and **Streamlit**, this application efficiently retrieves relevant information from a local dataset and generates intelligent responses.

## 🚀 Features

- **AI-Powered Q&A** – Uses Google's Gemini AI for intelligent responses.
- **Retrieval-Augmented Generation (RAG)** – Enhances responses by fetching relevant data.
- **Streaming Responses** – Provides real-time, token-by-token AI responses.
- **Persistent Storage** – Saves indexed data for faster retrieval.
- **User-Friendly Interface** – Built with Streamlit for an intuitive chat experience.

## 🛠️ Installation

This project uses [UV](https://github.com/astral-sh/uv) as the package manager.

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/ChatRAGI.git
cd ChatRAGI
```

### 2️⃣ Install Dependencies

```sh
uv sync
```

### 3️⃣ Set Up Environment Variables

Create a `.env` file in the project root and add your **Google API Key**:

```sh
GOOGLE_API_KEY=your_google_api_key
```

### 4️⃣ Prepare Data

Place your documents inside the `data/` directory, Currently it contains 'paul_graham_essay.txt'. If the storage directory (`./storage`) doesn't exist, the index will be built automatically on the first run.

### 5️⃣ Run the Application

```sh
streamlit run app.py
```

## 📜 Usage

1. Open the web app in your browser (Streamlit will provide a local URL).
2. Type a question or prompt in the chat box.
3. The AI retrieves relevant context and generates a response in real-time.

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin feature-branch`
5. Open a **Pull Request**.

## 🚀 Future Features

- **Chat History** – Implement a feature to save and display past conversations for user reference.
- **User Data Upload** – Allow users to upload their own documents to be used as context for generating responses.
- **Customizable Responses** – Allow users to customize the tone and style of the chatbot's responses.

## ⚖️ License

This project is licensed under the **MIT License**.

---

🔹 _Built with ❤️ using LlamaIndex, Gemini AI, and Streamlit._
