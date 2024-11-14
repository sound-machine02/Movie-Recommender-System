import pickle
import streamlit as st
import pandas as pd
import numpy as np
import requests


# Function to recommend movies
def recommend_movie(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_idx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in movies_list:
        movie_id = movies['movie_id'][i[0]]
        recommended_movie_names.append(movies['title'][i[0]])
        recommended_movie_posters.append(fetch_poster(movie_id))       # fetch poster from TMDb API
        # st.write(fetch_poster(movie_id))         

    return recommended_movie_names, recommended_movie_posters


# Function to fetch movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=708aa82ed60a0d3763123104339f741b".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


movies = pickle.load(open('./artifacts/movie_list.pkl','rb'))           # DataFrame
similarity = pickle.load(open('./artifacts/similarity.pkl','rb'))

movie_list = movies['title'].values             # NumPy Array

st.title("Movie Recommender System")

# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list.tolist(),
#     placeholder="Choose a movie"
#     )

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    ["Select a movie..."] + movie_list.tolist(),  # Placeholder as the first item
    placeholder="Choose a movie"
)

# Recommendation logic with validation for movie selection
if st.button("_Show Recommendation_"):
    if selected_movie == "Select a movie...":  # Check if the user selected a movie
        st.error("Please select a movie before clicking 'Show Recommendation'.")

    else:
        movie_names, movie_posters = recommend_movie(selected_movie)       # list
        
        cols = st.columns(5)

        # Loop through the recommended movie names and posters and assign them to each column
        for i in range(5):
            with cols[i]:
                st.markdown(f"<div style='text-align: center; font-size:16px; margin-bottom:10px;'>{movie_names[i]}</div>",unsafe_allow_html=True)
                st.image(movie_posters[i])