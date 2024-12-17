from pydantic import BaseModel, field_validator
from typing import Optional
from fastapi import HTTPException

class Pelicula(BaseModel):
    title: str
    año: int
    imdbID: str
    presupuesto: Optional[str] = None

    @field_validator('title')
    def validar_titulo_unico(cls, v):
        
        if v in peliculas:
            raise HTTPException(status_code=400, detail=f"La película '{v}' ya está en el catálogo.")
        
        return v

    class Config:
        from_attributes = True
