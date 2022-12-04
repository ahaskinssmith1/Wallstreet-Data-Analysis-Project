from flask import Flask, render_template, request, redirect

app=Flask(__name__,template_folder='template')
    
# deleted STUDENTS = {}
COMPANY = {}
# deleted COURSES = ['Python', 'Web', 'Blockchain', 'UI']

@app.route("/", methods=["GET", "POST"])
def Search():
    if request.method == "POST":
        name = request.form["name"]
        company = request.form.get("company") # chnage from course to comapny
        COMPANY[name] = company
        return redirect("/company")

    else:
        return render_template("form.html")


@app.route("/company")
def company_info():
    company = request.args.get()
    return render_template("company.html", company=COMPANY)

if __name__=="__main__":
    app.run(port=5001, debug=True)