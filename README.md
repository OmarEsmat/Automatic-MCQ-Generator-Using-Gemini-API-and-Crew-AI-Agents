# 📝 Automatic MCQ Generator

Welcome to the **Automatic MCQ Generator** project! 🎉 This tool leverages the power of AI to generate multiple-choice questions (MCQs) from a given text. Perfect for educators, learners, and anyone looking to create engaging quizzes quickly and efficiently. 🚀

---

## 🌟 Features

- **Dynamic MCQ Generation**: Convert any text into relevant MCQs in seconds.
- **Interactive Interface**: Built with **Streamlit** for a seamless user experience.
- **AI-Powered Back-end**: Utilizes **Gemini API** for content generation.
- **Cloud Storage**: Stores user inputs and generated MCQs in **Supabase**.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit 🖥️
- **Backend**: Flask 🌐
- **Database**: Supabase 🛢️
- **AI Model**: Gemini API 🤖
- **Language**: Python 🐍

---

## 🚀 How It Works

1. **Input Text**: Enter a block of text in the Streamlit app.
2. **Generate MCQs**: Click the "Generate MCQs" button.
3. **View Results**: The app displays the generated questions, options, and correct answers.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/OmarEsmat/Automatic-MCQ-Generator-Using-Gemini-API-and-Crew-AI-Agents.git

   cd mcq-generator
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file with the following:
   ```env
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

4. **Run the Flask API**:
   ```bash
   python app.py
   ```

5. **Launch the Streamlit App**:
   ```bash
   streamlit run mcq_app.py
   ```

---

## 📚 Usage

1. Open the Streamlit app in your browser.
2. Paste your text into the input box.
3. Click **"Generate MCQs"**.
4. View the generated MCQs along with the correct answers.

---

## 🌐 API Endpoints

- **`POST /generate-mcq`**:
  - **Request**: `{ "text": "Input text here" }`
  - **Response**: `{ "mcqs": [...] }`

---

## 🚧 Future Enhancements

- 🌟 Add support for multiple languages.
- 📊 Include detailed analytics for generated MCQs.
- 🤝 Integrate with learning management systems (LMS).

---

## 📧 Contact

For any queries or suggestions, feel free to reach out:
- 📧 Email: omaresmat31@gmail.com
- 🌐 GitHub: [OmarEsmat](https://github.com/OmarEsmat)

---

🎉 **Happy MCQ Generating!** 🎉

