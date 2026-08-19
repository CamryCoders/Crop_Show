from waitress import serve
from index import app

if __name__=="__main__":
    print("Server is hoting on http://127.0.0.1:5000 ")
    serve(app,host="127.0.0.1",port=5000)
    