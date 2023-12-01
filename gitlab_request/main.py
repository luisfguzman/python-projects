import requests

response = requests.get("https://gitlab.com/api/v4/users/foundryvault/projects")

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}")
    print(f"Project URL: {project['web_url']}\n")