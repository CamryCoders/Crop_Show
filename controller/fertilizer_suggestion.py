from flask import request,jsonify
def fertilizer_suggestion():
    data=request.get_json()
    N=int(data.get("N"))
    K=int(data.get("K"))
    P=int(data.get("P"))

    suggestions = []

    if N < 50:
        suggestions.append({
            "msg":"Nitrogen is low. Consider nitrogen-rich fertilizer."
        }) 
    if P < 40:
        suggestions.append({
            "msg":"Phosphorus is low. Consider phosphate fertilizer."
        })
        
    if K < 40:
        suggestions.append({
                    "msg":"Potassium is low. Consider potassium-rich fertilizer."
                })
         
        
    if len(suggestions) == 0:
        suggestions.append({
                            "msg":"NPK levels appear to be adequate."
                        })
        
    print(suggestions)
        

    return suggestions


