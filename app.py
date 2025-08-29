from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 資料庫模型
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    priority = db.Column(db.String(20), default='medium')
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Task {self.title}>'

# 資料現在都儲存在資料庫中了！

@app.route('/')
def index():
    tasks_from_db = Task.query.all()
    return render_template('index.html', tasks=tasks_from_db)

@app.route('/add', methods=['POST'])
def add_task():
    task_title = request.form.get('title')
    task_description = request.form.get('description')
    task_priority = request.form.get('priority', 'medium')  # 預設中優先級
    task_category = request.form.get('category')  # 可以為空
    
    if task_title:
        new_task = Task(
            title=task_title, 
            description=task_description,
            priority=task_priority,
            category=task_category if task_category else None
        )
        db.session.add(new_task)
        db.session.commit() 
        
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)  # 根據 ID 查找任務
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'GET':
        return render_template('edit.html', task=task, task_id=task_id)

    new_title = request.form.get('title')
    new_description = request.form.get('description')
    new_priority = request.form.get('priority', 'medium')
    new_category = request.form.get('category')
    
    if new_title:
        # TODO(human) - 更新任務的所有欄位：title, description, priority, category
        # 提示：task.title = new_title, task.description = new_description 等等
        # 記得處理空的 category（設為 None）
        db.session.commit()
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 建立所有資料表
    app.run(debug=True)