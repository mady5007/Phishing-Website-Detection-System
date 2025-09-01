from flask import Flask,render_template,request
import pickle
import re

app = Flask(__name__)

vector=pickle.load(open("vectorizer.pkl",'rb'))
model=pickle.load(open("phishing.pkl",'rb'))

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=="POST":
        url=request.form['url']
        cleaned_url=re.sub(r'^https?://(www\.)?','',url)

        predict=model.predict(vector.transform([url]))[0]
        #print(predict)
        if predict=='bad':
            predict="Phshing"
        elif predict=='good':
            predict="Good"
        else:
            predict="Something went wrong"
        # predict = model.predict(vector.transform([url]))[0]

        # if predict == 1:
        #     predict = "Phishing"
        # else:
        #     predict = "Legitimate"


        return render_template("index.html",predict=predict)


    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)