from pydantic import BaseModel

class Car(BaseModel):
    start_point: str
    end_point: str
    # current_position:str