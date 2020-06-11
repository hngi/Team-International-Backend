# Team-International-Backend(Dead-line Friday 10:00 GMT)


In this repo you will find the microservice with a REST API Integrated with Swagger for documentation purposes.
Below are the instructions on how to get this microservice up and running for testing or development purposes.


## Repository
1) Fork this repository, Clone it on your system.
Before running this please keep in mind you will need Swagger, Django, and REST API.
Run the following commands to install these plugins
`$ pip install django`
`$ pip install django-rest-swagger`
`$ pip install djangorestframework`

## Run the server
1) In your command prompt navigate to the original file directory where the manage.py script exists and run the following:
`$python manage.py runserver`

Now the server is up and running on your local host on http://127.0.0.1:8000/

#### For more testing purposes please refer to the following 

`$python manage.py makemigrations` ->creates migration files based on your models

`$python manage.py migrate`-> will create the tables in your db based on the migration files created

`$python manage.py createsuperuser` ->will create a superuser for your application in the database

3) You will now be greeted with our REST API that displays the current logged in users.

If you would like to navigate to swagger please go to http://127.0.0.1:8000/docs 


PLEASE NOTE: Swagger is currently facing problems with Django 3.0 or above, This problem is within the base swagger installation files on your local machine so there isn't really much we can do to fix it BUT we can always provide instructions :)
When trying to navigate to http://127.0.0.1:8000/docs you will be greeted with a static file error to fix it simply do the following: 

-Navigate to :

C:\Users\YOURNAME\AppData\Local\programs\python\python38\lib\site-packages\rest-framework-swagger\index.html

-Open the HTML file in any text editor and navigate to line 2 

-Change `{% load staticfiles %}` to `{% load static %}`

-Back in the terminal press Ctrl+C to stop the server and run the server again. 

And now Swagger will work, A ticket about this issue was open and answered by one of our team memebers here:

https://github.com/unioslo/mreg/issues/395


4)Do your changes or whatever part was assigned to you by the teamleads and Create a PR request !  


###  Dockerize the microservice 


1--Download and Install docker on your local machine,

2--Run the following  commands on your terminal(Linux) or command prompt(Windows)

3--Test if docker is well installed by using this command :`docker --version`(it should display the docker's version installed).
   
   NOTE:In the root project folder you will notice two files, `Dockerfile` and `Docker-compose.yml` files.
   
4--Run this command: `docker-compose up` (It will build the image and run it using instructions in Dockerfile and 
   Docker-compose.yml)  
   
   This action might take time because; all dependencies like Django RestApi,Swagger...has to be downloaded as well.    
   At the end of this process,The microservice will be running in the docker container and listenning to the port:8000
   (This port was configured in the  `Docker-compose.yml` file `[line-5]`)
   

####  Additional Information !

-When commiting changes please include your Slack ID in the commit message so we can reach you easily.

-When creating a PR make sure you are submitting the correct files !

-If you have access to the repo DO NOT merge your own PR ! Wait for us to compare and run our test and then we will merge. 

-The JSON file structure is the same as the models.py (obviously) and it's in this format :

`user_id(string);`
`user_first_name(string);`
`user_last_name(string);`
`user_gender(string);`
`user_address(string`
`user_email(string);`
`user_image(string),`
`is_user_logged(boolean).`

