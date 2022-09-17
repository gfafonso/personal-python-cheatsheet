# -*- coding: iso-8859-15 -*-
#qwoijdqwoifefwefwef
import importlib
import re
import json
import os
import requests
from os import listdir
from os.path import isfile, join

LAST_FILE = 'hyper/prod/ci-prod/us-west-2/dms/certificate'
env_file = os.getenv('GITHUB_ENV')


# FILES = list(os.getenv('FILES'))


def main():
    with open('paths.py', "a+") as myfile:
        import paths

        # Needed because of exporting variables
        G = pygraphviz.AGraph()
        G.read("graph.dot")
        adj = []
        for n in G.nodes():
            row = {'name': re.sub(r'.+CEG-IaC-Live-AWS/', '', n),
                   'value': sum([G.has_edge(n, tn) * 1 for tn in G.nodes()])}  # CREATE MATRIX WITH SINGLE
            # VALUES
            adj.append(row)
        json_matrix = json.loads(json.dumps(adj))
        print(json_matrix)
        new_list = sorted(json_matrix, key=lambda json_matrix: json_matrix['value'])  # SORT BY VALUE
        # ARRAY ORDER
        filtered = new_list
        # print(ordered)
        # print(filtered)

        filtered.append({'name': LAST_FILE, 'value': 1000})
        try:
            myfile.truncate(0)
            myfile.write(f"FILES={paths.FILES + new_list}\n")
        except AttributeError:
            myfile.write(f"FILES={new_list}\n")
    importlib.reload(paths)
    print(paths.FILES)


def export():
    import paths
    ordered = [li["name"] for li in paths.FILES]
    final = []
    for x in ordered:
        # check if exists in unique_list or not
        if x not in final:
            final.append({'name': x, 'log': re.sub(r'.+/', '', x)})
    print(final)


def clean():
    from pathlib import Path
    p = Path("/Users/guilhermeafonso/PycharmProjects/pythonProject/.github/paths.py")
    path = p.parent.absolute()
    print(path)
    file = Path(str(path) + "/fine_me.txt")
    print(file)
    if os.path.isfile(file):
        print("\nIt is a normal file")


def join():
    l = []
    f = open('graph.dot', 'r')
    file_contents = f.read()
    l.append(file_contents)
    f.close()
    with open('paths.py', "a+") as my_file:
        import paths
        d = [{'digraph': l[0], 'file': LAST_FILE}]
        try:
            my_file.truncate(0)
            my_file.write(f"DEPENDENCIES={paths.DEPENDENCIES + d}")
        except AttributeError:
            my_file.write(f"DEPENDENCIES={d}")
    importlib.reload(paths)
    print(paths.DEPENDENCIES)


def runners():
    path = ".github/work/1/33"
    urls = "https://github.com/ConvaTec/GEM-in-market-data-feeds,https://github.com/ConvaTec/CEG-IaC-Live-AWS"
    names = "1,2"
    onlyfiles = [f for f in listdir(".github")]
    files = []
    labels = ""
    levels = path.split('/')
    current = levels[0]
    for i, p in enumerate(levels, start=0):
        if not i == 0:
            current += "/" + p
        files += [f for f in listdir(current)]
        if 'env.hcl' in files:
            f = open(f"{current}/env.hcl", "r")
            for x in f:
                if x.strip().startswith("environment"):
                    labels += x.split("\"")[1]
            break
    print(path.split('/'))
    f = open(f"{path.split('/')[0]}/project.hcl", "r")
    for x in f:
        if x.strip().startswith("codename"):
            labels += "," + x.split("\"")[1]

    url_array = urls.split(',')
    names_array = names.split(',')

    containers = []
    for index, i in enumerate(url_array, start=0):
        url = i.strip()
        repo = url.rsplit('/', 2)
        print(repo)
        token = "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"
        api_url = f"https://api.github.com/repos/{repo[1]}/{repo[2]}/actions/runners/registration-token"
        headers = {"Authorization": f"token {token}"}
        response = requests.post(api_url, headers=headers)
        result = response.json()
        print(api_url)
        img = {
            "image": "${DOCKER-IMG}",
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-group": "${cloudwatch_group}",
                    "awslogs-region": "${region}",
                    "awslogs-stream-prefix": "ecs"
                }
            }
        }
        env = [
            {
                "name": "REPO_URL",
                "value": f"{url}"
            },
            {
                "name": "RUNNER_TOKEN",
                "value": result['token']
            },
            {
                "name": "LABELS",
                "value": labels
            }
        ]
        print(index)
        img['environment'] = env
        img['name'] = names_array[index].strip()
        containers.append(img)

    with open(f'{path}/container.json', 'w') as outfile:
        json.dump(containers, outfile)

    print(path + "/ecs-task-service")


