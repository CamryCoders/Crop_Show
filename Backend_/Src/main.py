from fastapi import FastAPI, HTTPException,requests
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routes.crop_routes import crop_routes
from fastapi.middleware.cors import CORSMiddleware


def createApp():
    app=FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
        "https://cropshow.vercel.app",
        ]
    )
    app.include_router(crop_routes)
    @app.get("/")
    def home():
        return {
            "message":"It is homepage"
        }

    @app.get("/health")
    def health_check():
        return {
            "status":"Ok"
        }
    @app.get("/test")
    def crop_recommend():
        return JSONResponse(status_code=200,content={"message":"Server is Working"})
    

    return app

app=createApp()


