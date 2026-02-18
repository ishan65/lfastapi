from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI blog!"}


@app.get("/htmltest", response_class=HTMLResponse, include_in_schema=False)
@app.get("/html", response_class=HTMLResponse)
def htmlhome():
    return """
        <html>
            <head>
                <title>FastAPI Blog</title>
            </head>
            <body>
                <h1>Welcome to the FastAPI blog!</h1>
            </body>
        </html>
    """


@app.get("/posts")
def get_posts():
    return {"data": posts}