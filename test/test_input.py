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


#rate a movie
def test_rate_new_movie():
    rate_new_movie=requests.post(getvalue("url")+"/"+getvalue("movieid")+"/rating",
                                     params={"api_key": getvalue("api_key"),
                                             "guest_session_id": getvalue("guest_session_id")},
                                        data={
                                            "value": getvalue("rate_value")
                                        }
                                     )

    assert rate_new_movie.status_code,201
    assert rate_new_movie.json()["status_message"],"success"


#rate an already rated movie
def test_rate_already_rated_movie():
    rate_already_rated_movie=requests.post(getvalue("url")+"/"+getvalue("already_rate_movie")+"/rating",
                                     params={"api_key": getvalue("api_key"),
                                             "guest_session_id": getvalue("guest_session_id")},
                                        data={
                                            "value": getvalue("rate_value")
                                        }
                                     )
    # print(rate_already_rated_movie.json())
    assert rate_already_rated_movie.status_code,201
    assert rate_already_rated_movie.json()["status_message"],getvalue("status_already_rated_movie")


#rate a movie with higher value
def test_rate_movie_higher_value():
    rate_movie_higher_value=requests.post(getvalue("url")+"/"+getvalue("already_rate_movie")+"/rating",
                                     params={"api_key": getvalue("api_key"),
                                             "guest_session_id": getvalue("guest_session_id")},
                                        data={
                                            "value": getvalue("rate_value_higher")
                                        }
                                     )
    print(rate_movie_higher_value.json())
    assert rate_movie_higher_value.json()["status_message"], getvalue("status_high_rated_movie")


def test_rate_movie_lower_value():
    rate_movie_lower_value=requests.post(getvalue("url")+"/"+getvalue("already_rate_movie")+"/rating",
                                     params={"api_key": getvalue("api_key"),
                                             "guest_session_id": getvalue("guest_session_id")},
                                        data={
                                            "value": getvalue("negative_rate_value")
                                        }
                                     )
    # print(rate_movie_lower_value.json())
    assert rate_movie_lower_value.json()["status_message"], getvalue("status_low_raed_movie")

def test_rate_movie_invalid_api():
    rate_movie_invalid_api=requests.post(getvalue("url")+"/"+getvalue("already_rate_movie")+"/rating",
                                     params={"api_key": getvalue("invalid_api"),
                                             "guest_session_id": getvalue("guest_session_id")},
                                        data={
                                            "value": getvalue("rate_value")
                                        }
                                     )
    # print(rate_movie_invalid_api.json())
    assert rate_movie_invalid_api.json()["status_message"], getvalue("invalid_key_status_message")
    assert  rate_movie_invalid_api.status_code,401


def test_rate_invalid_movie():
    rate_invalid_movie = requests.post(getvalue("url") + "/" + getvalue("invalid_movie_id") + "/rating",
                                   params={"api_key": getvalue("api_key"),
                                           "guest_session_id": getvalue("guest_session_id")},
                                   data={
                                       "value": getvalue("rate_value")
                                   }
                                   )

    # print(rate_invalid_movie.status_code)
    # print(rate_invalid_movie.json())
    assert rate_invalid_movie.status_code, 404
    assert rate_invalid_movie.json()["status_message"], "The resource you requested could not be found."