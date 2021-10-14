from flask import Flask , request
import os
import json
import requests
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
load_dotenv()
app = Flask(__name__)

def get_dictionary_response(word):
    word_metadata = {}
    definition = "sorry, no definition is available."
    example = "sorry, no examples are available."
    synonyms = ["sorry, no synonyms are available."]
    antonyms = ["sorry, no antonyms are available."]
    status = 1
    api_key = os.getenv("KEY_THESAURUS")
    url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={api_key}"
    response = requests.get(url)
    api_response = json.loads(response.text)
    if response.status_code == 200:
        for data in api_response:
            try:
                if data["meta"]["id"] == word:
                    try:
                        if len(data["meta"]["syns"]) != 0:
                            synonyms = data["meta"]["syns"][0]
                            status = 0
                        if len(data["meta"]["ants"]) != 0:
                            antonyms = data["meta"]["ants"][0]
                            status = 0
                        for results in data["def"][0]["sseq"][0][0][1]["dt"]:
                            if results[0] == "text":
                                status = 0
                                definition = results[1]
                            if results[0] == "vis":
                                example = results[1][0]["t"].replace("{it}", "*").\
                                    replace("{/it}", "*")
                                status = 0
                    except KeyError as e:
                        print(e)
            except TypeError as e:
                print(e)
            break
    word_metadata["meaning"] = definition
    word_metadata["examples"] = example
    word_metadata["antonyms"] = antonyms
    word_metadata["synonyms"] = synonyms
    word_metadata["status"] = status
    return word_metadata




@app.route('/vocabulary', methods=['POST'])
def vocabulary():
    word_synonym = ""
    word_antonym = ""
    incoming_msg = request.get_json()
    print(incoming_msg['word'])
    response = get_dictionary_response(incoming_msg['word'])
    return response


if __name__ == "__main__":
    app.run(port=8081,debug=True)