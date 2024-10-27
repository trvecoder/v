from flask import Flask, render_template, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# List of love notes
love_notes = [
    "✦•┈๑⋅⋯ ⋯⋅๑┈•✦",
    "TUTUTUTUTUTUTUUTUT", 
    "you're the most amazing, sweetest, kindest, most beautiful person ever and i'm so glad to have you in my life",
    "your smile makes me go SDHKAJDHAKJDH",
    "you make me so fucking happy varsh", 
    "i wanna kiss you in the rain :'3", 
    "i love listening to your voice <3", 
    "YAP MORE >.<",
    "you beautiful ass mf, i want you (bad)",
    "im sooo glad kristen made dat gc ong", 
    "you make days happier ily <3", 
    "youre so lovable its crayc", 
    "youre so fkn cute i just wanna kiss you all day", 
    "making you mushroom soup one day promis", 
    "everyday, you make me want to live even more", 
    "im always here to listen :D",
    "I DONT WANNA WORK I WANT MY HUSBAND WAAAAA" ,
    "FUCK YOURE SOOOOOO ASDJLA no words onl",
    "im always here for you bby", 
    "talking to you is always the best part of my day mwaa", 
    "MANY MANY MANY MANY KISSES 4 U :33333 MWAHHHH", 
    "RANT TO ME I LIKE THE SOUND I LIKE YOUR VOICE I", 
    "will u... get freaky w me 🥺🥺🥺", 
    "I REALLY REALLY REALLY REALLY REALLY LIKE YOU so fucking much dont ever question this ill beat u up >:(", 
    "everything about you is so likeable", 
    "YOU MAKE MY HEART GO DGDGDGDGDGDGDGDG 1231283 BPM ", 
    "im so glad you exist <3", 
    "can u call me a good boy and peg me", 
    "i hope theres not a day i make you feel like youre not good enough", 
    "you deserve all the love you get, and more <3",
    "sadi..krlo..mer se 🥺🥺🥺",
    "you have the prettiest smile most gorgeoefuwif",
    "id kill for that smile", 
    "i watch your highlights w my right hand strokin hard", 
    "ILY HUSBAND :3", 
    "IM SO PROUD OF YOU", 
    "I WISH I COULD SEE YOU EVERYDAY MF", 
    "i cant wait to meet you :3", 
    "BREKUP NHII KRO MUJHSE WWAAAAAA", 
    "SEND ME MORE PICS OF YOU", 
    "CLASICAL DANS VIDS DKIHAOOOOOO", 
    "you have no fkn idea how happy you make me", 
    "i wish i could just cuddle w you all day yaar varshh", 
    "im gna bite ur cutu ahh", 
    "you can talk to me anyt you feel low bby", 
    "IM ALWAYS ALWAYS ALWAYS HERE",
    "NO MATTER WHAT",
    'ILL ALWAYS CARE FOR YOU',
    "BOHT ZYADA",
    "YOURE SOOOO",
    "PLEASEEE TALK TO ME KABHI BHI",
    "I WANNA BE THERE FOR YOUR HIGHS AND LOWS",
    "achha vars ly bby",
    "thank u for letting me hit :pp"
]

@app.route('/')
def home():
    # If the index is not initialized, start with "click me :3"
    if 'note_index' not in session:
        session['note_index'] = -1  # Start with -1 to show the initial note

    # Show "click me :3" for the first visit
    if session['note_index'] == -1:
        note = "⎛⎝ ≽ > ⩊ < ≼ ⎠⎞"
    else:
        # Otherwise, display the note from the list
        note = love_notes[session['note_index']]

    return render_template('index.html', note=note)

@app.route('/get_note', methods=['POST'])
def get_note():
    # Move to the next note
    if 'note_index' in session:
        session['note_index'] += 1

    # Reset to 0 if the end of the list is reached
    if session['note_index'] >= len(love_notes):
        session['note_index'] = 0

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
