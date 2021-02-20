from flask import Flask, request, Response
import json
import pprint
import subprocess
import sys
import os

DIR = "/home/james/kubernetes/"
app = Flask(__name__)

@app.route('/docker-webhook/05b6053c41a2130afd6fc3b158bda4e6', methods=['POST', 'GET'])
def respond():
    print(json.dumps(request.json))

    try:
        j = request.get_json(silent=True)

        if "repository" in j:
            if "repo_name" in j['repository']:
                repo_name = j['repository']['repo_name']
                
                if repo_name == "insidus341/nginx-test":
                    redeploy()
    
    except Exception as e:
        print(e)

    return Response(status=200)

def redeploy():
    hosts = DIR + "ansible/kube-cluster/hosts/hosts"
    print(hosts)
    playbook = DIR + "ansible/kube-cluster/playbooks/monitoring/check-kube-cluster-health.yml"
    print(playbook)

    cmd = ["ansible-playbook",
           "-i {},".format(hosts),
           playbook,
           "-e 'ansible_password=$ANSIBLE_PASSWORD'"
           ]

    proc = subprocess.Popen(cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            )

    outs, errs = proc.communicate(timeout=15)
    pprint.pprint(outs.decode().split('\n'))


if __name__ == "__main__":
    
    redeploy()
    # app.run(host='0.0.0.0', port=9000)