# Team-International-Backend 



Task given: Dockerized micro-service for showing a dashboard for logged in users

#Django will be used  as the main Framework


1--Fork the project to your github account
    
   
2--Clone the repository in your local environement
  2.1--Run this command git  remote add https://github.com/bensoftware/Team-International-Backend/edit/master/README.md
  
3--Create the JSON file,this is the structure(Same structure than the attributes in the model) :
user_id(string);
user_first_name(string);
user_last_name(string);
user_email(string);
user_image(string),you can use any public image link;
is_user_logged(boolean) it will always be true in our case.


4--Put the pre-prepared  JSON file in your project;

5--Integrete Swagger in the project;

6--Create your microservice API it has to read the JSON file and display
the outpout through the endpoint(api/team-international/user/logged);

NOTE:It's the GET method;

7--Test your API if it displays data;

8--Document your API using SWAGGER(We have just one method to document,let's call that : loggedUser );

9--Create the txt file with your slack name for example @ben.Put your HNG-Board ID in the file.

10--Put instructions in the Dockerfile  located in the project's root,this  will allow you to create the image.This bellow link will hepl you.
https://www.youtube.com/watch?v=KN8wuFi2RXM

11--Create your image using Dockerfile.

12--Use Docker command and Dockerfile to Create the container .

13-Run the container.

14--Run git add . (To add and upade files in the stagging area);

15--Commit your repository:git commit -m "Microservice created"

16--Run git push origin master to push to your fork.For example (git push origin master  https://github.com/bensoftware/Team-International-Backend.git);

17--Create the pull request to the main repository (https://github.com/hngi/Team-International-Backend.git).
