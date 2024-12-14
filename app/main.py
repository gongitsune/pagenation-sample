from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from app.initial_data import init
from app.routes import router
from app.db import engine
from app.models import *  # noqa: F403
from app.models import SQLModel

app = FastAPI(title="PagenationExample")
app.include_router(router)

# 初期データを投入
SQLModel.metadata.create_all(engine)
maker = sessionmaker(bind=engine)
session = maker()
init(session)
session.commit()
