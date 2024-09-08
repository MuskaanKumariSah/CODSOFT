movies = {
    'The Pursuit Of Happyness': ['drama', 'biography', 'motivational'],
    'Inception': ['sci-fi', 'thriller'],
    'Interstellar': ['sci-fi', 'drama','education'],
    'Conjuring': ['drama', 'horror'],
    'Gravity': ['si-fi', 'thriller'],
    'The Shawshank Redemption': ['thriller', 'crime','inspirational']
}

def calculate_overlap(user_input, movie_features):
    
    return len(set(movie_features) & set(user_input.split()))

def recommend_movie(user_input, movies_data):
    
    best_match = None
    max_overlap = 0

    for movie, features in movies_data.items():
        overlap = calculate_overlap(user_input, features)
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = movie

    return best_match
    
user_input = input("Enter your favorite genre: ")

recommended_movie = recommend_movie(user_input, movies)

if recommended_movie:
    print(f"Recommended movie for you: {recommended_movie}")
else:
    print("Sorry, no recommendations found.")