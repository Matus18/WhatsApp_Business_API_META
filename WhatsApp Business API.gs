function envio_whatsapp{
  var sheet_configuracion = libro.getSheetByName("HOJA_EXCEL");
  var plantilla = sheet_configuracion.getRange(1, 2).getValue();
  var token = sheet_configuracion.getRange(2, 2).getValue();
  var api = sheet_configuracion.getRange(3, 2).getValue();
  var payload = {
                "messaging_product": "whatsapp",
                "to": numero_telefono,
                "type": "template",
                "template": {
                    "name": plantilla,
                    "language": {
                        "code": "es"
                    },
                    "components": [{
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": nombre
                            },
                            {
                              "type":"text",
                              "text": monto_total
                            }
                        ]
                    }]
                }
            }
            var options =
            {
              'headers': { "Content-Type": "application/json","Authorization": token},
                'method': "POST",
                'payload': JSON.stringify(payload)
            };
            try {
                var response = UrlFetchApp.fetch(api, options);
                var json = JSON.parse(response.getContentText());
            } catch (e) {
            }
}
