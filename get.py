from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def get_hello():
    return "Hello Word"

if __name__ == '__main__':
    app.run(debug=True)

# comentario para hacer un commit github-webhook/
