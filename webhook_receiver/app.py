from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/docker-webhook/05b6053c41a2130afd6fc3b158bda4e6', methods=['POST', 'GET'])
def respond():
    print(request.json);
    return Response(status=200)

app.run(host='jamesearl.co.uk', port=6666)