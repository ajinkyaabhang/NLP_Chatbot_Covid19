import requests

class CovidCases:
    def __init__(self):
        pass

    def covid_india(self, state_name):
        try:
            url = "https://covid19india.p.rapidapi.com/getStateData/{}".format(state_name)
            headers = {
                'x-rapidapi-host': "covid19india.p.rapidapi.com",
                'x-rapidapi-key': "3ea549fbfamsh2b39f3e0bee8632p1fd465jsn79c403858623"
            }
            response = requests.request("GET", url, headers=headers)

            return response.json()

        except Exception as e:
            print('the exception is ' + str(e))

    def covid_world(self, country_name):
        try:
            url = "https://covid19-data.p.rapidapi.com/"
            querystring = {"iso3": '{}'.format(country_name)}
            headers = {
                'x-rapidapi-host': "covid19-data.p.rapidapi.com",
                'x-rapidapi-key': "3ea549fbfamsh2b39f3e0bee8632p1fd465jsn79c403858623"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)

            return response.json()

        except Exception as e:
            print('the exception is ' + str(e))