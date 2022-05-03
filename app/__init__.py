from flask import Flask
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()



app = Flask(__name__)




 # Initializing flask extensions
bootstrap.init_app(app)