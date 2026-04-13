import uuid
from fastapi import APIRouter, Depends, HTTPException,Cookie, BackgroundTasks
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import Session
from FAST.db.database import get_db, SessionLocal
from models.story import Story, StoryNode
from models.job import StoryJob
from schemas.story import (CompleteStoryResponse, CreateStoryRequest, CompleteStoryResponse)
from schemas.job import StoryJobCreate, StoryJobResponse
router = APIRouter(prefix="/story", tags=["story"])

def get_session_id(session_id: Optional[str] = Cookie(None)) -> str:
    if not session_id:
        session_id = str(uuid.uuid4())
    return session_id
@router.post("/create", response_model=StoryJobResponse)
def create_story(request: CreateStoryRequest, 
                session_id: str = Depends(get_session_id),
                 db: Session = Depends(get_db), 
                 background_tasks: BackgroundTasks,

):
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    job_id = str(uuid.uuid4())
    job = StoryJob(job_id=job_id, session_id=session_id, theme=request.theme, status="pending")

    db.add(job)
    db.commit()

    background_tasks.add_task(
        generate_story_task, 
        job_id = job_id, 
        theme = request.theme,
        session_id = session_id
    )

    return job
def generate_story_task(job_id: str, session_id: str, theme: str):
    db = SessionLocal()
    try:
        job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()
        if not job:
            return
        try:
            job.status = "running"
            db.commit()
            story ={}
            job.story_id = story.id
            job.status = "completed"
            job.completed_at = datetime.now()
            db.commit()
        except Exception as e:
            job.status = "failed"
            job.completed_at = datetime.now()
            job.error = str(e)
            db.commit()
    finally:
        db.close()

@router.get(path="/get/{story_id}/complete", response_model=CompleteStoryResponse)
def get_complete_story(story_id: int, db: Session = Depends(get_db)):
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Job not found")
    return story

            
       




