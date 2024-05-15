# Thesis_Cloud

## Description
Thesis Content Validation System for Bachelor's Degrees at the National Autonomous University of Mexico (UNAM)

## Author and Contact
- Arnoldo Fernando Chue Sánchez: arnoldwork20@gmail.com

## License
GNU General Public License v3.0

## Affiliation
Final project for the Distributed Computing (Cloud Computing) 2024-2 class, designed and developed at the National Autonomous University of Mexico (UNAM), specifically at its National School of Higher Studies, Morelia Campus (ENES Morelia). This project is an integral component of the Bachelor's in Information Technologies for Science curriculum.

## Introduction
Being recognized as the premier university in Mexico, the National Autonomous University of Mexico (UNAM) boasts the largest collection of bachelor's thesis in the country. With a repository comprising over 400,000 research documents spanning nearly two centuries, dating back to the oldest bachelor's thesis from 1840, UNAM stands as a beacon of academic excellence.

While these invaluable resources are physically accessible within the university's main library, the digitization of this vast collection posed a significant challenge. Thus, the concept of TESIUNAM was conceived: a digital repository housing the entirety of UNAM's thesis collection in all their different formats. (Prior to the advent of the Portable Document Format (PDF), the thesis were digitized using videofilm technology.)

In light of this endeavor, Thesis_Cloud emerges as an innovative solution. By leveraging the wealth of data contained within UNAM's bachelor's thesis, this project aims to explore the potential of cloud computing services to benefit students, UNAM, and the nation as a whole.

## Justification
While TESIUNAM represents a first step in this significant effort to manage the enormous amount of data from the vast repository of undergraduate thesis documents published throughout UNAM's history, the reality is that the exploration and utilization of this information have yet to be completed.

Simply put, finding topics of interest for someone who is about to publish their thesis is challenging with the current cataloging and search engine. This not only hampers the work of students but also of all the academic committees of the more than one hundred undergraduate programs offered throughout the country. How can these committees validate whether a thesis topic has already been explored?

Thus, faced with this challenge, I find an exciting opportunity to offer a cloud computing microservice: given the title of a new thesis about to be approved, provide access to previously published related theses. This can be useful both in providing a source of quality information for students and a tool for plagiarism verification for professors.

Furthermore, with all the information intended to be extracted, different data visualization services can be provided to understand the context of research in Mexico over the years.

This work represents an innovative approach that has not yet been explored and offers immense potential to enhance access to and utilization of UNAM's thesis repository.

## Hypothesis
*The hypothesis for this project posits that by employing natural language processing and unsupervised learning techniques, it is feasible to classify over 400,000 bachelor's theses by their titles. This classification process aims to facilitate the creation of a cloud-based cataloging service: given the title or the topic of a thesis, provide access to related theses previously published in TESIUNAM.*

## General Objective
- Develop a cloud-based cataloging service for all bachelor's theses from the National Autonomous University of Mexico (UNAM), categorized according to their research topics as mentioned in their titles.

## Particular Objectives
1. Apply the tools introduced in the Distributed Computing (Cloud Computing) class to design a cloud architecture capable of performing extraction, transformation, and loading (ETL) operations on data related to UNAM's bachelor's theses.
2. Implement efficient algorithms for ETL processing and all machine learning processes involved in thesis classification.
3. Create a platform to access this classification, where users can input their new thesis titles. The algorithm will then provide access to previously published theses that are related to the user's research topic.

## Toolset
- Current Technologies
    - TESIUNAM
    - Python
        - Standard library
        - Numpy
        - Matplotlib
        - Pickle
        - Natural Language Processing and Deep Learning libraries 
            - Spacy
            - Gensim
                - Word2vec
    - Datasets manipulation 
        - Pandas
    - Web Scraping
        - Selenium
        - Requests
    - Automatization
        - Bash
    - Web framework
        - Django
- Technologies for Future Development
    - Seaborn (Improve data visualization)
    - Database administration systems
        - SQL
            - MySQL
            - PostgreSQL
    - Cloud Service
        - AWS
    - Web Server
        - Nginx
    - Docker

