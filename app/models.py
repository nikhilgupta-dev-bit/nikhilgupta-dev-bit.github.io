from pydantic import BaseModel, EmailStr
from typing import Optional, List

class ProjectBase(BaseModel):
    title: str
    description: str
    technologies: List[str]
    image_url: Optional[str] = None
    video_url: Optional[str] = None
    github_url: Optional[str] = None
    project_url: Optional[str] = None

class Project(ProjectBase):
    id: int
