import streamlit as st
import os
import random
from datetime import datetime, timedelta

# File to store data
USER_DATABASE_FILE = "user_database.txt"
TASK_DATABASE_FILE = "task_database.txt"

# ================= SAVE AND LOAD DATA =================
def save_user(username, password):
    with open(USER_DATABASE_FILE, "a") as file:
        file.write(f"{username},{password}\n")

def load_users():
    if os.path.exists(USER_DATABASE_FILE):
        with open(USER_DATABASE_FILE, "r") as file:
            users = [line.strip().split(",") for line in file.readlines() if "," in line]
        return {user[0]: user[1] for user in users}
    return {}

def save_task(username, task, priority, deadline):
    with open(TASK_DATABASE_FILE, "a") as file:
        file.write(f"{username},{task},{priority},{deadline}\n")

def load_tasks(username):
    if os.path.exists(TASK_DATABASE_FILE):
        with open(TASK_DATABASE_FILE, "r") as file:
            tasks = [line.strip().split(",") for line in file.readlines()]
        return [task for task in tasks if task[0] == username]
    return []

# ================= AI SUGGESTION =================
def suggest_task(task_count, priority):
    suggestions = [
        "Complete high-priority tasks first.",
        "Break large tasks into smaller steps.",
        "Set realistic deadlines to avoid stress.",
        "Focus on one task at a time to boost productivity.",
        "Review your task list at the start of each day.",
        "Use time-blocking to schedule your tasks."
    ]
    
    # Priority-based suggestions
    if priority == "High":
        suggestions.append("Prioritize high-priority tasks before starting new ones.")
    elif priority == "Medium":
        suggestions.append("Focus on medium-priority tasks in between other work.")
    else:
        suggestions.append("Low-priority tasks can be handled after urgent work.")

    # Task count-based suggestions
    if task_count >= 5:
        suggestions.append("You have many tasks! Try to reduce workload.")

    return random.choice(suggestions)

# ================= DEADLINE NOTIFICATION =================
def check_deadline(deadline):
    today = datetime.today().date()
    task_date = datetime.strptime(deadline, "%Y-%m-%d").date()

    if task_date == today:
        return "Today's deadline!"
    elif task_date == today + timedelta(days=1):
        return "Tomorrow is the last date!"
    elif task_date < today:
        days_ago = (today - task_date).days
        return f"Deadline was {days_ago} days ago"
    return ""

# ================= MAIN FUNCTION =================
def main():
    st.set_page_config(page_title="AI Task Manager", layout="wide")

    # ✅ Background image using direct URL
    # page_bg_img = f"""
    # <style>
    # .st-emotion-cache-t1wise {{
    # background-image: url("https://tripleareview.com/wp-content/uploads/2023/08/Best-AI-Task-Manager-Tools-for-Booosting-Productiivity.jpg");
    # background-size: cover;
    # background-position: center;
    # background-attachment: fixed;
    # }}
    # </style>
    # """
    # st.markdown(page_bg_img, unsafe_allow_html=True)

    # Left side menu
    menu = ["Login", "Signup", "Dashboard"]
    choice = st.sidebar.selectbox("Menu", menu)

    # SESSION STATE to store login status
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['username'] = ""

    # ================= SIGNUP PAGE =================
    if choice == "Signup":
        st.subheader("Create an Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type="password")

        if st.button("Signup"):
            if len(new_password)<8:
                st.error("Password must be atleast 8 characters long!")
            else:
                users = load_users()
                if new_user in users:
                    st.error("Username already exists. Try a different one.")
                else:
                    save_user(new_user, new_password)
                    st.success("Signup successful! You can now login.")

    # ================= LOGIN PAGE =================
    elif choice == "Login":
        st.subheader("Login to Your Account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            users = load_users()
            if username in users and users[username] == password:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success(f"Welcome {username}!")
            else:
                st.error("Invalid username or password , First You need to SignUp then Login...")

    # ================= DASHBOARD =================
    elif choice == "Dashboard":
        if not st.session_state['logged_in']:
            st.warning("Please login to access the dashboard.")
        else:
            st.subheader(f"Welcome, {st.session_state['username']}")

            # Form to add tasks
            st.subheader("Add New Task")
            task = st.text_input("Task Name")
            priority = st.selectbox("Priority", ["High", "Medium", "Low"])
            deadline = st.date_input("Deadline")

            if st.button("Add Task"):
                if task:
                    save_task(st.session_state['username'], task, priority, deadline)
                    st.success("Task added successfully!")
                    st.snow()

                    # Load tasks to calculate suggestions
                    tasks = load_tasks(st.session_state['username'])
                    ai_suggestion = suggest_task(len(tasks), priority)
                    st.info(f"*AI Suggestion:* {ai_suggestion}")
                else:
                    st.error("Please enter a task name.")

            # Display existing tasks with deadline notifications
            st.subheader("Your Tasks")
            tasks = load_tasks(st.session_state['username'])
            if tasks:
                for i, task in enumerate(tasks):
                    task_name, priority, deadline = task[1], task[2], task[3]
                    st.write(f"{i + 1}.)  {task_name} -->  Priority : { priority} , Deadline : { deadline}")

                    # Show deadline notification
                    notification = check_deadline(deadline)
                    if notification:
                        st.warning(notification)
            else:
                st.write("No tasks added yet.")

            # Logout Button
            if st.button("Logout"):
                st.session_state['logged_in'] = False
                st.session_state['username'] = ""
                st.success("You have been logged out.")

if __name__ == "__main__":
    main()