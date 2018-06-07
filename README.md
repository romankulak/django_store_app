# Banner-Creator
### *Web service for creating promo-banners*



# Run with vagga
1. Clone the project `git clone https://gitlab.uaprom/bigl/banner-creator.git`
2. Configure port forwarding: 11900 to 5000

    >if you use vagga-box configure in virtual box app: network > Advanced > Port Forwarding
3. ```vagga run``` -starts application on port 11900 

    >your app should be available on http://127.0.0.1:5000/
3. ```vagga test``` -runs tests

4. ```vagga webpack -w``` -run webpack watch

#####Uploading files

*To upload files use `dev.py` config instead of `production.py`* :

   >CUR_DIR = os.path.abspath(os.path.dirname(__file__))
   
   >BASE_DIR = os.path.abspath(os.path.dirname(CUR_DIR))
   
   >STORAGE_DIR = os.path.join(BASE_DIR, 'media')
   
   >UPLOAD_FOLDER = os.path.join(STORAGE_DIR)
   
   >FONT_FOLDER = UPLOAD_FOLDER


*If you want to use local database, 
you should provide appropriate info in `instance/config.py`* Example:

   >SECRET_KEY = 'supersecretstring'
    
   >SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@host/database'
    
   >SQLALCHEMY_TEST_DATABASE_URI = 'postgresql+psycopg2://user:password@host/test_database'




# Installing Locally
*( The option without vagga )*
1. Clone the project `git clone https://gitlab.uaprom/bigl/banner-creator.git`
2. Setup requirements using your virtualenv `pip install -r requirements.txt` 
3. Apply DB migrations `python manage.py db upgrade`
4. Create `media/` folder in directory `server/`
5. Create `instance/config.py` **in your repository root directory** and populate it with configs. Example:

    >SECRET_KEY = 'supersecretstring'
    
    >SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@host/database'
    
    >SQLALCHEMY_TEST_DATABASE_URI = 'postgresql+psycopg2://user:password@host/test_database'`
    
Now try to run dev server `python manage.py runserver`

## Database migrations
- Use `python manage.py db migrate` to create a new migrations file
- Use `python manage.py db upgrade` to apply changes to your database

## Tests
- Use `python manage.py test` to run all the tests

======
## How to build front-end in repo:

1. Open terminal: and input
```
npm install
```
this will install all used packages.
2. Then input
```
npm run watch
```
 or
```
npm run webpack
```
to run webpack in auto mode

### How to minimize and uglify js\css
```
npm run prod
```

## Client side structure
1. Styles sources stored in stylus file in /client/css
2. JS sources stored in /client/js
3. Don't forget to add new js code in separate files and require them into app.js
