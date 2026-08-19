from flask import Flask,jsonify
import time
from flask_cors import CORS
start =time.time()
print("INDEX: started",start)
from routes.crop_routes import crop_routes
print("INDEX: routes imported",time.time()-start)

def create_app():
    app=Flask(__name__)

    CORS(app,
         origins=["https://cropshow.vercel.app","http:localhost:5173"])
    app.register_blueprint(
        crop_routes,
        url_prefix="/api/crop"
    )
    # Test the server
    @app.route("/test",
        methods=["POST"]
    )
    def crop_recommend():
        return {
            "message":"route and server is working"
        }
    

    return app
app=create_app()