from flask import Flask
app = Flask(__name__)
#import enchant
import random

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/dictionary/<myword>')
def show_user_dict(myword):
    # show the user profile for that user
    #d = enchant.request_dict("en_US")
    #my = d.suggest(myword)
    my = ['hey']
     
    return 'suggestions {}'.format(my)


@app.route("/")
def hello():
    import enchant

    my_unused_variable = """<html>
    <body>
    <div style="background:red">
    <h1>WHATUP </h1>
    </div>
    <div style="background:#CCF">
    <h1>falafael </h1>
    </div>
    </body>
    </html>"""

    myhtmlstring = "poop"
    for poop in range(random.randint(1,10)):
        myhtmlstring = myhtmlstring + str(poop)

    return myhtmlstring

if __name__ == "__main__":
    app.run()