from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.calculation_endpoints import router as calculation_router

# command uvicorn main:app --reload 
#App object 
app = FastAPI()

origins = ['http://localhost:3000', 'http://localhost:5173']

#permissions for cors that will allow communication between the front end and the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculation_router)