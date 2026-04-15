from fastapi import FastAPI, Request, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


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

@app.get("/", include_in_schema=False, name="home")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", context={"posts": posts, "title": "Home"})

@app.get("/posts")
def get_posts():
    return {"data": posts}

@app.get("/posts/{post_id}")
def get_posts(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return {"data": post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")

@app.get("/post/{post_id}", include_in_schema=False)
def get_post(request: Request, post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return templates.TemplateResponse(request, "post.html",
                                              context={"post": post, "title": {post['title']}})
    return templates.TemplateResponse(request, "error.html",
                                        context={"message": "Post not found", "status_code": 404})