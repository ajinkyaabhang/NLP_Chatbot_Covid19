from covid_api import CovidCases

class EmailContent:
    def __init__(self):
        pass

    def email_india(self, india_data):
        self.india_data = india_data.get("response")
        text_india = """\
        Hello,

        Please find below details about {} state.

        Confirmed Cases : {}
        Active Cases : {}
        Recovered Cases : {}
        Deaths Cases : {}

        Please find attached document which states preventive measures for Covid-19.

        Thanks & Regards,
        Covid19_chatbot""".format(self.india_data.get('name'), self.india_data.get('confirmed'), self.india_data.get('active'),
                                  self.india_data.get('recovered'), self.india_data.get('deaths'))
        return text_india

    def email_world(self, world):
        text_world = """\
        Hello,

        Please find below details about {}.

        Confirmed Cases : {}
        Recovered Cases : {}
        Deaths Cases : {}

        Please find attached document which states preventive measures for Covid-19.

        Thanks & Regards,
        Covid19_chatbot""".format(world.get('country'), world.get('confirmed'), world.get('recovered'), world.get('deaths'))

        return text_world