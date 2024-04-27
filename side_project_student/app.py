from flask import Flask, render_template,request,redirect

app = Flask(__name__)

students = [
    {'name':'張三','Chinese':'65','Math':'65','English':'65'},
    {'name':'李四','Chinese':'65','Math':'65','English':'65'},
    {'name':'王五','Chinese':'65','Math':'65','English':'65'},
    {'name':'趙六','Chinese':'65','Math':'65','English':'65'},
    
]



@app.route("/")
def hello_world():
    return "hello world"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username =request.form.get("username")
        password =request.form.get("password")
        return redirect('/admin')
    return render_template('login.html')


@app.route('/admin')
def admin():
    return render_template('admin.html', students=students)


@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        username = request.form.get('username')
        Chinese = request.form.get('Chinese')
        Math = request.form.get('Math')
        English = request.form.get('English')
        students.append({'name': username, 'Chinese': Chinese, 'Math': Math, 'English': English})
        return redirect('/admin')
    return render_template('add.html')


@app.route('/delete')
def delete_student():
    username = request.args.get('name')
    for stu in students:
        if stu['name'] == username:
            students.remove(stu)
    return redirect('/admin')


@app.route('/change', methods=["GET","POST"])
def change_student():
    username = request.args.get('name')
    if request.method == 'POST':
        username = request.form.get('username')
        Chinese = request.form.get('Chinese')
        Math = request.form.get('Math')
        English = request.form.get('English')
        for stu in students:
            if  stu['name'] == username:
                stu['Chinese'] == Chinese
                stu['Math'] == Math
                stu['English'] == English
        return redirect('/admin')
    for stu in students:
        if stu['name'] == username:

            return render_template('/change.html', students=stu)


if __name__ == "__main__":
    app.run(debug=True)
