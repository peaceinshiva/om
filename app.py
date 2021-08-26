from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def kfljfsj():
    return render_template("omp.html")

@app.route('/prakash',methods=['GET','POST'])
def jkdsgfk():
    
    if(request.method=='POST'):
        
        n1=int(request.form['a'])
        n2=int(request.form['b'])
        
        x=n1+n2
        return render_template("omp.html", op=x)
    
if __name__=='__main__':
    app.run()