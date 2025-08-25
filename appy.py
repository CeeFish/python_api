from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

PROJECTS = [
  {"name": "my_portfolio", "html_url": "https://github.com/CeeFish/my_portfolio", "description": "Ruby on Rails, Python, and Bootstrap"},
]

@app.route('/projects')
def get_projects():
    DEFAULT_FEATURED = 'my_portfolio'

    featured = request.args.get('featured', DEFAULT_FEATURED)
    featured_lower = featured.lower()

    limit = request.args.get('limit', 1, type=int)

    filtered = [
        p for p in PROJECTS
        if p['name'].lower() == featured_lower
    ]

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