# Example Django App
### *Book Store*

# Installing Locally
- Python 3.6+ required

1. Clone the project `https://github.com/romankulak/django_store_app.git`
2. Setup requirements using virtualenv `pip install -r requirements.txt` 
3. Apply DB migrations `python manage.py db migrate`
4. Test `python manage.py test`
5. Load initial data from fixtures 
    * `python manage.py loaddata users.json`
    * `python manage.py loaddata books.json`
6. Run `python manage.py runserver`
7. Go to login page and login
 `http://127.0.0.1:8000/book_store/accounts/login/`
Username: `admin`
Password: `qwertyuyuiop`

## Manage commands

To display available books in DB use:
- `python manage.py display_books`

Options:
   * `--order` `asc` `desc`
   * `--limit` `100`

Example of Usage: 
`python manage.py display_books --order desc --limit 100`


