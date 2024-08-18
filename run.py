from waitress import serve
from qhtan import app

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
