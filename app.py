from flask import Flask , render_template

app = Flask(__name__)



@app.route('/')
def indix():
    return render_template('indix.html')

@app.route('/post')
def post():
    all_post = [ 
    {
        'title':'post 1',
        'content': 'this is the content of post 1',
    },
      {
        'title':'post 2',
        'content': 'this is the content of post 2'
    }
    ]
    return render_template('post.html', post=all_post)

@app.route("/home/<string:name>/<int:id>")
def hello(name , id):
    return "hello ," + name + "  " + "  youre id is  : " + "  " + str(id)

@app.route("/onlyget" , methods=['GET'])
def get_Only():
    return "you can only get this webPage . 3"

if __name__ == "__main__":
    app.run(debug=True)
    
