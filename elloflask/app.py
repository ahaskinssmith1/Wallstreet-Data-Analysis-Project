from flask import Flask, render_template, request, redirect

app = Flask(__name__)

"""
@app.route("/")
@app.route("/hello/<name>") #if the route contains '/hello/<name>, it will tigger the function below
def hello(name=None):
    if request.method == "POST":
        city_name = request.form["city"]
        temp
    if name:
        return f'Hello, {name}!'
    else:
        return "<h1>Hello, World!</h1> <p>I am learning Flask and I love it!</p>"
    """
STUDENTS = {}

COURSES = ['Python', 'Web', 'Blockchain', 'UI']

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form.get("course")
        STUDENTS[name] = course
        return redirect("/students")

    else:
        return render_template("register-form.html", courses=COURSES)


@app.route("/students")
def students():
    return render_template("students.html", students=STUDENTS)


"""
@app.route('/square/')
@app.route("/square/<number>")
def square(number=None):
    if number:
        res = int(number) ** 2
        return str(res)
    else:
        return "You need to provide a number in the URL after /square/"
"""

if __name__=="__main__":
    app.run(port=5001, debug=True)