import string

import pydantic
from typing import Optional

class User(pydantic.BaseModel):
    username: str
    password: str
    age: int
    score: float
    email:Optional[str]
    phone_number: Optional[str]

    @pydantic.validator("username")
    @classmethod
    def username_valid(cls,value):
        if any(p in value for p in string.punctuation):
            raise ValueError("Username não podera incluir puntuação")
        else:
            return  value

    @pydantic.validator("password")
    @classmethod
    def password_valid(cls,value):
        if value <= 8:
            raise  ValueError("Password deverá conter o minimo de 8 carascteres")
        if any(p in value for p in string.punctuation):
            if any(d in value for d in string.digits):
                if any(l in value for l in string.ascii_lowercase):
                    if any(u in value for u in string.ascii_uppercase):
                        return  value

        raise  ValueError(" Password deverá conter ao menos uma caracter esspecial,número, letra minúscula e letra maiúscula")

    @pydantic.validator("age", "score")
    @classmethod
    def number_valid(cls,value):
        if value > 0 :
            return  value
        else:
            raise  ValueError("Número deverá maior que zero")

    @pydantic.root_validator(pre=True)
    @classmethod
    def validate_phone_or_email(cls,values):
        if "email" in values or "phone_number" in values:
            return  values
        else:
            raise ValueError("Deverá ser fornecido  pelo menos um deles")



user1 = User(username="john1.",password="aaaa", age=31,score=12.3)