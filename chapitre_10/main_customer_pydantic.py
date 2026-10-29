from pprint import pprint
from pydantic import BaseModel, field_validator, ValidationError


class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    gender: str
    ip_address: str

    @field_validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Email error')
        return v


def main():

    try:
        c = Customer(id=1, first_name="Jacques", last_name="Martin",
                     email="toto", gender="H", ip_address="127.0.0.1")
        print(c)
    except ValidationError as e:
        print(e)


if __name__ == '__main__':
    main()
