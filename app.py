from flask import Flask, request, render_template_string

app = Flask(__name__)

# หน้าเว็บฟอร์ม
form_html = """
<!doctype html>
<title>Submit Message</title>
<h1>Submit your message</h1>
<form method="post">
  <textarea name="message"></textarea><br>
  <input type="submit" value="Submit">
</form>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        with open('log.txt', 'a') as f:
            f.write(message + '\n')
        return f"<h1>Message received:</h1><p>{message}</p>"
    return form_html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
