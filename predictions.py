import joblib
import pandas as pd
import numpy as np


# # Load the model and scaler
model = joblib.load('model/rental_trained.joblib')
scaler = joblib.load('model/rental_scaler.joblib')

# Load name mapping dictionaries
city_name_mapping = joblib.load('model/city_name_mapping.joblib')
area_type_name_mapping = joblib.load('model/area_type_name_mapping.joblib')
furnishing_status_name_mapping = joblib.load('model/furnishing_status_name_mapping.joblib')
point_of_contact_name_mapping = joblib.load('model/point_of_contact_name_mapping.joblib')
posted_on_name_mapping = joblib.load('model/posted_on_name_mapping.joblib')
tenant_preferred_name_mapping = joblib.load('model/tenant_preferred_name_mapping.joblib')


# Create funciton to take in a df and return a predicted rental price
def predict(df):

    # Scale the df
    pred_scaled = scaler.transform(df)

    # Predict and display pridiction
    prediction = model.predict(pred_scaled).round(2)
    return(float(prediction))

# Initial variable 
continue_prediction = "yes"

# While we want to continue predicting
while continue_prediction == "yes":

    posted_on = 2

    # Ask the user how many bhk's

    print("-----------------------------------------------")
    print("-----------------------------------------------")
    print("-----------------------------------------------")
    print("Welcome to the app for predicting rental value")
    print("-----------------------------------------------")
    print("-----------------------------------------------")
    print("-----------------------------------------------")
    print()
    
    print('How many bathrooms, hallways and kitchen spaces are required?')
    print()
    bhk = int(input("Please enter a number between 1 and 5: "))

    print("-----------------------------------------------")
    print()

    print('Enter in the size of the property in Square Feet.')
    print()
    size = int(input("Enter number between 200 and 1500: "))

    print("-----------------------------------------------")
    print()

    print('Enter the area type (base on size of the property)')
    print()
    for x in area_type_name_mapping:
        print(f"For {x}, Enter {area_type_name_mapping[x]}")
    print()   
    area_type = int(input("Enter area type No.: "))
    

    print("-----------------------------------------------")
    print()

    print('Enter City the property needs to be located in.')
    print()
    for x in city_name_mapping:
        print(f"For {x}, Enter {city_name_mapping[x]}")
    print()        
    city = int(input("Enter City No.: "))

    print("-----------------------------------------------")
    print()

    print('Enter the property furnishing status.')
    print()
    for x in furnishing_status_name_mapping:
        print(f"For {x}, Enter {furnishing_status_name_mapping[x]}")
    print()
    furnishing_status = int(input("Enter furnishing status No.: "))

    print("-----------------------------------------------")
    print()

    print('Enter the preferred tenant type.')
    print()
    for x in tenant_preferred_name_mapping:
        print(f"For {x}, Enter {tenant_preferred_name_mapping[x]}")
    print()
    tenant_preferred = int(input("Enter preferred tenant No.: "))

    print("-----------------------------------------------")
    print()

    print('Enter the number of bathrooms required.')
    print()
    bathroom = int(input("Enter a number between 1 and 4: "))

    print("-----------------------------------------------")
    print()

    print('Enter the preferred point of contact.')
    print()
    for x in point_of_contact_name_mapping:
        print(f"For {x}, Enter {point_of_contact_name_mapping[x]}")
    print()
    point_of_contact = int(input("Enter point of contact No.: "))
    

    data = [{'posted_on':posted_on, 'bhk':bhk, 'size':size, 'area_type':area_type, 'city':city, 'furnishing_status':furnishing_status,
       'tenant_preferred':tenant_preferred, 'bathroom':bathroom, 'point_of_contact':point_of_contact}]

    df = pd.DataFrame(data)

    pred = predict(df)

    print("--------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------")
    print(f"The predicted rental value, based on the parameters entered, is {pred}")
    print("--------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------")

    # Once complete...
    continue_prediction = input("Would you like to predict based on other parameters: 'yes' or 'no'? ")

print()
print()
print()
print('------------------------------')
print('Thank you for using this app..')
print('------------------------------')