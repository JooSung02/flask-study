from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        message = f"안녕하세요, {name}님!"
        return render_template('result.html', message=message)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(port=5008)


