from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the CSV file
df = pd.read_csv("books.csv")

@app.route('/')
def index():
    query = request.args.get('q', '').lower()
    if query:
        filtered_df = df[df['Title'].str.lower().str.contains(query)]
    else:
        filtered_df = df
    return render_template('index.html', books=filtered_df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

