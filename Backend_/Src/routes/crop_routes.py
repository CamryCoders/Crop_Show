from fastapi import APIRouter

from controller.crop_recommend import cropRecommend
from controller.prob_chart import show_prediction_chart
from controller.Top3_recommend import top_3_crops
from controller.fertilizer_suggestion import fertilizer_suggestion

crop_routes=APIRouter(prefix="/api/crop",tags=["crop Analysis"])

crop_routes.post("/crop_recommendation")(cropRecommend)
crop_routes.post(
    "/prob_chart",
    
)(show_prediction_chart)

crop_routes.post(
    "/Top_3_crop",
    
)(top_3_crops)

crop_routes.post(
    "/fertilizer_suggestion",
    
)(fertilizer_suggestion)

