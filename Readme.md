##Deployed FastAPI application to Docker container##
first we write an file main.py --> This file indicates the containt of the application.
next we write the requriments.txt file for the what dependencies needed to install.

##layer caching docker file##
This is used to we have changes the main file not effected the install dependencies.
ex: if we have change the something in main.py file while running the docker file it was running layer by layer thats way we copied the requirements.txt file first after that to run the file pip install -r requirements.txt file then only we reduce the time / what ever to changes that only deployed..