from flask import Flask, render_template, request, redirect

app=Flask(__name__, template_folder='template')
    
# deleted STUDENTS = {}
COMPANY = {}
# deleted COURSES = ['Python', 'Web', 'Blockchain', 'UI']

@app.route("/", methods=["GET", "POST"])
def Search_Company():
    if request.method == "POST":
        name = request.form["name"]
        company = request.form.get("company") 
        COMPANY[name] = company
        return redirect("/ticker")

    else:
        return render_template("form.html")

@app.route("/ticker", methods=["GET", "POST"])
def Search_Ticker():
    if request.method == "POST":
        name = request.form["name"]
        ticker = request.form.get("ticker") 
        COMPANY[name] = ticker
        return redirect("/company")

    else:
        return render_template("tickerform.html")


@app.route("/company", methods=["GET", "POST"])
def company_info():
    #company = request.args.get()
    return render_template("company.html", company=COMPANY)

if __name__=="__main__":
    app.run(port=5001, debug=True)