# Welcome to My Imdb Api
***

## Task
The goal of this project is to build a lightweight REST API that provides movie information from an IMDB dataset.
The main challenge is to load movie data from CSV file, process it, and make it accessible through HTTP GET requests.
The API must also allow users to filter movies by genre and return the results in JSON format.

## Description
My IMDB API is a lightweight REST API built with Python and Flask.
It allows users to retrieve movie information from and IMDb dataset stored in a CSV file
The API provides movie data in JSON format and allows users to filter movies by genre

## Installation
1. Clone the repository:
```bash
git clone git@git.us.qwasar.io:my_imdb_api_220906_ypwves/my_imdb_api.git 
```
2. Navigate to the project directory:
```bash
cd my_imdb_api 
```
3. Install Flask:
```bash
pip install Flask
```
4. Make sure the imdb-movie-data.csv dataset is available in the project directory

## Usage
Run the application with:
```bash
python3 app.py
```
The API starts on port 8080.
You can access the API using a browser or curl.
Examples:
Retrieve all movies:
```bash
curl "http://localhost:8080/"
```
Retrieve movies by genre:
```bash
curl "http://localhost:8080/?genre=western"
```
Retrieve action movies:
```bash
curl "http://localhost:8080/action"
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
