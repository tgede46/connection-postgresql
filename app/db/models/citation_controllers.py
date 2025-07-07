from typing import Annotated
from fastapi import APIRouter, HTTPException,Depends,status
from app.core.database import SessionLocal
from sqlalchemy.orm import Session
from app.db.models.citation import Citation
from pydantic import BaseModel 

router=APIRouter(
    prefix='/citation',
    tags=['citation']
)

class CitationRequest(BaseModel):
    auteur:str
    citation:str
    date:str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependancy=Annotated[Session,Depends(get_db)]

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_citation(citation: CitationRequest, db: db_dependancy):
    db_citation= Citation(
        auteur=citation.auteur,
        citation=citation.citation,
        date=citation.date
    )
    db.add(db_citation)
    db.commit()
    db.refresh(db_citation)
    return db_citation

@router.get('/',status_code=status.HTTP_200_OK)
def get_citations(db: db_dependancy):
    citation= db.query(Citation).all()
    if not citation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No citations found")
    return citation

@router.get('/{citation_id}',status_code=status.HTTP_200_OK)
def get_citation_byid(citation_id: int, db: db_dependancy):
    citation=db.query(Citation).filter(Citation.id==citation_id).first()
    if not citation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Citation not found")
    return citation

@router.delete('/{citation_id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_citation(citation_id: int, db: db_dependancy):
    citation=db.query(Citation).filter(Citation.id==citation_id).first()
    if not citation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Citation not found")
    db.delete(citation)
    db.commit()
    return {"message": "suppresion avec succes"}

@router.put('/{citation_id}',status_code=status.HTTP_200_OK)
def update_citation(citation_id: int, citation: CitationRequest, db: db_dependancy):
    db_citation = db.query(Citation).filter(Citation.id == citation_id).first()
    if not db_citation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Citation not found")
    db_citation.auteur = citation.auteur
    db_citation.citation = citation.citation
    db_citation.date = citation.date
    db.commit()
    db.refresh(db_citation)
    return db_citation