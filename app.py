from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_sentiment_data():
    try:
        with open('sentiment_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data['negative'], data['positive']
    except Exception as e:
        print(f"Error loading sentiment data: {e}")
        return [], []

@app.route('/analyze', methods=['POST'])
def analyze():
    negative, positive = load_sentiment_data()
 
    content = request.get_json()
    text = content.get('text', '')
    
    words = text.lower().split() 
    

    contains_negative = any(word in negative for word in words)
    contains_positive = any(word in positive for word in words)

    if contains_negative:
        return jsonify({'result': '-'})  
    elif contains_positive:
        return jsonify({'result': '+'})
    else:
        return jsonify({'result': 'Söz daxil ele'})  

if __name__ == '__main__':
    app.run(debug=True)
