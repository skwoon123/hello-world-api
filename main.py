from fastapi import FastAPI

app = FastAPI()	#Creates the API application

@app.get("/")		#Defines an HTTP GET endpoint
def hello():		# hello() Returns a JSON response
	return {"message": "hello"} # 1st endpoint, GET returns

@app.get("/health") #Defines a health-check endpoint
def health():
	return {"status": "healthy"} #2nd endpoint, GET /health returns