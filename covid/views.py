from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def index(request):
    
    df = pd.read_csv('covid_final_data.csv')
    X = df.iloc[:,0:15].values
    y = df.iloc[:,15].values

    

    if request.method == 'POST':
        # full_name = str(request.POST['full_name'])
        age = request.POST['age']
        gender = request.POST['gender']
        fever = request.POST['fever']
        cough = request.POST['cough']
        fatigue = request.POST['fatigue']
        pains = request.POST['pains']
        nasal_congestion = request.POST['nasal_congestion']
        shortness_of_breath = request.POST['shortness_of_breath']
        runny_nose = request.POST['runny_nose']
        sore_throat = request.POST['sore_throat']
        diarrhea = request.POST['diarrhea']
        chills = request.POST['chills']
        headache =request.POST['headache']
        vomiting = request.POST['vomiting']
        lives_in_affected_area = request.POST['lives_in_affected_area']


        user_data = np.array(
            (age,
             gender,
             fever,
             cough,
             fatigue,
             pains,
             nasal_congestion,
             shortness_of_breath,
             runny_nose,
             sore_throat,
             diarrhea,
             chills,
             headache,
             vomiting,
             lives_in_affected_area)
        ).reshape(1, 15)

        rf = RandomForestClassifier(random_state=42)

        rf.fit(np.nan_to_num(X), y)
        rf.score(np.nan_to_num(X), y)
        result = rf.predict_proba(user_data)
        return render(request,"index.html",{'result':result})
    else:
        return render(request,"index.html")

