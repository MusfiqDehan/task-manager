<div align="center">
<h1>Task Manager</h1>
A Python-Django Task Manager Project with REST API 
<br>
<br>
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green">
<h3>Project's Short Demo</h3>

https://github.com/MusfiqDehan/task-manager/assets/47440165/7219a3f5-e809-4182-8478-ec85f105a210

For more detail overview visit this link: https://youtu.be/4XTaPGTVto0

</div>

## Table of Contents

-   [Easy Login Info](#easy-login-info)
-   [Technology Used](#technology-used)
-   [Added Features](#added-features)
-   [How to Run Locally](#how-to-run-locally)
    -   [Clone from GitHub](#clone-from-github)
    -   [Setup PostgreSQL Database](#setup-postgresql-database)
    -   [Import Data from db.json](#import-data-from-dbjson)
    -   [Admin Panel](#admin-panel)
-   [API Details](#api-details)

## Technology Used

-   **Frontend:** HTML5, CSS3, Bootstrap5, JavaScript
-   **Backend:** Python=3.11.4, Django=4.2.5
-   **Database:** PostgreSQL, (Hosted on Render for Production)
-   **Static and Media Upload:** AWS S3 Bucket using Cloudflare R2
-   **API:** Django-REST-Framework
-   **Version Control:** Git, GitHub
-   **Editor:** VS Code
-   **Operating System:** Ubuntu 23.04 LTS
-   **Browser(Tested On):** Google Chrome, Microsoft Edge, Mozilla Firefox

[⬆️**Go to Table of Contents**](#table-of-contents)

## How to Run Locally

### Clone from GitHub

-   Install Python3
-   Install pip

```bash
sudo apt install python3-pip
```

-   Clone the repository

```bash
git clone https://github.com/MusfiqDehan/task-manager.git
```

-   Go to the project directory

```bash
cd task-manager
```

-   Create a virtual environment

```bash
python3 -m venv venv
```

-   Activate the virtual environment

```bash
source venv/bin/activate
```

-   Install the dependencies

```bash
pip3 install -r requirements.txt
```

-   Run the server

```bash
python manage.py runserver
```

-   Open the browser and go to http://127.0.0.1:8000/

-   To deactivate the virtual environment

```bash
deactivate
```

[⬆️**Go to Table of Contents**](#table-of-contents)

### Setup PostgreSQL Database

-   Install PostgreSQL

```bash
sudo apt install postgresql postgresql-contrib
```

-   Login to PostgreSQL

```bash
sudo -u postgres psql
```

-   Create a database

```bash
CREATE DATABASE task_manager;
```

-   Create a user

```bash

CREATE USER task_manager_user WITH PASSWORD 'task_manager_password';
```

-   Grant privileges to the user

```bash
GRANT ALL PRIVILEGES ON DATABASE task_manager TO task_manager_user;
```

-   Exit from PostgreSQL

```bash
\q
```

-   Open the `settings.py` file from `task_manager` directory

-   Create a file named `.env` in the `task_manager` directory and add the following lines

```bash
SECRET_KEY=your_secret_key
DEBUG=False
DB_ENGINE=django.db.backends.postgresql
DB_NAME=task_manager
DB_USER=task_manager_user
DB_PASSWORD=task_manager_password
DB_HOST=localhost
DB_PORT=5432
```

See the `.env.example` file for reference.

[⬆️**Go to Table of Contents**](#table-of-contents)

### Import Data from db.json

-   You will find a file named `db.json` in the root directory

-   Run the following command to import data from `db.json`

```bash
python3 manage.py loaddata db.json
```

-   Migrate Database

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

[⬆️**Go to Table of Contents**](#table-of-contents)

### Admin Panel

-   Run the server

```bash
python manage.py runserver
```

-   Open the browser and go to http://127.0.0.1:8000/

-   To access the admin panel, go to http://127.0.0.1:8000/admin/

-   Login with the following credentials:

    -   Username: `admin`
    -   Password: `admin`

-   If these credentials don't work, you can create a superuser by running the following command:

```bash
python manage.py createsuperuser
```

-   Enter the username, email, and password

-   Now you can access the admin panel with the credentials you have just created

[⬆️**Go to Table of Contents**](#table-of-contents)

## API Details

-   **Endpoint:** http://127.0.0.1:8000/tasks/api/v1/tasks
-   **Method:** GET
-   **Description:**
    -   Returns all the tasks
-   **Endpoint:** http://127.0.0.1:8000/tasks/api/v1/tasks/1
-   **Method:** GET, PUT, PATCH, DELETE
-   **Description:**
    -   Returns a single task
    -   Updates a single task
    -   Partially updates a single task
    -   Deletes a single task

[⬆️**Go to Table of Contents**](#table-of-contents)
