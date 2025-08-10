from flask import Flask
from flask_cors import CORS
from api.run_code import run_code_bp

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173"])
    app.register_blueprint(run_code_bp, url_prefix='/api')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=4000, debug=True)
