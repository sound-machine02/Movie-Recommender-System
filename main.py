import pickle

import requests

# try:
#     with open('movie_list.pkl', 'rb') as file:
#         movies = pickle.load(file)
#     print(movies)  # Or examine the contents
# except Exception as e:
#     print(f"Error loading pickle file: {e}")

# try:
#   movies = pickle.load(open('./artifacts/movie_list.pkl','rb'))
#   sim = pickle.load(open('./artifacts/similarity.pkl','rb'))
#   print(movies)
#   # print(sim)
# except Exception as e:
#     print(f"Error loading pickle file: {e}")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=708aa82ed60a0d3763123104339f741b".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

print(fetch_poster(49026))