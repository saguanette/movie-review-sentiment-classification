from pydantic import BaseModel, Field


class ReviewRequest(BaseModel):
    review: str = Field(..., title = "Moview Review", max_length=10000)