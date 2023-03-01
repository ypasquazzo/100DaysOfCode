import requests

NB_QUESTIONS = 50
parameters = {
    "amount": NB_QUESTIONS,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()
