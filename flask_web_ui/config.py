import os           # If you need to use OS environment variables

class Config:
    SECRET_KEY = 'b319157f1a11c07c0160d3f940ba2a87'
    #SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'mysql://philipsqladmin:Integra827@philipmysql.mysql.database.azure.com/flaskdb'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'paw.flask.blog@gmail.com'
    MAIL_PASSWORD = 'Integra827'