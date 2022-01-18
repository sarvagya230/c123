contact=[
    {
        'name':"Robin",
        'lastName':"TheBank",
        "contact":"+91 911"
    },
        {
        'name':"smith",
        'lastName':"swiss",
        "contact":"+91 100"
    },
    {
        'name':"charak",
        'lastName':"singh",
        "contact":"+91 898968985210"
    },
    {
        "name":"ayush",
        "contact":"+91 42056956"
    }
]
from unicodedata import name
from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")

def lol():
    return render_template("index.html",contact=contact) 
if("__name__==__main__"):
    app.run(debug=True)    