# 🧠 AI Task Management System

An intelligent task manager built using **Python** and **Streamlit** that supports **user authentication (Login/Signup)**, **AI-based task suggestions**, and stores data in simple `.txt` files — no external databases needed.

---

## 🚀 Live App

🌐 **Try the App**: https://ai-poweredtms.streamlit.app/

---

## ✨ Key Features

* 🔐 **User Authentication**: Signup and Login with basic credential check
* 🎯 **Set Priorities** (High, Medium, Low)
* 🤖 **AI Suggestions** for tasks and productivity tips
* 📄 **Local Storage** in `.txt` files (`user_database.txt`, `task_database.txt`)
* 🧠 **Clean Streamlit UI** hosted on Streamlit Cloud

---

## 🔐 Login / Signup Functionality

* **Signup Page**: New users can register by entering a name, username, and password.
* **Login Page**: Existing users can log in with their credentials.
* User credentials are stored in `user_database.txt` in a simple format (e.g., comma-separated or JSON lines).
* Only authenticated users can access or modify tasks.

---

## 🗃 Project Structure

```bash
.
├── app.py               # Main Streamlit application
├── user_database.txt    # Stores user credentials (name, username, password)
├── task_database.txt    # Stores tasks for each user
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 💻 Run Locally

1. **Clone the repository**:

```bash
git clone https://github.com/Priyagupta0/AI_Task_Management_System
cd ai-task-manager
```

2. **Install the required libraries**:

```bash
pip install -r requirements.txt
```

3. **Start the Streamlit app**:

```bash
streamlit run app.py
```

---

## 🧠 How AI Suggestions Work

* Based on entered task titles, the app suggests priorities or motivational prompts.
* Uses simple rule-based logic (or optionally lightweight AI models) for efficiency.
* Can be expanded later to integrate with OpenAI or other ML APIs.

---

## 📝 Example Entries

### user\_database.txt

```
Priya,priya123,securepassword
```

### task\_database.txt

```
priya123,Complete ML assignment,High,2025-06-11 10:00
```

---

## 📦 Example `requirements.txt`

```streamlit
```
---

## 🙋 Author

**Priya Gupta**
GitHub: [@Priyagupta0](https://github.com/Priyagupta0)

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---
