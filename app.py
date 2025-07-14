#print("Hello, World!")

from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = '''
<!doctype html>
<html>
<head><title>Greeting App</title></head>
<body>
  <h2>Enter your name:</h2>
  <form method="POST">
    <input type="text" name="name" placeholder="Your name"/>
    <input type="submit" value="Greet"/>
  </form>
  {% if name %}
    <h3>Hello, {{ name }}!</h3>
  {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def greet():
    name = None
    if request.method == "POST":
        name = request.form.get("name")
    return render_template_string(HTML_FORM, name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

