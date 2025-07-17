# content_based.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess movie data
def load_movie_data():
    movies = pd.read_csv('data/movies.csv')  # movieId, title, genres
    movies['genres'] = movies['genres'].fillna('')
    return movies

# Create cosine similarity matrix
def build_similarity_matrix(movies):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

# Recommend top N similar movies
def get_content_recommendations(title, movies, cosine_sim, num=10):
    indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

    if title not in indices:
        return ["Movie not found."]

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num+1]
    movie_indices = [i[0] for i in sim_scores]
    
    return movies['title'].iloc[movie_indices].tolist()

# Example (for testing only):
if __name__ == "__main__":
    movies = load_movie_data()
    sim_matrix = build_similarity_matrix(movies)
    print(get_content_recommendations("Toy Story (1995)", movies, sim_matrix))
