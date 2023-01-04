import requests

ACCESS_TOKEN = "API KEY"
PHONE_NUMBER = "CODIGO DE PAIS + NUMERO"
MESSAGE = "MENSAJE"
url = f"https://graph.facebook.com/v15.0/ID_URL/messages?access_token={ACCESS_TOKEN}"

# JSON API WHATSAPP
payload = { "messaging_product": "whatsapp",
                "to": PHONE_NUMBER,
                "type": "template",
                "template": {
                    "name": "NOMBRE DE PLANTILLA DE MENSAJE",
                    "language": {
                        "code": "IDIOMA"
                    },
                    "components": [{
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": "INGRESA TEXTO"
                            },
                            {
                              "type":"text",
                              "text": "INGRESA TEXTO"
                            }
                        ]
                }]
            }
        }

response = requests.post(url, json=payload)

print(response.text)
