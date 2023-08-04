"# oracle_db" 

1. For running this script you need to have running connection
with Oracle DB on your laptop with usuall user (NOT sys or other)
with all permissions
2. From OracleSQL Developer (or other program) you need get info about:
- DB name
- PORT (usuall 1521)
- user name
- password
and replace it in oracle_db/oracle_db/settings.py in next block
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.oracle',
        'NAME':     'test80',
        'USER':     'C##test80',
        'PASSWORD': '111',
        'PORT': '1521',
        
    }
}
3. You need have Python 3.11 on your laptop
(modules for it you find in requirments.txt)

4. To manually run script loading data into DB, you should 
place next .csv and .txt files in directory '.static':

tax.txt
business_areas.csv
companies.csv
items.csv

and run in main directory (oracle_db with manage.py)
next command:

python manage.py write_data

4. To run whole project in main directory 
(oracle_db with manage.py) next command:

python manage.py runserver

5. Admin panel you can reach at address
http://127.0.0.1:8000/admin
user: admin
password: admin

6. Frontend show only items marked as 'in_market' 
or 'is_active', so be careful with this flag, but it
always could be changed in admin panel (see above)

7. Tax values could be easily changed in tax.txt file

8. If case not logged strait:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
(admin - email - admin x 2 - y)


