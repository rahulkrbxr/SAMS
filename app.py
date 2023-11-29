from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/student/")
def student_login():
  return render_template('student_login.html')


@app.route("/admin/")
def admin_login():
  return render_template('admin_login.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
