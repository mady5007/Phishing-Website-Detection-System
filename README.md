# Phishing Website Detection System  

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)  
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?logo=flask)  
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange?logo=scikit-learn)  
![Status](https://img.shields.io/badge/Status-Active-success)  
![License](https://img.shields.io/badge/License-MIT-green)  

> A Machine Learning + Flask-based web application that detects **phishing websites** from URL features and classifies them as **Legitimate** or **Phishing**.  

---

## Features  
- Extracts and analyzes URL-based features  
- Trained using multiple models:  
  - Logistic Regression (`phishing.pkl`)  
  - Multinomial Naive Bayes (`phishing_mnb.pkl`)  
- Flask web app with an HTML front-end (`templates/`)  
- Dataset included for training and testing  
- Ready-to-deploy project structure  

---

## Tech Stack  
- **Python 3.x**  
- **Flask** (Web framework)  
- **Scikit-learn** (Machine Learning)  
- **Pandas, NumPy** (Data handling)  
- **Pickle / Joblib** (Model serialization)  
- **Jupyter Notebook** (Model training & evaluation)  
- **Matplotlib, Seaborn, WordCloud** (Data visualization)  
- **NLTK** (Text preprocessing)  

---

##  Project Structure  

```bash
Phishing Website Detection System/
│── .ipynb_checkpoints/                # Jupyter autosave files
│── .vscode/                           # VS Code settings
│── Dataset/                           # Dataset used for training/testing
│── env/                               # Virtual environment (not uploaded to GitHub)
│── templates/                         # HTML templates for Flask app
│── app.py                             # Flask web application
│── requirments.txt                    # Dependencies list
│── Phishing website detection system.ipynb  # ML training notebook
│── phishing.pkl                        # Trained ML model (Logistic Regression)
│── phishing_mnb.pkl                    # Trained ML model (MultinomialNB)
│── vectorizer.pkl                      # Vectorizer for URL features
```

---

## Installation  

1. Clone this repository:  
   ```bash
   git clone https://github.com/mady5007/Phishing-Website-Detection-System.git
   cd Phishing-Website-Detection-System
   ```

2. Create a virtual environment (recommended):  
   ```bash
   python -m venv env
   source env/bin/activate   # On Linux/Mac
   env\Scripts\activate      # On Windows
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirments.txt
   ```

4. (Optional) Download NLTK resources:  
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   ```

---

## Usage  

### 1. Train / Retrain Model  
Run the Jupyter Notebook:  
```bash
jupyter notebook "Phishing website detection system.ipynb"
```

### 2. Start Flask App  
```bash
python app.py
```
The server will start at **http://127.0.0.1:5000/**  

### 3. Test in Browser  
Open `http://127.0.0.1:5000/` and enter a URL to check if it is **Legitimate** or **Phishing**.  

---

## Dataset  
The dataset used for training is located in the `Dataset/` folder.  

If you want a public dataset reference, you can use:  
- [UCI ML Repository - Phishing Websites Dataset](https://archive.ics.uci.edu/ml/datasets/Phishing+Websites)  
- [PhishTank](https://www.phishtank.com/)  

---

## Contributing  
Pull requests are welcome! You can improve the model, UI, or add new features.

1. Fork the repo  
2. Create a new branch (`git checkout -b feature-name`)  
3. Commit changes (`git commit -m "Added feature"`)  
4. Push to your branch (`git push origin feature-name`)  
5. Open a Pull Request  

---

## Acknowledgements  
- [Scikit-learn](https://scikit-learn.org/stable/)  
- [Flask](https://flask.palletsprojects.com/)  
- [NLTK](https://www.nltk.org/)  
- [WordCloud](https://github.com/amueller/word_cloud)  

---

## Conclusion
The **Phishing Website Detection System** demonstrates how Machine Learning and Flask can be combined to build a practical security application.  
By analyzing URL features, the system effectively classifies websites as **Legitimate** or **Phishing**, helping users stay safe online.  

This project can be further enhanced with:  
- Larger and more diverse datasets  
- Advanced models like deep learning  
- Real-time browser extensions or cloud deployment  

Overall, this project serves as a strong foundation for exploring **cybersecurity solutions using Machine Learning**.  