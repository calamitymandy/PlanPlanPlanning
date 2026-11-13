from datetime import datetime
from sqlmodel import SQLModel, Field

class Place(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nom: str

class Space(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nom: str
    place_id: int = Field(foreign_key="place.id")