from flask import Flask, render_template

app = Flask(__name__)

@app.route('/users')
def users():
    user_list = ['Alice', 'Bob', 'Charlie', 'David']
    return render_template('users.html', users=user_list)

if __name__ == '__main__':
    app.run(port=5002)
