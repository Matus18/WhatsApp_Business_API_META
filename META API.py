import requests

ACCESS_TOKEN = "EAAL028cN0asBAIVwc744AODZBOD8CmaoAeklEk71ZC17qyy7vG2mM93tpZC3KNXhaEwldkof85CYpowbrMn6Scpmnhl1cs71l6QTbAJf7FqaXI4ZBR8T84qB18pU1WzOF5KIwOJ8VxEEWrcHKGyDBr00KQqNZBARbL8UJZAf5giZCIDyzh30JUKYcfNGpZBNg3HKAjxL3cStFgZDZD"
PHONE_NUMBER = "569"
MESSAGE = "Hola, ¿cómo estás?"
url = f"https://graph.facebook.com/v15.0/110002441945576/messages?access_token={ACCESS_TOKEN}"

# JSON API WHATSAPP
payload = { "messaging_product": "whatsapp",
                "to": PHONE_NUMBER,
                "type": "template",
                "template": {
                    "name": "pedido_enviado_sinpago",
                    "language": {
                        "code": "es"
                    },
                    "components": [{
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": "Benjamin"
                            },
                            {
                              "type":"text",
                              "text": "$23.990"
                            }
                        ]
                }]
            }
        }

response = requests.post(url, json=payload)

print(response.text)