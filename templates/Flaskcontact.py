from flask import Flask, render_template, request

app= Flask("MyApp")

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "All ok"

@app.route("/")
def hello():
    return "Hello world again"

@app.route("/<name>")
def hello_someone (name):
    return render_template ("contact.html", name=name.title())



app.run(debug=True)
