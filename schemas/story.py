from typing import List, Optional,Dict
from pydantic import BaseModel
from datetime import datetime
class StoryOptionSchema(BaseModel):
    text: str
    node_id:Optional[int] = None

class StoryNodeBase(BaseModel):
    content: str
    is_end: bool = False
    is_winning_ending: bool = False
    

class CompleteStoryNodeResponse(StoryNodeBase):
    id: int
    options: List[StoryOptionSchema] =[]
    class Config:
        from_attributes = True
        
