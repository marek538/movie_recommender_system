# Movie Recommender System

## Project Description
A web-based movie recommendation platform built with Flask. The system generates personalized movie suggestions for users by calculating similarity scores based on their historical ratings and film genre profiles.

## Key Features
* **Personalized Recommendations:** Uses a weighted dot-product scoring system to match users with movies they haven't rated yet.
* **TF-IDF Integration:** Implements Inverse Document Frequency (IDF) logic to weigh movie attributes, ensuring recommendations are tailored to unique user interests.
* **User Management:** Dynamic handling of users, rating profiles, and administrative tools for re-calculating model parameters.
* **Web Interface:** Interactive frontend built with Flask templates allowing users to search, filter, and rate movies.
