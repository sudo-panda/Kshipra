from flask import Flask,render_template,request,redirect,url_for
import call_nn
import random
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/lite")
def lite():
    try:
        err = request.args['error']
    except:
        err='0'
    try:
        rr = request.args['result']
    except:
        rr='-1'
    return render_template("lite.html",error=err,r=rr)

@app.route("/live")
def live():
    try:
        err = request.args['error']
    except:
        err='0'
    try:
        rr = request.args['result']
    except:
        rr='-1'
    rn=random.randint(0,5)
    names=[["Baidyanath Kundu","Anish Biswas","Aryaman Pande"],["Baidyanath Kundu","Aryaman Pande","Anish Biswas"],["Aryaman Pande","Baidyanath Kundu","Anish Biswas"],["Anish Biswas","Baidyanath Kundu","Aryaman Pande"],["Aryaman Pande","Anish Biswas","Baidyanath Kundu"],["Anish Biswas","Aryaman Pande","Baidyanath Kundu"]]
    return render_template("live.html",error=err,name=names[rn],r=rr)

@app.route('/res', methods=['POST'])
def my_form_result():
    X=request.form['latitude']
    Y=request.form['longitude']
    return my_form_lite(X,Y)

def my_form_lite(X,Y):
    try:
        X=float(X)
        try:
            Y=float(Y)
            try:
                res=call_nn.populate(X,Y)
                if(res==-1):
                    print("Error")
                    return redirect(url_for('.lite', lat=str(X),long=str(Y),error='2',result='-1'))
                try:
                    return redirect(url_for('.lite', lat=str(X),long=str(Y),error='0',result=str(res)))
                except Exception as e:
                    print("Error",e)
                    return redirect(url_for('.lite', lat=str(X),long=str(Y),error='2',result='-1'))
            except Exception as e:
                print("Error while calling function")
                return redirect(url_for('.lite', lat=str(X),long=str(Y),error='2',result='-1'))
        except:
            print(Y)
            return redirect(url_for('.lite', lat=str(X),long=str(Y),error='1',result='-1'))
    except:
        print(X)
        return redirect(url_for('.lite', lat=str(X),long=str(Y),error='1',result='-1'))

@app.route('/result', methods=['POST'])
def my_form_res():
    X=request.form['latitude']
    Y=request.form['longitude']
    return my_form_live(X,Y)

def my_form_live(X,Y):
    try:
        X=float(X)
        try:
            Y=float(Y)
            try:
                res=call_nn.populate(X,Y)
                if(res==-1):
                    print("Error")
                    return redirect(url_for('.live', lat=str(X),long=str(Y),error='2',result='-1'))
                try:
                    return redirect(url_for('.live', lat=str(X),long=str(Y),error='0',result=str(res)))
                except Exception as e:
                    print("Error",e)
                    return redirect(url_for('.live', lat=str(X),long=str(Y),error='2',result='-1'))
            except Exception as e:
                print("Error while calling function")
                return redirect(url_for('.live', lat=str(X),long=str(Y),error='2',result='-1'))
        except:
            print(Y)
            return redirect(url_for('.live', lat=str(X),long=str(Y),error='1',result='-1'))
    except:
        print(Y)
        return redirect(url_for('.live', lat=str(X),long=str(Y),error='1',result='-1'))

@app.route('/result')
def result():
    return render_template('lite.html',error='0',result='-1')


@app.route('/res')
def res():
    return render_template('lite.html',error='0',r='-1')

if __name__ == "__main__":
    app.run(debug=True)