from pydantic import BaseModel


class CharacterBase(BaseModel):
    is_private: bool
    name: str
    race: str
    char_class: str
    background: str
    strength: int
    dexterity: int
    constitution: int
    wisdom: int
    intelligence: int
    charisma: int
    skills: str
    languages: str
    alignment: str

class Character(CharacterBase):
    id: int
    creator_id: int

    class Config:
        orm_mode = True

class CharacterCreate(CharacterBase):
    pass


class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int
    # username: str
    characters: list[Character] = []

    class Config:
        orm_mode = True

