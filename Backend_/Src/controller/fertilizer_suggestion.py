from fastapi import APIRouter
from pydantic import BaseModel, Field

router=APIRouter(prefix="/api/crop",tags=["Crop"])
class FertilizerInput(BaseModel):
  N: int=Field(...,ge=0,description="Nitrogen value")
  P: int=Field(...,ge=0,description="Phosphorus value")
  K: int=Field(...,ge=0,description="Potassium value")

@router.post("/fertilizer")
def fertilizer_suggestion(data: FertilizerInput):
  suggestions = []
  if data.N<50:
    suggestions.append(
        {"msg":"Nitrogen is low. Consider nitrogen-rich fertilizer."}
)
  if data.P<40:
    suggestions.append(
        {"msg":"Phosphorus is low. Consider phosphate fertilizer."}
         )
  if data.K<40:
    suggestions.append(
        {"msg":"Potassium is low. Consider potassium-rich fertilizer."}
)

  if len(suggestions)==0:
    suggestions.append({"msg": "NPK levels appear to be adequate."})
  print(suggestions)
  return suggestions



  



