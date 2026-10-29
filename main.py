from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfloMvUTyWpJ8y2DgJsvf1zsviqbGrC8e-tQ58rs7uMGBLcWwujO4yPAo&s=10"
# image = "https://img.magnific.com/free-photo/closeup-shot-beautiful-butterfly-with-interesting-textures-orange-petaled-flower_181624-7640.jpg?semt=ais_hybrid&w=740&q=80"
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

@app.get("/image", response_class=HTMLResponse)
def get_images():
    return f"""
    <h1>Images</h1>
    <img src="{image}" width="200" alt="cat">
    """

@app.get("/contact")
def home():
    return {
        "Message" : "Contact page"
    }