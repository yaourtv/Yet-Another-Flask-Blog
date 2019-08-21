import os

class Config:

	SECRET_KEY = 'f5636f0074bfa87953403c43b8c17701'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
