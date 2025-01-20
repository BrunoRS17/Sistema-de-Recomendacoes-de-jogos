import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.impute import SimpleImputer

ratings_df = pd.read_csv('data/user_ratings.csv')


imputer = SimpleImputer(strategy="mean")
ratings_filled = imputer.fit_transform(ratings_df.values)

def generate_recommendations(selectedUser):
    user_ratings = ratings_filled[selectedUser]
    other_users_ratings = np.delete(ratings_filled, selectedUser, axis=0)
    
    user_similarity = cosine_similarity([user_ratings], other_users_ratings)[0]
    similar_user_indices = np.argsort(user_similarity[::-1])
    
    recommended_games = []
    
    for user_idx in similar_user_indices[:5]:  #Base dos 5 usuarios semelhantes
        similar_user_ratings = ratings_filled[user_idx]
        for game_idx, rating in enumerate(similar_user_ratings):
            if user_ratings[game_idx] == 0 and rating > 5:  # Recomendar jogos não avaliados
                recommended_games.append(ratings_df.columns[game_idx])
    
    recommended_games = list(set(recommended_games))
    evaluated_games = [ratings_df.columns[i] for i in range(len(user_ratings)) if user_ratings[i] > 0]
    
    return recommended_games, evaluated_games
