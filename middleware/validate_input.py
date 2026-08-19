from flask import request

from functools import wraps
from flask import request, jsonify

def validate_input(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request body is required"
            }), 400

        required_fields = [
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall"
        ]
        for field in required_fields:
                    if field not in data:
                        return jsonify({
                            "error": f"{field} is required"
                        })


        N=int(data.get("N"))
        P=int(data.get("P"))
        K=int(data.get("K"))
        temperature=int(data.get("temperature"))
        humidity=int(data.get("humidity"))
        ph=int(data.get("ph"))
        rainfall=int(data.get("rainfall"))

        if N < 0 or P < 0 or K < 0:
            return jsonify({
                 "error":"NPK values cannot be negative"
            }) 
        

        if temperature < -50 or temperature > 60:
            return jsonify({
                             "error":"Unrealistic temperature"
                        }) 
            

        if humidity < 0 or humidity > 100:
            return jsonify({
            "error":"Humidity must be between 0 and 100"
                    }) 
            
         

        if ph < 0 or ph > 14:
            return jsonify({
                        "error":"pH must be between 0 and 14"
                            })
            

        if rainfall < 0:
            return jsonify({
                                    "error":"Rainfall cannot be negative"
                            })
         

        for field in required_fields:
            if field not in data:
                return jsonify({
                    "error": f"{field} is required"
                }), 400

        return function(*args, **kwargs)

    return wrapper

 