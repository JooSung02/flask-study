from flask import Flask, render_template

app = Flask(__name__)

@app.route('/users2')
def users():
    user_list = [
        {'name': 'Alice', 'vip': True},
        {'name': 'Bob', 'vip': False},
        {'name': 'Charlie', 'vip': True},
        {'name': 'David', 'vip': False}
    ]
    return render_template('users2.html', users=user_list)

if __name__ == '__main__':
    app.run(port=5003)