## Usage Instructions & Requirements
First of all, it is necessary to have each of the tools of the current development installed. The versions used in the project are:
- Python 3.12 https://www.python.org/downloads/release/python-3120/
- Numpy 1.24.4 https://numpy.org/devdocs/release/1.24.4-notes.html
- Matplotlib 3.8.3 https://matplotlib.org/3.8.3/users/release_notes.html#version-3-8
- Pickle 4.0 https://docs.python.org/3/library/pickle.html
- Spacy 3.7.4 https://spacy.io/usage
- Spacy Spanish Model: es_core_news_sm https://spacy.io/models
- Gensim 4.3.2 https://pypi.org/project/gensim/
- Pandas 2.2.0 https://pandas.pydata.org/docs/dev/whatsnew/v2.2.0.html
- Selenium 4.17.2 https://www.selenium.dev/blog/2024/selenium-4-17-released/
- Requests 2.31.0 https://pypi.org/project/requests/
- Django 5.0.3 https://docs.djangoproject.com/en/5.0/releases/5.0.3/

With everything properly installed and updated, clone the repository, move to the directory "ThesisCloud", and run the Django server. You can do it writing on your terminal 'py manage.py runserver'. This will allow you to access the website locally at the URL 127.0.0.1:8000. Once on the page, you can enjoy the microservice.

## General System Architecture
The general system architecture for Thesis Cloud.

![General System Architecture](/img/GeneralSystemArchitecture.png)

