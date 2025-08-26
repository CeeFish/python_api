from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

allowed_origins = os.getenv('ALLOWED_ORIGINS', '').split(',')

# CORS for Rails frontend only
CORS(app, origins=allowed_origins)

PROJECTS = [
    {
        "name": "my_portfolio",
        "html_url": "https://github.com/CeeFish/my_portfolio",
        "description": "Backend engineer blending creative design with secure architecture"
    },
]

@app.route('/projects')
def get_projects():
    default_featured = 'my_portfolio'
    featured = request.args.get('featured', default_featured).lower()
    limit = request.args.get('limit', 1, type=int)

    filtered = [p for p in PROJECTS if p['name'].lower() == featured]
    return jsonify(filtered[:limit]), 200


# This is used when showing all public projects on the portfolio page
    # GITHUB_USERNAME = "CeeFish"

    # @app.route("/projects")
    # def get_projects():
    #     raw = requests.get(f"https://api.github.com/users/{GITHUB_USERNAME}/repos").json()
    # @app.route("/projects")
    # def get_projects():
    #     url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    #     response = requests.get(url)
    #     repos = response.json()

    #     projects = []
    #     for repo in repos:
    #         if not repo.get("fork"):  # Skip forks
    #             projects.append({
    #                 "name": repo["name"],
    #                 "description": repo["description"] or "No description provided.",
    #                 "language": repo["language"],
    #                 "stars": repo["stargazers_count"],
    #                 "updated_at": repo["updated_at"],
    #                 "html_url": repo["html_url"]
    #             })

    #     return jsonify(projects)

if __name__ == "__main__":
    app.run(debug=True)