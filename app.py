from flask import Flask, request, make_response
import json
import os
from flask_cors import cross_origin
from SendEmail.sendEmail import EmailSender
from logger import logger
from email_templates import email_content
from covid_api import CovidCases

app = Flask(__name__)



# geting and sending response to dialogflow
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():

    req = request.get_json(silent=True, force=True)

    print(req)
    #print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


# processing the request from dialogflow
def processRequest(req):
    log = logger.Log()

    sessionID=req.get('responseId')


    result = req.get("queryResult")
    user_says=result.get("queryText")
    log.write_log(sessionID, "User Says: "+user_says)
    parameters = result.get("parameters")
    user_name = parameters.get("user_name")
    option_name = parameters.get("option_name")
    option_name_2 = parameters.get("option_name_2")
    user_location = parameters.get("user_location")
    user_location = user_location.upper()
    user_mobile=parameters.get("user_mobile")
    user_email= parameters.get("user_email")
    #intent = result.get("intent").get('displayName')
    cases = CovidCases()
    email_sender = EmailSender()
    content_email = email_content.EmailContent()
    if (option_name=='Covid-19 in India'):

        cases_india = cases.covid_india(user_location)
        content_india = content_email.email_india(cases_india)
        email_sender.send_email_to_user(user_email,content_india)
        fulfillmentText="The total confirmed cases in {} state is {}.For more details please check your Email and for visualization please check below link. https://www.covid19india.org/".format(cases_india.get("response").get('name'), cases_india.get("response").get('confirmed'))
        log.write_log(sessionID, "Bot Says: "+fulfillmentText)
        return {
            "fulfillmentText": fulfillmentText
        }
    elif (option_name_2=='Covid-19 in World'):

        cases_world = cases.covid_world(user_location)
        content_world = content_email.email_world(cases_world)
        email_sender.send_email_to_user(user_email, content_world)
        fulfillmentText="The total confirmed cases in {} is {}.For more details please check your Email and for visualization please check below link. https://www.covidvisualizer.com/".format(cases_world.get('country'), cases_world.get('confirmed'))
        log.write_log(sessionID, "Bot Says: "+fulfillmentText)
        return {
            "fulfillmentText": fulfillmentText
        }
    else:
        log.write_log(sessionID, "Bot Says: " + result.fulfillmentText)


if __name__ == '__main__':
    #port = int(os.getenv('PORT', 5000))
    #print("Starting app on port %d" % port)
    #app.run(debug=False, port=port, host='0.0.0.0')
    #app.run(port=8000, debug=True)
    app.run(debug=True)