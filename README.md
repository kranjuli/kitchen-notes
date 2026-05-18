# Kitchen Notes 🍽️

A simple personal recipe web application built with Flask and Jinja2.

The goal of this project is to manage and display cooking recipes in a clean, minimal web interface using JSON files as a lightweight data source.

---

## 🚀 Features

- 📖 List all recipes on the homepage
- 🍲 View detailed recipe pages
- 🗂️ Recipes stored as individual JSON files
- 🎨 Simple, responsive UI (Jinja2 templates + CSS)
- ⚡ Lightweight Flask backend

---

## 🧱 Tech Stack

- Python 3.14+
- Flask
- Jinja2
- JSON (file-based storage)
- uv (dependency management)

---

## 📁 Project Structure

see `src/kitchen_notes`

---

## ⚙️ Run applaction

### 1. Clone repository

```bash
git clone git@github.com:kranjuli/kitchen-notes.git

cd kitchen-notes

# pull dockerfile uv and python
docker pull ghcr.io/astral-sh/uv:0.11.14-python3.14-trixie@sha256:ce5c2af593c72eedbfd70bf243861bc12e161959dd73e79dd2b807e81e0badf4

docker tag ghcr.io/astral-sh/uv:0.11.14-python3.14-trixie@sha256:ce5c2af593c72eedbfd70bf243861bc12e161959dd73e79dd2b807e81e0badf4 uv-python

```

### 2. Run the app

manually

```bash
docker run -it --rm -p 5000:5000 -v "$(pwd)":/app -w /app -e UV_PROJECT_ENVIRONMENT=/opt/venv -e PATH="/opt/venv/bin:$PATH" -e PYTHONPATH="/app/src" uv-python:latest bash
# run app with debug mode
uv run flask --app kitchen_notes:create_app run --debug --host=0.0.0.0 --port=5001

# without debugging
uv run flask --app kitchen_notes:create_app run --host=0.0.0.0 --port=5001
```

one step with bash script `run-local.sh`

```bash
./run-local.sh

# you can run docker logs uv-python to see app log
docker logs -f kitchen-notes
```

### 3. Open in Browser

```bash
http://<your_host>:5001
```
---

## 🍽️ Adding recipes

Each recipe is stored as a JSON file in:

```bash
kitnotes/
```

### Install/Update dependencies in pyproject.toml oder uv.lock

Using `uv`:

```bash
docker run -it --rm -p 5000:5000 -v "$(pwd)":/app -w /app -e UV_PROJECT_ENVIRONMENT=/opt/venv -e PATH="/opt/venv/bin:$PATH" -e PYTHONPATH="/app/src" uv-python:latest bash

# activate venv and install current packages
uv sync

# install new dependency
uv add <dependency>
# i.e. uv add jinja2

# check your pyproject.toml and uv.lock if package added
```

---

## Linting with Ruff

```bash
# run docker
docker run -it --rm -p 5000:5000 -v "$(pwd)":/app -w /app -e UV_PROJECT_ENVIRONMENT=/opt/venv -e PATH="/opt/venv/bin:$PATH" -e PYTHONPATH="/app/src" uv-python:latest bash

# activate venv
uv sync

# install ruff package if does not exist
uv add --dev ruff

# checking with ruff
uv run ruff check .

# checking and fix with ruff
uv run ruff check . --fix

# format check with ruff
uv run ruff format .
```

---

## Bash script to run app for development

see `run-local.sh`

```bash
# Run the script to pull the dockerfile and build the app container
./run-local.sh

# run docker logs to see the app log
docker logs -f kitchen-notes
```

---

## 🛠️ Development Notes

- Ensure `kitnotes/` folder exists before running the app
- Use debug=True for automatic reload during development
- Flask static files are served from `src/kitchen_notes/static/`
