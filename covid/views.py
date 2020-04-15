from django.shortcuts import render
from .models import Coviddata
import pickle
import numpy as np
import pandas as pd
import json
def index(request):
    
    if request.method == 'POST':
        full_name = request.POST['full_name']
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
        file = open("model.pkl", "rb")
        classifier = pickle.load(file)
        file.close()
        user_data = np.array(
            (age,
             gender,
             lives_in_affected_area,
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
             vomiting
             )
        ).reshape(1, 15)

        result = classifier.predict_proba(user_data) 
        result=round(result[0][1]*100,2)
        print(f"Result: {result}")

        covid_data=Coviddata.objects.create(age=age,gender=gender,fever=fever,cough=cough,fatigue=fatigue,pains=pains,nasal_congestion=nasal_congestion,shortness_of_breath=shortness_of_breath,runny_nose=runny_nose,sore_throat=sore_throat,diarrhea=diarrhea,chills=chills,headache=headache,vomiting=vomiting,lives_in_affected_area=lives_in_affected_area,result=result)
        covid_data.save()

        age = int(user_data[0][0])
        gender = 'Male' if int(user_data[0][1]) else 'Female'
        lives_in_affected_area ='Yes' if int(user_data[0][2]) else 'No'
        fever ='Yes' if int(user_data[0][3]) else 'No'
        cough ='Yes' if int(user_data[0][4]) else 'No'
        fatigue ='Yes' if int(user_data[0][5]) else 'No'
        pains = 'Yes' if int(user_data[0][6]) else 'No'
        nasal_congestion='Yes' if int(user_data[0][7]) else 'No'
        shortness_of_breath = 'Yes' if int(user_data[0][8]) else 'No'
        runny_nose = 'Yes' if int(user_data[0][9]) else 'No'
        sore_throat = 'Yes' if int(user_data[0][10]) else 'No'
        diarrhea = 'Yes' if int(user_data[0][11]) else 'No'
        chills = 'Yes' if int(user_data[0][12]) else 'No'
        headache = 'Yes' if int(user_data[0][13]) else 'No'
        vomiting = 'Yes' if int(user_data[0][14]) else 'No'

        user_details_API = {
            'Name':full_name,
            'Age':age,
            'Gender':gender,
            'Living in Affected Area':lives_in_affected_area,
            'Fever':fever,
            'Dry Cough':cough,
            'Fatigue':fatigue,
            'Pains':pains,
            'Nasal Congestion':nasal_congestion,
            'Problem in Breathing':shortness_of_breath,
            'Runny Nose':runny_nose,
            'Sore Throat':sore_throat,
            'Diarrhea':diarrhea,
            'Chills':chills,
            'Headache':headache,
            'Vomiting':vomiting
        }
     
        return render(request,"result.html",{'result':result,'user_details_API':user_details_API,
                        'user_json_data':json.dumps(user_details_API)})
    else:
        return render(request,"index.html")