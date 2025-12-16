import flask

app = flask.Flask("task app")

tasks = []


@app.route("/view_tasks", methods=["get", "post"])
def view_tasks():
    if flask.request.method == "POST":
        task = flask.request.form.get("task_name")
        tasks.remove(task.strip())
    return flask.render_template("view_tasks.html", tasks=tasks)


@app.route("/add_tasks", methods=["get", "post"])
def add_tasks():
    if flask.request.method == "POST":
        task = flask.request.form.get("task")
        print(task)
        tasks.append(task)
    return flask.render_template("add_tasks.html", tasks=tasks)
