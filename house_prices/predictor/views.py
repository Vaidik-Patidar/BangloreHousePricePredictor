from django.shortcuts import render

# Create your views here.
import json
import pickle
import numpy as np

# Load the model 
model = pickle.load(open('predictor/model.pickle', 'rb'))

# Load the columns
with open('predictor/columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']

location_columns = [col for col in data_columns if col not in ['total_sqft', 'bath', 'bhk']]    

def home(request):
    return render(request, 'home.html' , {'locations': location_columns})

def predict_price(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        sqft = float(request.POST.get('sqft'))
        bath = int(request.POST.get('bath'))
        bhk = int(request.POST.get('bhk'))

        # Create a zero array for the input features
        x = np.zeros(len(data_columns))
        
        # Set the numerical features
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        
        # Set the location feature
        if location in data_columns:
            loc_index = data_columns.index(location)
            x[loc_index] = 1

        # Predict the price using the model
        predicted_price = model.predict([x])[0]
    
        return render(request, 'result.html', {'predicted_price': round(predicted_price, 2), 'sqft': sqft, 'bath': bath, 'bhk': bhk, 'location': location})
    else:
        return render(request, 'home.html', {'locations': location_columns})