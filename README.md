This is a Python API for my portfolio project.

This microservice powers the dynamic **Projects** section of my hybrid [Rails/Python portfolio](.....). Built with Flask, it serves structured JSON data to the frontend via API calls.

Some of the features included: 
- RESTful endpoint for project data
- CORS-enabled for cross-origin requests
- Environment-based configuration
- Secure deployment-ready setup

The tech stack used:
- Python 3.11+
- Flask
- Gunicorn (for production)
- dotenv
- Render (deployment)

How to Setup and Use this repo:
bash
git clone https://github.com/CeeFish/python_api.git
cd python_api
python -m venv venv
source venv/bin/activate or venv\Scripts\activate (Windows)
pip install -r requirements.txt
cp .env.example .env
flask run
