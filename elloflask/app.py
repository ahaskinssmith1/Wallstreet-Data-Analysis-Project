from flask import Flask, render_template, request, redirect

app=Flask(__name__,template_folder='template')
    
STUDENTS = {}

COURSES = ['Python', 'Web', 'Blockchain', 'UI']

@app.route("/form", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form.get("course")
        STUDENTS[name] = course
        return redirect("/students")

    else:
        return render_template("form.html", courses=COURSES)


@app.route("/students")
def students():
    return render_template("students.html", students=STUDENTS)

if __name__=="__main__":
    app.run(port=5001, debug=True)