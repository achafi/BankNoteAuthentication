# Bank Note Authentication
![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Flasgger-Swagger-green)
![Frontend](https://img.shields.io/badge/Streamlit-green)


![Project Image](asstes/flask_app_swagger_front1.PNG)
![Project Image](asstes/flask_app_swagger_front2.PNG)
![Project Image](asstes/streamlit_app.PNG)

---

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)


---

## Description

#### Machine Learning algorithms

[Back To The Top](#Bank-Note-Authentication)

---

## How To Use

1. Install all the libraries mentioned in the requirements.txt file.
2. Clone this repository in your local system.
3. Open the command prompt from your project directory and run the command python app1.py.
4. Oppen the command from your project directory and run the command streamlit app_streamlit.py



#### Sources of the datasets
- [Kaggle :  Dataset](https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data)

[Back To The Top](#Bank-Note-Authentication)


### Docker
- Docker command :  ALL THE COMMANDS ARE USED IN DOCKER FILE
- Each and every Docker has a user root folder
- Each docker image has network interface.

1- From : SELECTING base image
2- Copy : copy my host(local) system (the flask app for example) into the user root folder location
3- Expose : port number of network interface
4- Workdir : working directory in my base image
5- RUN : pip install -r requirement.txt
6- CMD : py app.py

### How To Use with docker 
1- Open docker terminal 
> pwd
2- write Dockerfile name it : Dockerfile
3- Build the docker image
> docker build -t money_api .
4 - Running our money authenticator app
> docker run -p 8000:8000 money_api

don't forget to use default machine IP adress instead of localhost !

[Back To The Top](#Bank-Note-Authentication)
---

## References
.
.
.


- Website - [Assia CHAFI](https://achafi.github.io/myportfolio/)
[Back To The Top](#Movie-Recommender-System-and-Reviews-Sentiment-Analysis)