from typing import Optional
from sqlmodel import Field,SQLModel



class Citation(SQLModel,table=True):
    id :Optional[int]=Field(default=None,primary_key=True)
    auteur:str
    citation:Optional[str]=Field(default=None)
    date: str
