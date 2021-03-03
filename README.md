# ApiDRFSocialNetwork

### HOW TO
1. clone the project
2. activate venv & run the command "pip install -r requirements.txt"
3. python manage.py migrate

(use postman for test api)
- user signup - [POST] http://127.0.0.1:8000/api/user/sign-up/
- user login and take a token - [POST] http://127.0.0.1:8000/api/user/login/
- post creation - [POST] http://127.0.0.1:8000/api/post/
- post like - [POST] http://127.0.0.1:8000/api/post/1/like/
- post unlike - [POST] http://127.0.0.1:8000/api/post/1/unlike/
- user who is fan of post - [GET] http://127.0.0.1:8000/api/post/1/fans/
- analytics about how many likes was made - [GET] http://127.0.0.1:8000/api/likes/check-count/?date_from=2021-03-02&date_to=2021-03-05
- user was login last time - [GET] http://127.0.0.1:8000/api/user/last-login/
- user mades a last request to the service - [GET] http://127.0.0.1:8000/api/user/last-activity/
