import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'sex':1, 'patient_type':1, 'intubed':1, 'pneumonia':1, 'age':30, 
                            'pregnancy':1,'diabetes':1, 'copd':1, 'asthma':1, 'inmsupr':1,'hypertension':1,
                            'other_disease':1, 'cardiovascular':1, 'obesity':1,'renal_chronic':1, 
                            'tobacco':1, 'contact_other_covid':1, 'covid_res':1, 'icu':1})

print(r.json())