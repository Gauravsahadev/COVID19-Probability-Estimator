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
        fatigue = request.POST.get('fatigue')
        fatigue = 1 if fatigue else 0
        pains = request.POST.get('pains')
        pains = 1 if pains else 0
        nasal_congestion = request.POST.get('nasal_congestion')
        nasal_congestion = 1 if nasal_congestion else 0
        shortness_of_breath = request.POST.get('shortness_of_breath')
        shortness_of_breath = 1 if shortness_of_breath else 0
        runny_nose = request.POST.get('runny_nose')
        runny_nose = 1 if runny_nose else 0
        sore_throat = request.POST.get('sore_throat')
        sore_throat = 1 if sore_throat else 0
        diarrhea = request.POST.get('diarrhea')
        diarrhea = 1 if diarrhea else 0
        chills = request.POST.get('chills')
        chills = 1 if chills else 0
        headache =request.POST.get('headache')
        headache = 1 if headache else 0
        vomiting = request.POST.get('vomiting')
        vomiting = 1 if vomiting else 0
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

        print(user_data)

        rf = RandomForestClassifier(random_state=42)

        rf.fit(np.nan_to_num(X), y)
        rf.score(np.nan_to_num(X), y)
        result = rf.predict_proba(user_data)
        result=round(result[0][1]*100,2)
        return render(request,"index.html",{'result':result})
    else:
        return render(request,"index.html")

