from pydantic import BaseModel, Field


class CropInput(BaseModel):
  N: float = Field(..., ge=0, description="NPK values cannot be negative")
  P: float = Field(..., ge=0, description="NPK values cannot be negative")
  K: float = Field(..., ge=0, description="NPK values cannot be negative")

  temperature: float = Field(
      ..., ge=-50, le=60, description="Unrealistic temperature"
  )
  humidity: float = Field(
      ..., ge=0, le=100, description="Humidity must be between 0 and 100"
  )
  ph: float = Field(..., ge=0, le=14, description="pH must be between 0 and 14")
  rainfall: float = Field(..., ge=0, description="Rainfall cannot be negative")