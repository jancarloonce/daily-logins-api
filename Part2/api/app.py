from flask import Flask, request
import configparser
from opensearch import Opensearch


app = Flask(__name__)
config = configparser.ConfigParser()
config.read("./configs/opensearch_config.ini")
conn = Opensearch(host=config['AWS']['host'],
                  basic_auth=config['AWS']['basic_auth'])


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users', methods=["GET"])
def returnUsers():
    user = request.args.get("user")
    if user:
        result = conn.filterUser(user)
        return result
    else:
        result = conn.getAllIndexData(conn.filterUser)
        return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
