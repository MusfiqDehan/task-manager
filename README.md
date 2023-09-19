<div align="center">
    <h1>Task Manager</h1>
    A Python-Django Task Manager Project with REST API 
    <br>
    <br>
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green">
</div>

## Table of Contents

-   [Easy Login Info](#easy-login-info)
-   [Technology Used](#technology-used)
-   [Added Features](#added-features)
-   [How to Run Locally](#how-to-run-locally)
    -   [From GitHub](#from-github)
-   [API Details](#api-details)

## Easy Login Info

To login as a user/admin, you can use the following credentials:

-   Username: `mrdehan`
-   Password: `54321.`

[⬆️**Go to Table of Contents**](#table-of-contents)

## Technology Used

-   **Frontend:** HTML5, CSS3, Bootstrap5, JavaScript
-   **Backend:** Python=3.11.4, Django=4.2.5
-   **Database:** PostgreSQL
-   **Deployment:** Render
-   **API:** Django-REST-Framework
-   **Version Control:** Git, GitHub
-   **Editor:** VS Code
-   **Operating System:** Ubuntu 23.04 LTS
-   **Browser(Tested On):** Google Chrome, Microsoft Edge, Mozilla Firefox

[⬆️**Go to Table of Contents**](#table-of-contents)

## How to Run Locally

### From GitHub

-   Install Python 3
-   Install pip

```bash
sudo apt install python3-pip
```

-   Clone the repository

```bash
git clone https://github.com/MusfiqDehan/amicodingparina.git
```

-   Go to the project directory

```bash
cd task-manager
```

-   Create a virtual environment

```bash
python3 -m venv venv
```

````
- Activate the virtual environment
```bash
source venv/bin/activate
````

````
- Install the dependencies
```bash
pip3 install -r requirements.txt
````

-   Run the server

```bash
python manage.py runserver 8080
```

-   Open the browser and go to http://127.0.0.1:8080/
-   To deactivate the virtual environment

```bash
deactivate
```

[⬆️**Go to Table of Contents**](#table-of-contents)

## API Details

-   **Endpoint:** http://127.0.0.1:8080/tasks/api/v1/tasks

[⬆️**Go to Table of Contents**](#table-of-contents)
