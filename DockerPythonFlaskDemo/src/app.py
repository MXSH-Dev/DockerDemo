import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return('Hey, we have Kibana on the right!!!')

if __name__ == '__main__':
    print(f'This server is running on port: {os.environ["PORT"]}')
    app.run(debug=True, host='0.0.0.0', port=os.environ["PORT"])