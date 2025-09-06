from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Taap_acc(BaseModel):
    Hour: int
    Day: int 
    LatBin: float 
    LonBin: float