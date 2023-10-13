# News app

## 🌎 Overview

This is my first training Django project. It's a news app that provides basic functionality on most news platforms.

## 🌟 Features
- accounts
- login/signup
- password change/reset via email
- post creation/editing/commenting

## 📂 Project Structure

Here's a breakdown of the project's structure:

- `articles/`: Code related to articles.
- `newspaper_project/`: Main Django project.
- `pages/`: Code related to pages.
- `static/`: Static files for the project.
- `templates/`: HTML templates for the project.
- `users/`: Code related to users.
- `db.sqlite3`: SQLite database for the project.
- `manage.py`: Entry point for executing management commands.
- `requirements.txt`: Lists the Python packages required for the project.

## ⚙️ Installation

Ready to get started? Just follow these steps:

1. **Clone the repository:** `git clone https://github.com/your-username/your-repo.git`
2. **Create a virtual environment:** `python -m venv venv`
3. **Activate the virtual environment:**
    - **For Unix/Linux:** `source venv/bin/activate`
    - **For Windows:** `venv\Scripts\activate`
4. **Install the required packages:** `pip install -r requirements.txt`
5. **Run the migrations:** `python manage.py migrate`
6. **Start the development server:** `python manage.py runserver`

## 💻 Usage

Once the development server is up and running, you can access the news website by opening your browser and navigating to `http://localhost:8000`.

Here are some of the things you can do:

- Browse through articles.
- Create, update, and delete articles (requires authentication).
- Register and enjoy the content.

## 🤝 Contributing

If you spot any issues or have ideas for improvements, please let me know by opening an issue or submitting a pull request.

## 📄 License

This codebase is licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License). Feel free to use it, modify it, or share it with others.
