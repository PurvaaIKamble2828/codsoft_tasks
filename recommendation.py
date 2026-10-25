import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# छोटा डेटासेट (मूव्हीज आणि त्यांचे जॉनर/प्रकार)
data = {
    'Title': ['Inception', 'Interstellar', 'The Dark Knight', 'Titanic', 'Avatar'],
    'Genre': ['Sci-Fi Action', 'Sci-Fi Drama', 'Action Crime', 'Romance Drama', 'Sci-Fi Action']
}

df = pd.DataFrame(data)
print("--- Movie Dataset ---")
print(df)
print("\n-----------------------\n")

# मजकुराचे (Genres) व्हेक्टरमध्ये रूपांतर करण्यासाठी TF-IDF वापरणे
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['Genre'])

# कॉसाइन सिमिलॅरिटी (Cosine Similarity) कॅलक्युलेट करणे
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend(movie_title):
    if movie_title not in df['Title'].values:
        return f"Movie '{movie_title}' not found in dataset!"
    
    # मूव्हीचा इंडेक्स शोधणे
    idx = df[df['Title'] == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    
    # स्कोअरनुसार सॉर्ट करणे
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    # स्वतःला सोडून इतर टॉप २ रिकमండేशन्स घेणे
    recommendations = [df['Title'][i[0]] for i in scores[1:3]]
    return recommendations

# टेस्ट करणे: 'Inception' सारखे चित्रपट शोधणे
test_movie = 'Inception'
print(f"Recommendations for '{test_movie}':")
recs = recommend(test_movie)
for r in recs:
   print("-",r)