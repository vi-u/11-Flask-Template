from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/blogs/<int:id>')
def blogs(id):
    return render_template('blog.html', number=id)
 
app.run(host='localhost', port=5000)
