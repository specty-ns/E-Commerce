# E-Commerce
To whomsoever it may concern,
to run this project you need to create "Virtual Environment". Virtual Environment provides an isolation environment for python files.

The following steps will guide you to create Virtutal Environment and this code should be executed in cmd and directory will be the folder in which you stored this project.

Step 1 creating virtutal environment as myvenv: D:\Python\Django\Interview\Django case Study>python -m venv myvenv 
Step 2 activating virtual environment: (myvenv) D:\Python\Django\Interview\Django case Study>myvenv\Scripts\activate
Step 3 connect with database through XAMPP
Step 4 installing requirement files to run this project: (myvenv) D:\Python\Django\Interview\Django case Study>pip install -r requirements.txt
Step 5 run celery server : (myvenv) D:\Python\Django\Interview\Django case Study>celery -A project worker -l info -P eventlet
Step 6 run python server : (myvenv) D:\Python\Django\Interview\Django case Study>python manage.py runserver


The above mentioned requirements.txt file is already provided with project.

After following the above given steps, you are good to go and can run this astonishing project.
