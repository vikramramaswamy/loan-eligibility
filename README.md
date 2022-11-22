# Loan Eligibility Predict
Implement a Classification Analysis Predictive Model for Determining whether a Person should be Granted Loan or Not.

[Live here](https://loanapprovel.herokuapp.com/)

# Features

| **#** | **Column** | **Dtype** | **Description** |
| :--- | :--- | :--- | :--- |
| 0 | Loan Id | Object | Unique loan id of applicant |
| 1 | Gender | Object | Gender of applicant Male/Female |
| 2 | Married | Object | Status of applicant Married or not |
| 3 | Dependent | Object | Number of children |
| 4 | Education | Object | Education status Graduate or not graduate |
| 5 | Self Employed | Object | self employed or not |
| 6 | Applicant Income | int64 | Income of Applicant |
| 7 | Co-applicant Income | float64| Income of Co-applicant if having other wise 0 |
| 8 | Loan Amount | float64 | Loan amount required by applicant |
| 9 | Loan Amount Term | float64 | Loan amount term in months |
| 10 | Credit History | float64 | Having any loan history |
| 11 | Property Area | Object | Applicant property in which area |
| 12 | Loan Status | Object | Target variable |


# Models
| **Classifiers** | **precision** | **recall** | **f1-score** | **accuracy** |
| :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 0.802548 | 0.992126 | 0.887324 | 0.827027 |
| **Support Vector** | 0.802548 | 0.992126 | 0.887324 | 0.827027 |
| **Decision Tree** | 0.815789 | 0.976378 | 0.888889	 | 0.832432 |
| **Random Forest** | 0.802548 | 0.992126 | 0.887324 | 0.827027 |
| **KNeighbors** | 0.715909 | 0.992126 | 0.831683 | 0.724324 |
| **XGboost** | 0.796178 | 0.984252 | 0.880282 | 0.816216 |
