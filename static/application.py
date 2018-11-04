from flask import Flask,render_template,request
import call_nn
import random
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/lite")
def lite():
    return render_template("lite.html",error='0',r='-1')

@app.route('/lite', methods=['GET','POST'])
def my_form_lite_get():
    if request.method =='POST':
        X=request.form['lat']
        Y=request.form['long']
    else:
        X = request.args.get['lat']
        Y = request.args.get['long']
    try:
        X=float(X)
        try:
            Y=float(Y)
            try:
                res=call_nn.populate(X,Y)

                try:
                    return render_template('lite.html',error='0',r=str(res))
                except Exception as e:
                    print("Erer",e)
                    return str(e)
            except Exception as e:
                print("Error while calling function")
                return render_template("lite.html",error='2',r='-1')
        except:
            print(Y)
            return render_template("lite.html",error='1',r='-1')
    except:
        print(X)
        return render_template("lite.html",error='1',r='-1')

@app.route("/live")
def live():
    r=random.randint(0,5)
    names=[["Baidyanath Kundu","Anish Biswas","Aryaman Pande"],["Baidyanath Kundu","Aryaman Pande","Anish Biswas"],["Aryaman Pande","Baidyanath Kundu","Anish Biswas"],["Anish Biswas","Baidyanath Kundu","Aryaman Pande"],["Aryaman Pande","Anish Biswas","Baidyanath Kundu"],["Anish Biswas","Aryaman Pande","Baidyanath Kundu"]]
    return render_template("live.html",error='0',name=names[r],r='-1')
    
@app.route('/live', methods=['GET','POST'])
def my_form_live_get():
    if request.method =='POST':
        X=request.form['latitude']
        Y=request.form['longitude']
    else:
        X = request.args.get['latitude']
        Y = request.args.get['longitude']
    print(X," ",Y)
    return my_form_live(X,Y)


def my_form_live(X,Y):

    r=random.randint(0,5)
    names=[["Baidyanath Kundu","Anish Biswas","Aryaman Pande"],["Baidyanath Kundu","Aryaman Pande","Anish Biswas"],["Aryaman Pande","Baidyanath Kundu","Anish Biswas"],["Anish Biswas","Baidyanath Kundu","Aryaman Pande"],["Aryaman Pande","Anish Biswas","Baidyanath Kundu"],["Anish Biswas","Aryaman Pande","Baidyanath Kundu"]]
    
    print(Y)
    try:
        X=float(X)
        try:
            Y=float(Y)
            try:
                res=call_nn.populate(X,Y)
                try:
                    return render_template('live.html',error='0',name=names[r],r=res)
                except Exception as e:
                    print("Erer",e)
                    return str(e)
            except Exception as e:
                print("Error while calling function")
                return render_template("live.html",error='1',name=names[r],r='-1')
        except:
            print(Y)
            return render_template("live.html",error='1',name=names[r],r='-1')
    except:
        print(X)
        return render_template("live.html",error='1',name=names[r],r='-1')

@app.route('/live#error', methods=['GET','POST'])
def my_form_live_get_error():
    if request.method =='POST':
        X=request.form['latitude']
        Y=request.form['longitude']
    else:
        X = request.args.get['latitude']
        Y = request.args.get['longitude']
    return my_form_live_error(X,Y)

def my_form_live_error(X,Y):

    r=random.randint(0,5)
    names=[["Baidyanath Kundu","Anish Biswas","Aryaman Pande"],["Baidyanath Kundu","Aryaman Pande","Anish Biswas"],["Aryaman Pande","Baidyanath Kundu","Anish Biswas"],["Anish Biswas","Baidyanath Kundu","Aryaman Pande"],["Aryaman Pande","Anish Biswas","Baidyanath Kundu"],["Anish Biswas","Aryaman Pande","Baidyanath Kundu"]]
    
    print(Y)
    try:
        X=float(X)
        try:
            Y=float(Y)
            try:
                res=call_nn.populate(X,Y)
                try:
                    return render_template('live.html',error='0',name=names[r],r=str(res))
                except Exception as e:
                    print("Erer",e)
                    return str(e)
            except Exception as e:
                print("Error while calling function")
                return render_template("live.html",error='1',name=names[r],r='-1')
        except:
            print(Y)
            return render_template("live.html",error='1',name=names[r],r='-1')
    except:
        print(X)
        return render_template("live.html",error='1',name=names[r],r='-1')

if __name__ == "__main__":
    app.run(debug=True)