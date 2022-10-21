from flask import Flask

app = Flask(__name__, static_folder='assets')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3307/BankRespublika'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
app.config['SECRET_KEY']='my_project'
from controllers import *
from models import *    
from extensions import *
    

if __name__ == "__main__":
    db.init_app(app)
    migrate.init_app(app)
    app.run(port=5000,debug=True)




