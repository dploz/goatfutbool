from flask import Flask 
from flask import render_template

app=Flask(__name__)

@app.route("/")
def incio():
    return render_template("/index.html")


@app.route("sitio/libros")
def libros():
    return render_template("/libros.html")



if __name__=="__main__":
    app.run(debug=True)
