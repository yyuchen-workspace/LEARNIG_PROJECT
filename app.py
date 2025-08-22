from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 暫時用 list 儲存任務（第2週會改用資料庫）
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_title = request.form.get('title')
    if task_title:
        new_task = {'title': task_title, 'completed' : False}
        tasks.append(new_task)
    
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id <= len(tasks) - 1: #索引從0開始所以長度要-1
        tasks.pop(task_id)
        
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if task_id:
        tasks[task_id]['completed'] = True
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)