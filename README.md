# 🔍 Flask SEO Checker

A login-protected Flask web application that allows users to analyze SEO data for any website URL, track results, and view their request history. The tool performs real-time scraping and gives a score based on standard SEO best practices.

---

## 🚀 Features

- 🔐 User registration and login (session-based)
- 🧠 SEO analyzer: title, meta tags, H1 count, image alt attributes, robots/canonical tags
- 📊 SEO score with percentage breakdown
- 📚 Request history table per user (using DataTables)
- 🗃️ PostgreSQL database integration
- 🛡️ Flask-Login for authentication
- 📦 Stores and displays SEO analysis history

---

## 🛠 Tech Stack

- Python 3.12
- Flask
- SQLAlchemy
- Flask-Login
- PostgreSQL
- BeautifulSoup (for scraping)
- DataTables (for frontend table rendering)

---
## 📂 Project Structure
flask-seo-checker/
├── app.py                   # Main Flask application
├── config.py                # Configuration settings (Dev/Prod)
├── models.py                # SQLAlchemy models
├── requirements.txt         # Python package dependencies
├── README.md                # Project documentation

├── templates/               # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   └── scrape.html

├── static/                  # Static assets
│   └── style.css

└── screenshots/             # UI screenshots (for README)
    ├── login.png
    └── dashboard.png

### ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/flask-seo-checker.git
cd flask-seo-checker
```

### 2. Create a Virtual Environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL

- Install PostgreSQL if not already installed.
- Create a new database named `flask_app`.
- Create a PostgreSQL user (e.g., `flask_user`) with password and grant privileges.

Update your `config.py` like this:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://flask_user:your_password@localhost:5433/flask_app"
```

### 5. Initialize the Database

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

### 6. Run the Application

```bash
python app.py
```

Then open your browser and go to:

```
http://localhost:5000
```

---

You’re now ready to use the Flask SEO Checker! 🚀
