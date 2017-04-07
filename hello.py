from flask import Flask
app = Flask(__name__)
#import enchant
import random
from nltk.corpus import brown

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/wordfinder/<myword>')
def show_user_dict(myword):
    brown_words = brown.words(categories='lore')

    bird_list = []
    for i in range(50):
        red_bird = brown_words[random.randint(0,10000)]
        bird_list.append(red_bird)

    return str(bird_list)



@app.route("/")
def hello():
    # import enchant

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