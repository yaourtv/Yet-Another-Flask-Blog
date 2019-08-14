# Yet Another Flask Blog
This is a simple Flask application, made using Flask libraries and a 
[YouTube guide by Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
<br><br>TL; DWatch microblog with simple functionality (User and post CRUD, email sender and something I forgot to mention).
## Requirements and Setting-Up
('cuz everyone wanna try to run it, huh?)
#### Libraries:
1. Flask (wow, such unexpected, much confusing)
2. flask_sqlachemy
3. flask_bcrypt
4. flask_login
5. flask_mail
6. flask_wtf
7. wtforms (isn't it installed with flask_wtf?)
8. pillow
9. Everything that would appear in error messages when you'll run `python run.py`


Python 3.x.x<br>
Environment variables `EMAIL_USERNAME` and `EMAIL_PASSWORD` (could be changed in [\_\_init__.py](/flaskproj/__init__.py) file).
