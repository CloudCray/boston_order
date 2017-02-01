from flask import url_for, request, Response, Blueprint
import twilio.twiml

bp_ivr = Blueprint('ivr', __name__)


file_options = {
    "landing": "https://www.dropbox.com/s/b1getcw9shw2y0d/intro.mp3?dl=1",
    "english": "https://www.dropbox.com/s/6u1pgu3yt0b1gyk/english.mp3?dl=1",
    "arabic": "https://www.dropbox.com/s/pgo1nsfgflu5gtp/arabic.mp3?dl=1",
    "somali": "https://www.dropbox.com/s/pviynwf6f8idwcv/somali.mp3?dl=1",
    "farsi": "https://www.dropbox.com/s/3rkn1ri99frluy5/farsi.mp3?dl=1"
}


@bp_ivr.route('/ivr/welcome', methods=['POST'])
def welcome():
    response = twilio.twiml.Response()
    with response.gather(numDigits=1, action=url_for('ivr.menu'), method="POST") as g:
        g.play(url=file_options["landing"], loop=3)
    return twiml(response)


@bp_ivr.route('/ivr/menu', methods=['POST'])
def menu():
    selected_option = request.form['Digits']
    option_actions = {'1': "english",
                      '2': "arabic",
                      "3": "somali",
                      "4": "farsi"}

    if selected_option in option_actions:
        response = twilio.twiml.Response()
        play_file_then_return(response, option_actions[selected_option])
        return twiml(response)

    return _redirect_welcome()


# private methods


def play_file_then_hangup(response, language):
    response.play(file_options[language])
    response.hangup()
    return twiml(response)


def play_file_then_return(response, language):
    response.play(file_options[language])

    return _redirect_welcome(response)


def _redirect_welcome(response):
    response.say("Returning to the main menu", voice="alice", language="en-GB")
    response.redirect(url_for('ivr.welcome'))

    return twiml(response)


def twiml(resp):
    resp = Response(str(resp))
    resp.headers['Content-Type'] = 'text/xml'
    return resp
