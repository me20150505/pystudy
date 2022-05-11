import os;
import json;

import requests;
from plotly.graph_objs import Bar;
from plotly import offline;

url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars';
limit_url = 'https://api.github.com/rate_limit';
headers = {'Accept': 'application/vnd.github.v3+json'};

req = requests.get(url, headers=headers);
# print('status code: ', req.status_code);
res = req.json();
with open(os.path.join(os.path.dirname(__file__), './result/res_github.json'), 'w') as f:
    json.dump(res, f, indent=4);

repo_datas = res['items'];
repo_names, stars, labels = [], [], [];
for i in repo_datas:
    repo_names.append(f"<a target='_blank' href='{i['html_url']}'>{i['name']}</a>");
    stars.append(i['stargazers_count']);
    labels.append(f"{i['owner']['login']}<br />{i['description']}");

vis_data = [{
    'type': 'bar', 
    'x': repo_names, 
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(128, 0, 128)',
        'line': {
            'width': 1.5,
            'color': 'rgb(30, 30, 30)'
        }
    },
    'opacity': 0.6
}];
vis_layout = {
    'title': 'Github Popular Javascript Project',
    'titlefont': {
        'size': 24
    },
    'xaxis': {
        'title': 'Reponsitory',
        'titlefont': {
            'size': 20
        },
        'tickfont': {
            'size': 16
        }
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {
            'size': 20
        },
        'tickfont': {
            'size': 16
        }
    }
};
fig = {'data': vis_data, 'layout': vis_layout};
offline.plot(fig, filename=os.path.join(os.path.dirname(__file__), './result/github_stars.html'));