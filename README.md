# test-upTrader
git clone 
cd test-upTrader
pip install virtualenv
python -m venv venv
venv\Scripts\activate (for windows os)
pip install -r requirements.txt
cd app
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
