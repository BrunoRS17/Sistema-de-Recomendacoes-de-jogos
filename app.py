from flask import Flask, render_template, request
from src.recomendation import generate_recommendations

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended_games = []
    evaluated_games = []

    if request.method == 'POST':
        selected_user = int(request.form['user_select'])
        recommended_games, evaluated_games = generate_recommendations(selectedUser=selected_user)
  

    return render_template('index.html', recommended_games=recommended_games, evaluated_games=evaluated_games)

if __name__ == "__main__":
    app.run(debug=True)