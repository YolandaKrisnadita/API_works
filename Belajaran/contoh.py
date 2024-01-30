from fastapi import FastAPI,HTTPException,Header
import pandas as pd 

df=pd.read_csv('Financials.csv')
app=FastAPI()
API_KEY="testingAPI4567"

@app.get("/")
def home():
    return{'Message':'This is my API. Welcome'}

@app.get("/protected/{pos}")
def protect(pos:str,api_key:str=Header(None)):
    if API_KEY is None or API_KEY!= API_KEY:
        raise HTTPException(status_code=401,detail="API yang dimasukan salah, coy")
    else:
        return df[df['Country']==pos].to_dict(orient='records')
