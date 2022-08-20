from flask import Flask

app = Flask(__name__, static_folder='static')

# Startapp
from projekt import routes
