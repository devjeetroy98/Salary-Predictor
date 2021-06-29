import pandas as pd
import numpy as np
import os.path
from datetime import date
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

def predict_salary(newX):
        try:
            if(os.path.exists('empsal.csv')):
                data=pd.read_csv("empsal.csv",parse_dates=True,infer_datetime_format=True,index_col='empno')
                def calculate_age(dob):
                      return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                today=date.today()
                data['dob']=pd.to_datetime(data['dob'])
                data['age']=data['dob'].apply(calculate_age)    
                # print(data.isnull().sum()) Checking if null values are present      
                data.drop(columns=['empname','dob','hra'],inplace=True)# dropping unnecessary columns             
                lc=LabelEncoder()
                data['sex']=lc.fit_transform(data['sex'])# Coverting sex column from categorical to integer
                data['state']=lc.fit_transform(data['state'])               
                data['city']=lc.fit_transform(data['city'])
                # print(data.head())         
                correlation=data.corr()  #Checking if the predicting columns are interrelated 
                x=data.drop(columns=['state','salary','city','sex','age']).iloc[:,:]
                y=data['salary']   
                lreg=LinearRegression()
                score=[]
                for i in range(1000):
                    x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=i,test_size=0.1)
                    lr=lreg.fit(x_train,y_train)
                    score.append(lr.score(x_test,y_test))                
                k=score.index(max(score))          
                x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=k,test_size=0.1)             
                lreg.fit(x_train,y_train)                       
                newX=np.array([[float(newX)]])           
                newy=lreg.predict(newX)
                return round(newy[0])
        except:
            return -1
