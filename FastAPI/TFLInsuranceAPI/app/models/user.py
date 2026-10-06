from dataclasses import dataclass

@dataclass
class User:
    user_id:int
    username:str
    email:str
    password_hash:str
    status:bool
    created_at:str
    updated_at:str