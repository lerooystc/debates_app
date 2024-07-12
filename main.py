from fastapi import FastAPI
from core.config import settings
from db import Base
from db.session import engine
from api.base import api_router


def include_router(app : FastAPI):
    app.include_router(api_router)


def create_tables():
    print(Base)
    Base.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()

@app.get("/")
def hello():
    return "hello"

# @app.get('/ideas/{idea_id}', response_model=Idea)
# def get_idea(idea_id: int):
#     return [idea for idea in ideas if idea.id == idea_id][0]


# @app.get('/ideas', response_model=List[Idea])
# def get_ideas():
#     return ideas


# @app.post('/ideas', response_model=Idea)
# def post_ideas(idea: Idea):
#     ideas.append(idea)
#     return idea
