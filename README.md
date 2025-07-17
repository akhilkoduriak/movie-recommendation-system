#  Movie Recommendation System

##  Project Overview

This project is a **Flask-based movie recommendation system** that provides personalized movie suggestions using two core techniques:

- **Content-Based Filtering** (using TF-IDF on genres)
- **Collaborative Filtering** (using user-item ratings)

Users can interact with the application via a web interface, select a movie, and receive recommendations based on their preferred method.

---

##  Project Structure

```bash
recommendation_system/
├── app/
│   └── app.py                      # Flask app routing and logic
├── models/
│   ├── content_based.py            # TF-IDF and content filtering
│   └── collaborative.py            # User-based collaborative filtering
├── data/
│   ├── movies.csv                  # Movie metadata
│   └── ratings.csv                 # User ratings
├── templates/
│   └── index.html                  # Flask Jinja2 HTML interface
├── static/                         # (Optional) CSS/JS/image assets
├── run.py                          # Entry point to run Flask app
├── requirements.txt                # List of dependencies
├── README.md                       # Project overview and instructions
└── Final_Recommendation_System_Report.docx  # Formal APA-style report
```

---

##  Recommendation Techniques

### 1. Content-Based Filtering
- Uses TF-IDF vectorization on movie genres
- Computes cosine similarity between selected movie and others
- Recommends top-N similar movies

### 2. Collaborative Filtering
- Builds a user-item matrix
- Computes user similarity via Pearson correlation
- Recommends movies liked by similar users

---

##  How to Run the Project

###  Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/recommendation_system.git
cd recommendation_system
```

###  Step 2: Create and Activate Virtual Environment (Windows)
```bash
python -m venv venv
.env\Scriptsctivate
```

###  Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶ Step 4: Run the Flask App
```bash
python run.py
```

Visit `http://127.0.0.1:5000` in your browser to use the app.

---

##  Dataset

This project uses the [MovieLens 100k dataset](https://grouplens.org/datasets/movielens/100k/), preprocessed into:

- `movies.csv`: Movie metadata (ID, title, genres)
- `ratings.csv`: User ratings (userId, movieId, rating, timestamp)

---

##  Included Files for Submission

- `Final_Recommendation_System_Report.docx` – Full APA-style project report
- `README.md` – Instructions and documentation
- All `.py` files in `app/` and `models/`
- HTML template in `templates/`
- `movies.csv` and `ratings.csv` in `data/`
- `requirements.txt` listing dependencies

---

##  Notes

- You must add `index.html` to the `templates/` directory.
- Be sure to activate your virtual environment before running the project.

---

##  Author

Sivarama Krishna Akhil Koduri

For academic use only.
