from pydantic import BaseModel
# 2. Class which describes features of Taap
class Taap_acc(BaseModel):
    Hour: int
    Day: int 
    LatBin: float 
    LonBin: float
