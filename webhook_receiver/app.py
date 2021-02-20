from flask import Flask, request, Response

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/docker-webhook/05b6053c41a2130afd6fc3b158bda4e6', methods=['POST', 'GET'])
def respond():
    print(request.json);
    return Response(status=200)

app.run(host='0.0.0.0', port=6666)