import requests

from plotly.graph_objs import bar
from plotly import offline

# make an API call and store the repose.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url)
response_dict = r.json()
print(f"total repositiories: {response_dict['total_count']}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner} <br>{description}"
    labels.append(label)

# Make visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'hovertext': labels,
    'maker': {
    'color': 'rgb(60,100,150)',
    'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': '0.6',
}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
