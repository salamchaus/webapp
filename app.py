from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Azure Web Apps!"}

if __name__ == "_main_":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)