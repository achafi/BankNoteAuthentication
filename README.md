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
In this project I:

-   built a flask app for Note Bank Authentification.
-   Deploy Machine Learning Models Using Flask And Flasgger
-   Write, Build And Run Docker Image
-   Deploy Machine Learning Models Using StreamLit Library

#### Machine Learning algorithms
Random Forest Classifier perform with acuracy of 99%.

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
Docker is a set of platform as a service products that uses OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels:

- Docker command :  ALL THE COMMANDS ARE USED IN DOCKER FILE
- Each and every Docker has a user root folder
- Each docker image has network interface.

- **From** : SELECTING base image
- **Copy** : copy my host(local) system (the flask app for example) into the user root folder location
- **Expose** : port number of network interface
- **Workdir** : working directory in my base image
- **RUN** : pip install -r requirement.txt
- **CMD** : py app.py

### How To Use with docker 
- Open docker terminal <br/>
> pwd <br/>
- write Dockerfile name it : Dockerfile <br/>
- Build the docker image <br/>
> docker build -t money_api . <br/>
- Running our money authenticator app <br/>
> docker run -p 8000:8000 money_api <br/>

don't forget to use default machine IP adress instead of localhost ! <br/>

[Back To The Top](#Bank-Note-Authentication)
---

## References
.
.
.


- Website - [Assia CHAFI](https://achafi.github.io/myportfolio/)
[Back To The Top](#Movie-Recommender-System-and-Reviews-Sentiment-Analysis)