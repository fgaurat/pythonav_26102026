from dataclasses import dataclass

@dataclass(slots=True)
class Customer:
    id:int=0
    first_name:str=""
    last_name:str=""
    email:str=""
    gender:str=""
    ip_address:str=""