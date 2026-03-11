
import streamlit as st
import pickle
import pandas as pd

# Load movie data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Recommendation function
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# ---------------- Streamlit UI ---------------- #

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🍿 Movie Recommender System")

st.write("Select a movie and get similar movie recommendations.")

selected_movie = st.selectbox(
    "Select a movie you like",
    movies['title'].values
)

if st.button("Recommend Movies"):

    names = recommend(selected_movie)

    st.subheader("Top 5 Recommended Movies")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(names[0])

    with col2:
        st.write(names[1])

    with col3:
        st.write(names[2])

    with col4:
        st.write(names[3])

    with col5:
        st.write(names[4])