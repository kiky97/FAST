from sqlalchemy import String, Column, Integer,DateTime,ForeignKey,JSON,Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.database import Base
class Story(Base):
    __tablename__ = "stories"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    session_id = Column(String, index=True)
    created_at = Column(DateTime, server_default=func.now())
    nodes = relationship(argument="StoryNode", back_populates="story")

class StoryNode(Base):
    __tablename__ = "story_nodes"
    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id"), index=True)
    story = relationship("Story", back_populates="nodes")
    content = Column(String)
    is_root = Column(Boolean, default=False)
    is_end = Column(Boolean, default=False)
    is_winning_ending = Column(Boolean, default=False)
    options = Column(JSON, default=list)
    story = relationship("Story", back_populates="nodes")
    