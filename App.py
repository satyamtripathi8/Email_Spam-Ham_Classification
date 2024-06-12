from flask import Flask, render_template, url_for, request
import joblib

# Load the model and CountVectorizer
model = joblib.load('MNB_Model.lb')
countvectorizer = joblib.load('CountVectorizer.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        email_message = request.form['email_message']
        email = [email_message]
        transformed_email = countvectorizer.transform(email)
        prediction = model.predict(transformed_email)[0]
        
        label = "Ham" if prediction == 0 else "Spam"

        with open('email.txt', 'a') as file:
            file.write(f"{label}\t{email_message}\n")
        
        return label  

if __name__ == "__main__":
    app.run(debug=True)
