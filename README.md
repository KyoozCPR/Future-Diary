![Alt text](static/images/logo.png)


# Future Diary - Web App
this a web app built in Full Stack Django with SQL lite 

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python (version 3.6 or later)
- Git

## Cloning the Repository

1. Open your terminal (or Git Bash on Windows).
2. Clone the repository by running the following command:

   ```bash
   git clone https://github.com/KyoozCPR/Future-Diary.git
3. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
4. Before running the project, apply the database migrations:
   ```bash
   python manage.py migrate
5. And apply static files:
   ```bash
   python manage.py collectstatic
6. Start the Django development server by running:
   ```bash
   python manage.py runserver
Now you can view my website by entering this url : http://127.0.0.1:8000/