## Metodology
The first phase of the project was data acquisition. For this, I had to interact with the repository of all the theses of UNAM: TESIUNAM (https://tesiunam.dgb.unam.mx/). Since this repository is user-oriented, I had to use web scraping to extract the data I needed. Additionally, due to the different formats in which the information of the theses was placed throughout the years by each of the university's faculties, it was challenging to extract exactly what I wanted. Therefore, I used selenium to apply search filters (undergraduate theses and the year they were published), interact with the page, and extract the titles, authors, years, and link for each thesis. Due to the characteristics of the TESIUNAM server and to ensure reliability in the extraction, the crawler was specially designed to optimize server memory during extraction. It also saves the data in real time to avoid information loss in case of failures in the interaction between the crawler and the server.

Next, I moved on to the data cleaning, preparation, and storage phase. Due to the characteristics of the information I stored, it was not necessary (for now) to use a relational SQL database. This is because the data (title, author, year, and link) can be perfectly placed in a single table. Therefore, to optimize memory usage and be able to use Pandas to preprocess the data for the deep learning model, I saved the data in CSV files. Some of them, due to being too large, were placed in .zip folders (which Pandas can directly read without needing to unzip them) or were stored as git LF to keep them in version control.

Specifically regarding cleaning, I simply had to give the extracted data the correct and readable format. The important preprocessing work was done until the neural network training phase.

Then I moved on to the visualization phase. In this case, I created a single simple yet highly illustrative graph regarding the production of undergraduate theses in the best University in Mexico: the number of theses published per year from the first one (in 1840) to the present day. Once the graph is rendered and saved, I can execute a bash script to copy it to the directory of the website where it will be displayed.

This brought me to the phase of developing the deep learning model. The first thing I did was to preprocess the titles of the theses. This was because they couldn't be directly given to the model for training. First, I needed to ensure that our data is alphabetical, then I removed the stop words (a set of very common words in the language), and finally, I tokenized them (separate each word individually) and lemmatized them (put all the different forms or variations of a word into a single format, the lemma). Once the words had been preprocessed, we could save them in a vector for each instance. For these processing tasks, I used the library spacy with its trained Spanish model "es_core_news_sm."

Terminado el preprocesamiento es que podemos crear el modelo y entrenarlo. Lo primero que hay que mencionar es que en esta tarea usamos la biblioteca gensim con su modelo Word2vec. Los parámetros que le dimos para crear el model son: los datos de entrenamiento son los vectores de palabras preprocesadas, el tamaño del vector es el número de dimensiones de los vectores que va a producir el modelo a partir de cada instancia del entrenamiento, el parámetro window es el number of words to take in consideration before and after the main word context, el min_count se refiere a la minimum frequency that a word must have to be taken in consideration y finalmente sg es el algoritmo para el entrenamiento (en este caso skip-gram). Con el modelo entrenado ahora sólo tenemos que guardarlo como un archivo independiente que podamos volver a cargar con pickle.

After preprocessing, I created and trained the model. It's worth mentioning that for this task, I used the gensim library with its Word2vec model. The parameters I provided to create the model were as follows: the training data is the preprocessed word vectors, the vector size is the number of dimensions of the vectors that the model will produce from each training instance, the window parameter is the number of words to consider before and after the main word context, min_count refers to the minimum frequency that a word must have to be considered, and finally, sg is the algorithm for training (in this case, skip-gram). With the model trained, I simply need to save it as an independent file that we can load back with pickle.

Ahora bien, con el modelo terminado pudimos crear el algoritmo final de nuestro microservicio. Como recibimos como entrada el título o tema de una nueva tesis, lo tenemos que pasar por la función de preprocesamiento que le aplicamos a todas las tesis (tokenización y lematización). Ya con ese vector podemos dárselo al modelo indicando el número de palabras más relacionadas a este nuevo título. El modelo nos regresa ese número de palabras asociadas a una probabilidad de estar relacionadas a ese tema. Naturalmente, entre más alta sea la probabilidad de la palabra, es más probable que las tesis que la contengan estén relacionadas al tema de nuestro input. Por lo tanto, iteramos a través de los vectores de palabras preprocesadas de nuestra base de datos, contamos el número de coincidencias con las palabras proporcionadas por la red neuronal para la nueva tesis. Este número de coincidencias lo podemos manejar como un índice de Jacard para cada tesis con respecto a nuestro input. Por lo que para regresar n tesis más cercanas simplemente debemos de regresar las n tesis con los índices de Jacard más altos. Esto lo regresamos como una matriz donde cada fila contiene la información de esas tesis.

Now, with the model finished, I could create the final algorithm for our microservice. Since it receives as input the title or topic of a new thesis, I need to pass it through the preprocessing function that I applied to all the theses (tokenization and lemmatization). With that vector, I can give it to the model indicating the number of words most related to this new title. The model returns that number of words associated with a probability of being related to that topic. Naturally, the higher the probability of the word, the more likely the theses containing it are related to our input topic. Therefore, I iterate through the preprocessed word vectors of the database, count the number of matches with the words provided by the neural network for the new thesis. We can handle this number of matches as a Jaccard index for each thesis with respect to our input. So, to return the n closest theses, I simply need to return the n theses with the highest Jaccard indices. This is returned as a matrix where each row contains the information of those theses.

These microservice implementation functions were not only written in the directory where the neural network work was done but also in a module at the same level as the Django application directory so that they could be imported into the webpage. Specifically, in this final phase of the work, everything was about integration: setting up the webpage to offer this algorithm, rendering the images, and creating a user interface for each part. This brought us to the first fully functional version of Thesis Cloud.

## Testing and Results
- Thesis Cloud Home Page

- Visualization of the number of theses published per year 

- Microservice

- Let's do some testing of our microservice with the following topics (this must be in Spanish because we train our model with the theses published by the National Autonomous University of Mexico (UNAM))
    - Matemáticas discretas
    - Sismos
    - Saturno
    - Arte barroco
    - Ecología de bosques de pino
    - Calentamiento global
    - Pedagogía
    - Oceanografía
    - Bolsa de valores
    - Vacunas
    - Pandemia
    - Tortugas marinas
    - Sociología
    - Antropología
    - Newton
    - México
    - Software para radiotelescopios
    - Machine learning
    - Análisis de cuencas hídricas

## Conclusions


## References
- TESIUNAM
    - https://tesiunam.dgb.unam.mx/
- Web Scraping
    - Mitchell, R. (2018). Web Scraping with Python. O’Reilly.
- Data Wrangling
    - Vanderplas, J. (2017). Python Data Science Handbook. O’Reilly.
- Machine Learning and Deep Learning
    - Skiena, S. S. (2017). The Data Science Design Manual. Springer.
- Django
    - W3Schools. Django Tutorial. https://www.w3schools.com/django/index.php
- Spacy Documentation
    - https://spacy.io/
- Spacy Spanish Model
    - https://spacy.io/models/es
- Gensim Documentation
    - https://radimrehurek.com/gensim/auto_examples/index.html#documentation
- Gensim Word2Vec Model
    - https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html#sphx-glr-auto-examples-tutorials-run-word2vec-py