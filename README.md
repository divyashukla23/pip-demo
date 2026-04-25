# 🚀 Python + pip Project Demo (Beginner Friendly | DevOps Focus)

This guide will help you create, manage dependencies, and run a simple Python application using **pip**.

---

# 🧰 Prerequisites

Make sure you have:

### ✅ Check installations

```bash
python3 --version
pip3 --version
```

If not installed:

* Install Python from https://www.python.org
* pip comes with Python

---

# 📁 Step 1: Create Project Folder

```bash
mkdir my-python-app
cd my-python-app
```

---

# 🧠 Step 2: Create Virtual Environment (VERY IMPORTANT)

👉 Why?

* Keeps dependencies isolated
* Avoids conflicts between projects
* Used in real DevOps pipelines

```bash
python3 -m venv venv
```

---

## Activate environment

### Mac/Linux:

```bash
source venv/bin/activate
```

### Windows:

```bash
venv\Scripts\activate
```

👉 You will see `(venv)` in terminal

---

# 📦 Step 3: Install Dependency

Example: install Flask

```bash
pip install flask
```

---

# ✍️ Step 4: Create Application

Create file:

```bash
touch app.py
```

Add code:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python + pip!"

if __name__ == "__main__":
    app.run(port=5000)
```

---

# ▶️ Step 5: Run Application

```bash
python app.py
```

👉 Open browser:

```text
http://localhost:5000
```

👉 Output:

```text
Hello from Python + pip!
```

---

# 📄 Step 6: Dependency Management
## Save dependencies

```bash
pip freeze > requirements.txt
```

👉 Creates:

```text
requirements.txt
```

---

## Install dependencies later

```bash
pip install -r requirements.txt
```

👉 This is used in:

* CI/CD pipelines
* Production deployments



# 🔁 Step 10: Lifecycle (Simple)

```text
install → develop → package → deploy
```

---

# 🧠 DevOps Connection (IMPORTANT)

👉 Real flow:

```text
Developer writes code
↓
pip installs dependencies
↓
requirements.txt used in pipeline
↓
App deployed in server/container
```

---

## Used in tools like:

* Jenkins
* Docker

---


# 🎯 What You Learned

* What is pip
* What is virtual environment
* How to install dependencies
* How to run Python app
* What is requirements.txt
* Python packaging basics

---

# 🚀 Summary

👉 pip manages Python dependencies and helps prepare apps for deployment

---
