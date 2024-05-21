# Project imports
from index import app

@app.get('/')
def index():
    return 'It\'s running'