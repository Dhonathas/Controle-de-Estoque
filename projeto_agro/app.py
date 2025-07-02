from flask import Flask, send_from_directory
from flask_cors import CORS
from database import db
from controllers.item_controller import item_bp
import os

def create_app():
    app = Flask(__name__, static_folder='view', template_folder='view')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        app.register_blueprint(item_bp)

    @app.route('/')
    def index():
        return send_from_directory('view', 'index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
