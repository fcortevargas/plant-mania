from pydantic import BaseModel


class UserHomeBase(BaseModel):
    user_id: int
    home_id: int


class UserHomeCreate(UserHomeBase):
    pass


class UserHomeUpdate(UserHomeBase):
    pass


class UserHomeOut(UserHomeBase):
    pass
