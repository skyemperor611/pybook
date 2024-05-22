from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd05c0c5d17c45ca1c4d70332b3f56583'

from appmain.routes import main
app.register_blueprint(main)

from appmain.user.routes import user
app.register_blueprint(user)