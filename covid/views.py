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
        full_name = str(request.POST['full_name'])
        age = int(request.POST['age'])
        gender = int(request.POST['gender'])
        fever = int(request.POST['fever'])
        cough = int(request.POST['cough'])
        fatigue = int(request.POST['fatigue'])
        pains = int(request.POST['pains'])
        nasal_congestion = int(request.POST['nasal_congestion'])
        shortness_of_breath = int(request.POST['shortness_of_breath'])
        runny_nose = int(request.POST['runny_nose'])
        sore_throat = int(request.POST['sore_throat'])
        diarrhea = int(request.POST['diarrhea'])
        chills = int(request.POST['chills'])
        headache = int(request.POST['headache'])
        vomiting = int(request.POST['vomiting'])
        lives_in_affected_area = int(request.POST['lives_in_affected_area'])


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
        ).reshape(1, 13)

        rf = RandomForestClassifier(random_state=42)

        rf.fit(np.nan_to_num(X), y)
        rf.score(np.nan_to_num(X), y)
        result = rf.predict_proba(user_data)

    return render(request,"index.html",{'result':result})