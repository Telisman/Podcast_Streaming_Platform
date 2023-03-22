# Django Podcast Platform

This Django-based podcast streaming platform allows users to stream and upload podcasts. Users can also create a blog, write posts, and leave comments. The project has several apps, including basic_pages, podcast, podcast_blog, and podcast_user. This is still in the development phase.

## Getting Started
To run this project on your local machine, follow the instructions below:

## Prerequisites
You need to have the following software installed on your machine:

```bash
Django
Python 3
```

## Installing
Clone this repository using Git:

```bash
https://github.com/Telisman/Podcast_Streaming_Platform.git
```
Next, install the necessary dependencies by creating a virtual environment, activating it, and running ***pip install -r requirements.txt.***

After installing the dependencies, run the following commands to set up the database and create a superuser:
```bash
python manage.py migrate
python manage.py createsuperuser
```
You can then start the development server by running python manage.py runserver.

## Apps
### basic_pages
This app contains the basic pages of the website, including the home page, about page, and contact page.

### podcast
This app is responsible for the live streaming of podcasts. Users can upload podcasts, view them, and leave comments. An API token is created for every new user registered.

### podcast_blog
This app allows users to create a blog, write posts, and leave comments. Users can also edit and delete their posts and comments using the API.

### podcast_user
This app handles user authentication and user settings. Users can edit their profiles, change their passwords, and view their API tokens. After login, users must use their API token to access their user info and settings.

### Media and Static Files
The project's media files are stored in the media directory, while the static files are stored in the static directory. You should configure your web server to serve these directories.

### Like and Unlike Option
Users can like and unlike podcasts and blog posts by clicking on the like icon.

## API endpoint 
Endpoints are created in serializers_urls.py for podcast_user and podcast_blog.
The following endpoints are available in the API:
```bash
/api_user/

GET /api_user/users/ - Returns a list of all users.
GET /api_user/users/<int:pk>/- Returns a specific user.
GET /api_user/countries/ - Returns a list of countries.
GET /api_user/countries/<int:pk>/- Returns a specific countrie.
GET /api_user/user-info/ - Returns a list of all users user-info.
GET /api_user/user-info/<int:pk>/- Returns a specific user user-info.
POST /api_user/register/ -Registers a new user and returns their API token.
POST /api_user/login/ -Logs in a user and returns their API token.
PUT /api_user/edit/<int:pk>/ - Updates a specific user.
DELETE /api_user/delete//<int:pk> - Deletes a specific user.


/api_blog/
GET /api_blog/blogs - Returns a list of all blog posts.
GET /api_blog/blogs/<int:pk>/ - Returns a specific blog post.
GET /api_blog/comments - Returns a list of all blog comments.
GET /api_blog/comments/<int:pk>/ - Returns a specific blog comments.
PUT /api_blog/blog/edit/<int:pk>/ - Updates a specific blog post.
PUT /api_blog/comment/edit/<int:pk>/ - Updates a specific blog comments.
DELETE /api_blog/blog/delete/<int:pk>/ - Deletes a specific blog post.
DELETE /api_blog/comment/delete/<int:pk>/ - Deletes a specific blog post.
```
Looks of podcast_graph  schemes in neo4j app
![podcast_graph](https://user-images.githubusercontent.com/23407190/225301971-dbfb625f-b163-4756-ab59-ff4e36d6abce.png)
