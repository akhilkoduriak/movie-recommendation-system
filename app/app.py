# app/app.py

from flask import Flask, render_template, request
from models.content_based import load_movie_data, build_similarity_matrix, get_content_recommendations
from models.collaborative import load_user_movie_matrix, build_movie_similarity_matrix, get_collaborative_recommendations

app = Flask(__name__)

# Load data and models once
movies_df = load_movie_data()
content_sim_matrix = build_similarity_matrix(movies_df)
user_movie_matrix = load_user_movie_matrix()
collab_sim_matrix = build_movie_similarity_matrix(user_movie_matrix)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    selected_title = ""
    method = "content"

    if request.method == "POST":
        selected_title = request.form["movie"]
        method = request.form["method"]

        if method == "content":
            recommendations = get_content_recommendations(selected_title, movies_df, content_sim_matrix)
        else:
            recommendations = get_collaborative_recommendations(selected_title, collab_sim_matrix)

    return render_template("index.html",
                           movie_titles=movies_df["title"].tolist(),
                           selected_title=selected_title,
                           method=method,
                           recommendations=recommendations)
