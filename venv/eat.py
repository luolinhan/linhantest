from flask import Flask, request, render_template, redirect, url_for
import time

app = Flask(__name__, template_folder='.')

users = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', says=users)

    else:

        text = request.form.get('say')
        title = request.form.get('say_title')
        user = request.form.get('say_user')
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        if not title or not text or not user or not date or len(title) < 1 or len(text) < 1:
            print('Invalid input.')
            return redirect(url_for('index'))  # 回主页

        users.append({"title": title,
                      "text": text,
                      "user": user,
                      "date": date})

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='192.168.1.132', port=5000, )
