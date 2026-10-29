from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "Message" : "Hello From FastAPI on Render..."
    }

@app.get("/users")
def get_users():
    return [
        {
            "name" : "Raj",
            "Role" : "Admin"
        },
        {
            "name" : "Vraj",
            "Role" : "Employee"
        }
    ]

