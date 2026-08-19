from flask import Blueprint
from middleware.validate_input import validate_input 
from controller.prob_chart import show_prediction_chart
from controller.crop_recommend import cropRecommend
from controller.Top3_recommend import top_3_crops
from controller.fertilizer_suggestion import fertilizer_suggestion

crop_routes =Blueprint(
    "crop_routes",
    __name__
)
crop_routes.route(
    "/crop_recommendation",
    methods=["POST"]
)(validate_input(cropRecommend))
# @validate_input
# def predict():
    
#     return cropRecommend()

crop_routes.route(
    "/prob_chart",
    methods=["POST"]
)(show_prediction_chart)

crop_routes.route(
    "/Top_3_crop",
    methods=["POST"]
)(top_3_crops)
crop_routes.route(
    "/fertilizer_suggestion",
    methods=["POST"]
)(fertilizer_suggestion)