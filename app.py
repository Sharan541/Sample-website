from flask import Flask
app=Flask(__name__)
@app.route('/')
def first_function():
  return "<p>hai, thisis ee testing</p>"
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)