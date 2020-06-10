# Team-International-Backend(Dead-line Friday 10:00 GMT)

Task given: Dockerized micro-service for showing a dashboard for logged in users

#Django will be used  as the main Framework


1--Fork the project to your github account
2--Clone the repository in your local environement

 2.1--Run this command :git remote add uppstream https://github.com/bensoftware/Team-International-Backend/edit/master/README.md

3--Need to install 
    3.1 django rest framework->pip install djangorestframework

4--Notice  the JSON file in the project root,this is the structure(Same structure than the attributes in the model) :

user_id(string);
user_first_name(string);
user_last_name(string);
user_gender(string);
user_address(string);
user_email(string);
user_image(string),
is_user_logged(boolean).


4--Integrate Swagger in the project;

5--Create your microservice API it has to read the JSON file and display
the outpout through the endpoint(/api/team-international/user/logged);

NOTE:It's the GET method;

6--Test your API if it displays data;

    In order to test in local

    1)python manage.py makemigrations ->creates migration files based on your models

    2)python manage.py migrate-> will create the tables in your db based on the migration files created

    3)python manage.py createsuperuser ->will create a superuser for your application in the database

    4)python manage.py runserver 

7--Document your API using SWAGGER;
7.1: If swagger is giving you a static file error please refer to this thread https://github.com/unioslo/mreg/issues/395

8--Create the txt file with your slack name for example @ben.Put your HNG-Board ID in the file.

9--Put instructions in the Dockerfile  located in the project's root,this  will allow you to create the image.This bellow link might help  you.
https://www.youtube.com/watch?v=KN8wuFi2RXM

10--Create your image using Dockerfile.

11--Use Docker command and Dockerfile to Create the container .

12-Run the container.

13--Run git add . (To add and upade files in the stagging area);

14--Commit your repository using :git commit -m "Microservice created"

16--Run git push origin master to push to your fork.For example (git push origin master  https://github.com/bensoftware/Team-International-Backend.git);

17--Create the pull request to the main repository ;in our case :https://github.com/hngi/Team-International-Backend.git.
