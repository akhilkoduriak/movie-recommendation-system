# collaborative.py

import pandas as pd

# Load and preprocess data
def load_user_movie_matrix():
    ratings = pd.read_csv('data/ratings.csv')  # userId, movieId, rating
    movies = pd.read_csv('data/movies.csv')    # movieId, title, genres

    merged = pd.merge(ratings, movies, on='movieId')
    user_movie_matrix = merged.pivot_table(index='userId', columns='title', values='rating')
    user_movie_matrix = user_movie_matrix.fillna(0)  # or use mean imputation
    return user_movie_matrix

# Build similarity matrix using Pearson correlation
def build_movie_similarity_matrix(user_movie_matrix):
    return user_movie_matrix.corr(method='pearson')

# Recommend similar movies
def get_collaborative_recommendations(title, similarity_matrix, num=10):
    if title not in similarity_matrix.columns:
        return ["Movie not found."]
    
    sim_scores = similarity_matrix[title].dropna()
    sim_scores = sim_scores.sort_values(ascending=False)
    return list(sim_scores.index[1:num+1])

# Example (for testing only):
if __name__ == "__main__":
    matrix = load_user_movie_matrix()
    sim_matrix = build_movie_similarity_matrix(matrix)
    print(get_collaborative_recommendations("Toy Story (1995)", sim_matrix))
