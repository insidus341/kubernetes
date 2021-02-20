from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/docker-webhook/05b6053c41a2130afd6fc3b158bda4e6', methods=['POST', 'GET'])
def respond():
    print(json.dumps(request.json))

    try:
        j = request.json

        if "repository" in j:
            if "repo_name" in j['repository']:
                repo_name = j['repository']
                print(repo_name)
    
    except Exception as e:
        print(e)

    return Response(status=200)

app.run(host='0.0.0.0', port=9000)
