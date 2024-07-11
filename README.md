# MyPortfolio Website

This is a simple portfolio website template build with Django. It's fully mobile responsive and it have nice parallax effect.
All information like your name, email, experience, about me, images and more are dynamically generated from database.

## Setting up

Install all required dependencies:
```commandline
pip install -r requirements.txt
```
Next step is to make migrations (Linux is `python3` on Windows it's `python`):
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```
Now you need to create a superuser account that will allow you to easily populate database:
```commandline
python manage.py createsuperuser
```
After that you can run a website on a localhost with this command:
```commandline
python manage.py runserver
```
After those steps go to http://127.0.0.1:8000/admin, there you need to log in with your superuser credentials. In order to start the 
website you need to add a user in BACKEND **Users** table. There are needed 2 pictures and 2 logo images (maybe 2 same ones)
it's **important** to check `is_active` checkbox because that's how the user that's about to be displayed found. Thanks to
`is_active` field you can create multiple users and check which one will suite you best.
Another table that you will need to fill is **Projects** (it's possible to run website without it).

When it's all done you can go to http://127.0.0.1:8000 to see the website. 



