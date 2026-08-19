from flask import Flask,request,jsonify
from pathlib import Path
import tensorflow as tf
import time
start=time.time()
print("Before load",start)
from load_data import model,scaler,label_encoder
print("After load",time.time()-start)
import numpy as np
import random
import time


def cropRecommend():
    start = time.time()
    print("CONTROLLER STARTED")
    
    data=request.get_json()
    print("After input extraction:", time.time() - start)

    input_data=np.array([
        [data.get("N"),
         data.get("P"),
         data.get("K"),
         data.get("temperature"),
         data.get("humidity"),
         data.get("ph"),
         data.get("rainfall"),]
    ])

    input_scaled=scaler.transform(input_data,)
    print("After scaling:", time.time() - start)
    probabilities = model.predict(input_scaled, verbose=0)[0]
    print("After prediction:", time.time() - start)
    predicted_index = np.argmax(probabilities)
    crop = label_encoder.inverse_transform(
        [predicted_index]
    )[0]
    print("After decoding:", time.time() - start)

    confidence = probabilities[predicted_index] * 100

    ans=[]
    ans.append({
        "crop":crop,
        "confidence":confidence
    })
    print("crop",crop, "  confidence",confidence)
    crop_image={
        "apple":[
            "https://img.magnific.com/free-photo/apple-orchard_342744-1013.jpg?semt=ais_hybrid&w=740&q=80",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS152Xf50Yx0Ow_M2ENoXbYeFbKppVPU9OTe8aNCkf4Dvl2CvNQ-_mqISs&s=10"
        ],
        "banana":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtxSnPKLb7RSKOqq8ZzrLwCBqhTB9RmBLJcYWB2AIijQSAprVydh1GzZrD&s=10",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRp3V8MK6z5qEg686gWs5mhtxkdwImtZOOqM44zqhG7skN4vRKQYyWom4ij&s=10"
        ],
        "blackgram":["https://novelseeds.com/wp-content/uploads/2025/01/Untitled-design-96.png"
                     ,"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQCr2Ap-QI2vLSSqPgjdZWxZFkmE8Q19pv0UR3UrEOsa51wCRBfsQM2-s&s=10"
        ],
        "chickpea":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSr3-ak4ieb0mOwpp69Xw-4dzwsaanO9DkWDCWilZRDSTbV5RFDNoy7ueg&s=10",
                    "https://st4.depositphotos.com/10194092/28752/i/450/depositphotos_287521290-stock-photo-chickpea-cicer-arietinum-leguminous-legume.jpg"],
        "coconut":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6o8YcFB42xhGMFKt7eKSbSo0NlNgsVIXWNcLjr1TcCzlrzjGW2La5c58&s=10",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCHl_dASCPF_18bcNA976bve95iJ12Ruuucedkn5wP_VbOxgPFrz0KuV28&s=10"],
        "coffee":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbiH-p2uNwXdvcKfC2gTvd9pXiTEBiQR_UCIIlAq4gRXNTK_F3AGHk65ZZ&s=10",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtAp-zcthy9_knJub74pT-uZr8UNsM8ez9iaakc2YfrA&s=10"],
        "cotton":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQupUD4cmmd7kdTdfDEwh3pegV7j6FVQt0GlMW78jHiGqd2X7elonuIcoA&s=10",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsXVl_SVlc7rHOULRJxcvg9VzunQg9Y2UYcg0l5tk-DHIfAtVQ2JwknJH_&s=10"],
        "grapes":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjaUNJHuw6bQkZADv2ZXvMKA5jufzlld9pZ4X-YFSQyJtF3Fl21FCf8Bo&s=10",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTtagbe25Y9zWx7Kz-zu3L81LWuy8DTEpFPkgOXR2dUZ1oBb7Zdydlo44&s=10"],
        "jute":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzQktdJweSarLXzB3NDOmX1lsn_2eZJeBba4r9v8FkUH-ZCnysBfrVIgul&s=10",
                  "https://t4.ftcdn.net/jpg/03/09/09/89/360_F_309098926_9nbiDQvEeVMyJZbxH7koU4RWFoC7v50v.jpg"],
        "kidneybea":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSz4lP09okwJ5kARwVvXHyAwIEDtWJBXjYsXmm_1pyvaw&s=10",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQb-TBi9OKfPiS80PrP4erq3P85KRaeKFYYM64JdeZtRfjNjraUQgV3xxLC&s=10"],
        "lentil":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRh-k7e6D147BVEL5U2yt0ojCFSqF5d_HpVomF-z4w_LmXp63MPnwrjhRPr&s=10",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYkJ2zsfMdKULMMmWPxFHfrleDio08Tx07BYE4h7fC913pE46tlG2vqWS8&s=10"],
        "maize":["https://thumbs.dreamstime.com/b/different-corn-plantation-524311.jpg",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmdA4ta1SgyXWDeFElIoOhE5ik3hkw1QaL_L_I06pV4vaMRi5wKSCE8_M&s=10"],
        "mango":["https://www.newnessplant.com/uploads/a30fb6611d14de2932c2dd4ff06ce932.jpg",
                  "https://thumbs.dreamstime.com/b/mango-crop-49272.jpg"],
        "mothbeans":["https://nishamadhulika.com/imgpst/featured/moth-beans.jpg",
                  "https://cpimg.tistatic.com/07379664/b/4/Moth-Beans.jpg"],
        "mungbean":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSETxjuf5WvLbmRQ56aoTMxOLkX_bWSsU7THuX1ytH7CA&s=10",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSuoYW79emleWtk_fhAmhJkM3eRyuqqzMF88KzHSrFs4enIe23mzsp1NM&s=10"],
        "muskmelon":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8fpykmBIB5vhqO6RGC2vsS8GqNstAlvnNFaFgAwqQs3oMFgWnU8a6sJ1S&s=10",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT9iRZbM62kGOwZ4cYdhF04G9OeWaVKnqSCIsnixMiKCN7xAW_3gzvOe2R&s=10"],
        "orange":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRD8WrkSP9TvTo5K2W66V5xtO8Y51w_Wa9S8eihjVWzBQ&s=10",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6Y-2j9d8npxSNABB2lCOFrWnkp8IV3P5IQr6jwxcTGCRZRDk9_FuORW5w&s=10"],
        "papaya":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsc7sRXe78CQ0V_UTz8j_bcS5YER5BvWFGam7ULHt7V0wvoJVAWngA3nyO&s=10",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0Zu4RwF1rPhXd42QdQqJ_CrE9Ulafjukz4r5XqSMVZw&s=10"],
        "pigeonpeas":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS73bI64rAwDhz7QYgU2X3eDZvUCt-AXo8ulapAJkeCjq80Um4fkpy5IzM&s=10",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG3FSAHfD_Jk0yU_vyN6kZQC7FI8ICIV3KIdr46cqu1xZtUE7aU98Sqotb&s=10"],
        "pomegranate":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjrxKdyC1J_6471ESNSHY4KQGngQzG6jK31CY9HQ2b5g&s=10",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6py_KL9R2j2f_w7L7OoXcVv9JquGUQ-nZJ-ktau_ggHD_cXhnD_GwQgSJ&s=10"],
        "rice":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRao4aeVeF2Ujo5n-w6j-21ykEy5Lk20bMg7jvRJn-3RFTu0LwHmN40rI2S&s=10",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQ5vxQqEHl97PdnSZlBseqYXrb2zB1VFZaVTcCTUyuaA&s=10"],
        "watermelon":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-cWlBa7P4EEjlcil9hcuLtPp4jm9oGXBvuR1viUGUPQ&s=10",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiFmRowqpp2uhqxo98rhS1A7ZfRkC_IkRh9EkYMT5ytA&s=10"],
    }
    index=random.randint(0,1)
    print("BEFORE RETURN:", time.time() - start)
   

    return jsonify({
        "crop":str(crop),
        "confidence":round(float(confidence),1),
        "url":crop_image[crop][index]

    })