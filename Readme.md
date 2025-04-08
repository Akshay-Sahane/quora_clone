# Quora Clone (Django)

This is a simplified Quora-like platform built using Django, designed as a learning/demo project. It supports user
registration, login/logout, asking questions, answering them, and an upvote system.

## 🚀 Features

- User Registration and Login (with custom user model)
- Ask questions
- Answer existing questions
- Upvote system for answers
- Pagination for user-asked questions
- Fully functional using Django templates (no external frontend framework)

## 🛠️ Setup Instructions

1. **Clone the repository**
   git clone https://github.com/your-username/quora-clone.git
   cd quora-clone

2. **Create a virtual environment**
   python -m venv env
   source env/bin/activate # On Windows: env\Scripts\activate

3. **Install dependencies**
   pip install -r requirements.txt

4. **Apply migrations**
   python manage.py migrate

5. **Create a superuser**
   python manage.py createsuperuser

6. **Run the development server**
   python manage.py runserver

7. Open your browser
   visit http://127.0.0.1:8000/

📄 License
This project is licensed for educational and demonstration purposes.