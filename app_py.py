import streamlit as st
import pandas as pd

# Sample movie dataset
data = {
    'Title': ['Toy Story', 'Inception', 'The Matrix', 'Titanic', 'Avatar'],
    'Genre': ['Animation', 'Sci-Fi', 'Sci-Fi', 'Romance', 'Action']
}

df = pd.DataFrame(data)

# Streamlit UI
st.title("🎬 Movie Recommendation System")

movie = st.selectbox("Select a movie:", df['Title'])

if st.button("Recommend"):
    genre = df[df['Title'] == movie]['Genre'].values[0]
    recommendations = df[df['Genre'] == genre]['Title'].tolist()
    recommendations.remove(movie)

    st.success("Recommended Movies:")
    for m in recommendations:
        st.write(m)

st.markdown("**Designed & Developed by: Anchal**")