def format_output():
    from cProfile import run
    import sys
    import os
    import base64

    # This script will format arg[1] text to a valid markdown language
    # [INPUT] : arg1 -- html file
    # [OUTPUT] : will be written to the same file or new one incase of error

    # GET CONTENT FROM FILE
    with open('show-plan-2.log', 'r') as myfile:
        data = myfile.readlines()
    print(data)
    finalstring = ''
    flag = False
    for s in data:
        # Filter info
        if ('Terraform will perform the following actions:' in s) or ('Error:' in s) or ('No changes' in s):
            flag = True
        elif ('????????????????' in s):
            flag = False

        if (flag):
            finalstring += s

    # OUTPUT ENCODING TO BASE64
    message_bytes = finalstring.encode('utf-8')
    base64_bytes = str(base64.b64encode(message_bytes))[2:-1]  # remove b' '

    # OUTPUT FILE: [output-planfile]
    with open('summary.log', 'w') as myfile:
        myfile.write(finalstring)

# -------------------------------------- GITHUB RELATED ---------------------------------- # 

def parse():
    variable = "PM: @project\r\nUsers: @user1, @user2\r\nProject description:\r\n"
    x = re.findall(r"PM:(.*)", variable)
    y = re.findall(r'Users:(.*)', variable)
    a = re.sub('\r', '', x[0]).strip()
    b = re.sub('\r', '', y[0]).strip().split(',')
    users = []
    for i in b:
        users.append(re.sub('@', '', i.strip()))
    print(a)
    print({'pm': re.sub('@', '', a), 'users': users})



def create_project():
    api_url = "https://api.github.com/orgs/CEG-GUI-Sandbox/projects"
    headers = {"Authorization": "token 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",
               "Accept": "application/vnd.github.v3+json"}
    my_project = {"name":title}
    response = requests.post(api_url, headers=headers, data=json.dumps(my_project))
    result = response.json()
    return result['id']

def create_team():
    api_url = "https://api.github.com/orgs/CEG-GUI-Sandbox/teams"
    headers = {"Authorization": "token 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",
               "Accept": "application/vnd.github.v3+json"}
    my_team = {"name": title+"-TEAM", "permission": "push",
             "privacy": "secret"}
    requests.post(api_url, headers=headers, data=json.dumps(my_team))

def add_project_to_team(project_id):
    api_url = f"https://api.github.com/orgs/CEG-GUI-Sandbox/teams/{title}-TEAM/projects/{project_id}"
    headers = {"Authorization": "token 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",
               "Accept": "application/vnd.github.v3+json"}
    response = requests.put(api_url, headers=headers)
    
    if response.status_code == 404:
        raise Exception(f"Could not add {title}-TEAM to {title}")


if __name__ == "__main__":
    # main()
    # join()
    # runners()
    # format_output()
    # parse()
    #use
    m = ['gfafonso']
    project_id = ''
    team_id = ''
    title = 'test-py4'
    create_team()
    id = create_project()
    add_project_to_team(id)
