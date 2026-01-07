import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
data = {
    'Title': ['Toy Story', 'Inception', 'The Matrix', 'Titanic', 'Avatar'],
    'Description': [
        'animation toys friendship',
        'dream subconscious mind thriller',
        'virtual reality future technology',
        'romance love ship tragedy',
        'future alien planet action'
    ]
}

df = pd.DataFrame(data)

# ML STEP 1: Convert text to numbers
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['Description'])

# ML STEP 2: Calculate similarity
cosine_sim = cosine_similarity(tfidf_matrix)

# Recommendation function
def recommend(movie_name):
    if movie_name not in df['Title'].values:
        return ["Movie not found"]

    idx = df[df['Title'] == movie_name].index[0]
    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i in scores[1:4]:
        recommendations.append(df['Title'][i[0]])

    return recommendations

# Streamlit UI
st.title("🎬 AI Movie Recommendation System")

movie = st.selectbox("Select a movie", df['Title'])

if st.button("Recommend Movies"):
    rec_movies = recommend(movie)
    st.success("Recommended Movies:")
    for m in rec_movies:
        st.write(m)

st.markdown("**Designed & Developed by: Anchal**")
