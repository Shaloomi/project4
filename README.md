Project-4
-------------
Project Name: 
-------------------
Rental house price prediction Model

Project Introduction/Objective
------------------------------------------

Rent prediction for major cities in India using machine learning would involve several steps. First, data would need to be collected on factors that affect rent prices, such as location, property type, and square footage. This data would then need to be cleaned and preprocessed to prepare it for use in a machine learning model. Next, a suitable model, such as a linear regression or a decision tree, would need to be selected and trained on the data. Finally, the model would need to be evaluated and fine-tuned to improve its accuracy.

It's important to note that machine learning model is only as good as the data that it's trained on. Therefore, a comprehensive and accurate dataset is crucial for making accurate rent predictions.


Methods Used
--------------------
1. Data collection
2. Data cleaning an exploration
3. Feature encoding
4. Train-test split validation
5. Feature scaling
6. Modelling
7. Model evaluation


Technologies
-------------------
Pgadmin
Python
PostGres
Pandas, 
jupyter
Amazon RDS


Project Description
----------------------------

The purpose of this project is to develop a machine learning model using sample data. We will then train, test the model. If the model is generating accurate data then we will save the model. This saved model will then be loaded to take input from the user to make predictions to assist the user in making informed decision.


Getting Started
---------------------
Clone this repo  https://github.com/joshmartin33/project-4.

Raw Data is being kept in the Resources folder within this repo.

This project has ipynb files used to analyse and transform data.

Dependencies:
---------------------
This section lists all the libraries and software required to run the project, including specific versions.
We require Jupyter notebook, Python, Pgadmin and Googelcolab set up on to run this program.

List of all the dependencies that will need to be installed

pip install SQLAlchemy
pip install numpy
pip install Flask
pip install DateTime
pip install matplotlib
pip install pandas
pip install scikit-learn


Data:
--------

Original data is avaiable from https://www.kaggle.com/datasets/iamsouravbanerjee/house-rent-prediction-dataset
It is then downloaded in to the Resources folder on the cloned GitRepo.


Initial analysis:
---------------------
Our project start with  running the initial_analysis file. Data is read from the House_Rent_Dataset.CSV file in the Resources folder.
This will help to understand the given data and the fields and any dependencies within the column. Data is visualised for different cities according to bhk, Areatype, furnishing status and size. Also, the number of houses available for rent is shown in the picutures.


load_data:
---------------
In this file we loaded the csv file into a data frame and read all the columns and the datatypes. 'Posted on' is converted from object to datetime64 datatype.

to_rds:
---------
Setting up a connection to RDS database using config for the data. Then export rental data frame into SQL.

modelling:
---------------
 
Using the Python programming language and then Split data into test and training.Using standard scaler we scale and fit the data. The training and testing data is stored in a variable called data. The data is passed to LinearRegression, KNeighborsRegressor, RandomForestRegressor, ExtraTreesRegressor,AdaBoostRegressor to find the best performing model.

While both RandomForestRegressor and AdaBoostRegressor models have good training figures, the RandomForestRegressor model has a higher testing accuracy score. While this may not be a strong/high accuracy, 0.71 accuracy is sufficeint for our case study.

Save the model. Load the saved model to make predictions. Use the actual data to compare the data with the predicted data. If results are satisified then we will use the model further to help user to make predictions with their requirements.
 
Predictions:
-------------

For making analysis, we used predicitons.py file to run our model. To run the file , use the command 

python predictions.py

This will start the user interface. As appeared on the screen, user is required to enter the input in the range for each field. 


Results:
-----------------
This section presents the performance of the model(s) on the dataset, including any visualizations or tables that help to understand the results.

Conclusion:
-----------------
This section provides a summary of the project, including any limitations or future work.

References: 
-----------------
This section lists any sources that were used or referenced in the project.

Code: 
--------
This section contains the code and instructions on how to run the project.

Instructions on how to run Predictions.py

clone repo
use command python predictions.py
follow the screen and enter input as shown. The results will appear on the screen.



Team Members:
-----------------
Josh Martini
Archana Karri
Udeshi Pereira
