### this app.py file contain the server code ,,, server starts when app.run(debug=True) this runs


from flask import Flask, render_template, request ,redirect,url_for
# create a simple flask application

app = Flask(__name__) # entry point of the programm
@app.route("/", methods= ["GET"]) #methodes are GET,PUT,POST , if we dont specify by default it takes GET
def welcome():
    return "Hi Welcome"


@app.route("/index/", methods= ["GET"])
def index():
    return "It is a index page"

#variable rule


@app.route("/success/<float:score>")
def success(score):
    return f"The person has passed and the score is :  {score}" 



@app.route("/not_success/<float:score>")
def not_success(score):
    return f"The person has failed and the score is :  {score}" 


@app.route("/form", methods = ["GET","POST"])
def form():
    if request.method == 'GET':
        return render_template("form.html")
    else:
        maths = float(request.form["maths"])
        science = float(request.form["science"])
        history = float(request.form["history"])

        avg_marks = (maths+science+history) / 3
        res = ""
        if avg_marks>=70:
            return redirect(url_for('success', score = avg_marks))
            #res = success
        else:
            return redirect(url_for('not_success', score = avg_marks))
            #res = not_success

        #return redirect(url_for(res.__name__, score = avg_marks))   


        


######################################################################################################
if __name__ == "__main__":
    app.run(debug = True) # by default app.run() takes two parameter one is URL another is port ... if nothing is provided by default URL = Local host and port = 5000
    
    