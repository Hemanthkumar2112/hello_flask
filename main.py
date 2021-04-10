from flask import Flask, render_template
data = [1,2,3,4]
app=Flask(__name__)

@app.route('/' , methods = ['GET','POST'])
def index():
    return render_template('index.html' , data = data)



if __name__=="__main__":
    app.run()
    
