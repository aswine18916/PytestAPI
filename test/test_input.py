import json
import requests
from utilities import getvalue


#Get top rate movie in the page 5
def test_get_resp():
    resp = requests.get(getvalue("url")+"/"+getvalue("topratedmovie"),
                        params={"api_key": getvalue("api_key"),
                                 "language":getvalue("language"),
                                 "page": 5})
    # print(json.dumps(resp.json(),indent=3))
    assert resp.status_code,200
    assert (resp.json()["page"]),5
    assert isinstance(resp.json()["results"],list)
    # print(json.dumps(resp.json()["results"][0],indent=3))

#pass invalid auth key and assert the response code
def test_invalid_auth_code():
    invalid_resp = requests.get(getvalue("url") + "/" + getvalue("topratedmovie"),
                        params={"api_key": getvalue("invalid_api"),
                                "language": getvalue("language"),
                                "page": 5})

    #print(invalid_resp.json())
    assert invalid_resp.status_code,401

#pass invalid language and page value
def test_invalid_language_page():
    invalid_language_page = requests.get(getvalue("url") + "/" + getvalue("topratedmovie"),
                        params={"api_key": getvalue("api_key"),
                                "language": getvalue("invalidlanguage"),
                                "page": getvalue("invalidpage")})

    assert invalid_language_page.status_code, 200


# rate a movie
# def test_rate_movie():
#     generate_auth_token=requests.get(getvalue("generate_auth_token"),
#                                      params={"api_key": getvalue("api_key")}
#                                      )
#     # rate_a_movie=requests.post(getvalue("url")+"/977/",
#     #                            data={
#     #                                 "value": getvalue("movieratevalue")},
#     #                            params={"api_key": getvalue("api_key")}
#     #                            )
#
#     auth_token=generate_auth_token.json()["request_token"]
#     print(auth_token)
#     new_session=requests.post(getvalue("generate_new_session"),
#                               params={"api_key": getvalue("api_key")},
#                               data={"request_token": auth_token}
#                               )
#     print(new_session.json())