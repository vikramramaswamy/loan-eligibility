from flask import Flask , render_template, request
import numpy as np
import pickle
from sklearn.ensemble import GradientBoostingClassifier
import joblib
#with open('xgb_cv_final.pkl','rb') as f:
 #   clf_individual = pickle.load(f)
#clf_individual = joblib.load("xgb_cv_final.pkl")
model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if (request.method == "POST"):
        AppIncome = int(request.form['AppIncome'])
        CoAppIncome = int(request.form['CoAppIncome'])
        gender = request.form['gender']
        married = request.form['married']
        property = request.form['property']
        credit = request.form['credit']
        education = request.form['education']
        selfEmp = request.form['self']
        dependent = int(request.form['dependent'])
        amount = int(request.form['amount'])
        amountTerm =int(request.form['amountTerm'])
        amount = np.log(amount)
        totalIncome = AppIncome+CoAppIncome
        if credit == "Yes":
            credit= 1
        else:
            credit = 0
        if gender == "Male":
            Gender_Female = 0
            Gender_Male = 1
        else:
            Gender_Female = 1
            Gender_Male = 0
        if married == "Yes":
            Married_No = 0
            Married_Yes = 1
        else:
            Married_No = 1
            Married_Yes = 0
        if dependent == 0:
            Dependents_0 = 1
            Dependents_1 = 0
            Dependents_2 = 0
            Dependents_3 = 0
        elif dependent == 1:
            Dependents_0 = 0
            Dependents_1 = 1
            Dependents_2 = 0
            Dependents_3 = 0
        elif dependent == 2:
            Dependents_0 = 0
            Dependents_1 = 0
            Dependents_2 = 1
            Dependents_3 = 0
        elif dependent >= 3:
            Dependents_0 = 0
            Dependents_1 = 0
            Dependents_2 = 0
            Dependents_3 = 1
        if education == "Yes":
            Education_Graduate = 1
            Education_Not_Graduate	= 0
        else:
            Education_Graduate = 0
            Education_Not_Graduate	= 1

        if selfEmp == "Yes":
            Self_Employed_No = 0
            Self_Employed_Yes = 1
        else:
            Self_Employed_No = 1
            Self_Employed_Yes = 0
        
        if property == "Urban":
            Property_Area_Rural = 0
            Property_Area_Semiurban = 0
            Property_Area_Urban = 1
        elif property == "Semiurban":
            Property_Area_Rural = 0
            Property_Area_Semiurban = 1
            Property_Area_Urban = 0
        elif property == "Rural":
            Property_Area_Rural = 1
            Property_Area_Semiurban = 0
            Property_Area_Urban = 0

        predInput = [[amountTerm,credit, amount,totalIncome, Gender_Female, Gender_Male, Married_No, Married_Yes, Dependents_0, Dependents_1, Dependents_2, Dependents_3, Education_Graduate, Education_Not_Graduate, Self_Employed_No, Self_Employed_Yes,Property_Area_Rural, Property_Area_Semiurban, Property_Area_Urban]]
        o = model.predict(predInput)
        o = 0
        
        if o == 0:
            output = "You are not qualify for loan"
            color = "red"
            print(o)
            return render_template( 'index.html', output=output,color=color)
        if o == 1:
            output = "Congratulations!! You qualify for the loan"
            color = "green"
            print(o)
            
            return render_template( 'index.html', output=output,color=color)
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
