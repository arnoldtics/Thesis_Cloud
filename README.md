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

Thus, faced with this challenge, we find an exciting opportunity to offer a cloud computing microservice: given the title of a new thesis about to be approved, provide access to previously published related theses. This can be useful both in providing a source of quality information for students and a tool for plagiarism verification for professors.

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

## General System Architecture
The general system architecture for Thesis Cloud.

![General System Architecture](/img/GeneralSystemArchitecture.png)
