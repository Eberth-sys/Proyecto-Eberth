print("Proyecto de Eberth Alarcòn")

import requests
import json

url_login = "https://10.10.20.14/api/aaaLogin.json"

data = {
    "aaaUser" : {
        "attributes" : {
            "name" : "admin",
            "pwd" : "C1sco12345"
        }
    }
}
cabecera = {"content-type":"application/json"}

requests.packages.urllib3.disable_warnings() # Eliminar el warning

Respuesta= requests.post(url_login, json.dumps(data), headers=cabecera, verify=False)
Respuesta_json= Respuesta.json()
API_TOKEN = Respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
print("")
print("***" *200)
print("EL TOKEN ES:", API_TOKEN)
print("***" *200)

#Obtner el firmware en ejecuciòn.

url_firmware = "https://10.10.20.14/api/class/firmwareCtrlrRunning.json"
cabecera_firmware = {"content-type":"application/json"}
webtoken = { "APIC-Cookie": API_TOKEN}
respuesta_firmware = requests.get(url_firmware, headers=cabecera_firmware, cookies=webtoken, verify=False)
respuesta_firmware_json=  respuesta_firmware.json()
firmwarelebel = respuesta_firmware_json["imdata"][0]["firmwareCtrlrRunning"]["attributes"]["internalLabel"]
firmwaremode = respuesta_firmware_json["imdata"][0]["firmwareCtrlrRunning"]["attributes"]["mode"]
firmwaretype = respuesta_firmware_json["imdata"][0]["firmwareCtrlrRunning"]["attributes"]["type"]
firmwaremgm = respuesta_firmware_json["imdata"][0]["firmwareCtrlrRunning"]["attributes"]["lcOwn"]
firmwareversion = respuesta_firmware_json["imdata"][0]["firmwareCtrlrRunning"]["attributes"]["version"]
firmwaretime = respuesta_firmware_json["imdata"][0]["firmwareCtrlrRunning"]["attributes"]["modTs"]
print("")
print("**"*20)
print(" * Informacion del Firmware * ")
print("**"*20)
print("- Etiqueta del Firmware:", firmwarelebel)
print("- Modo actual del Firmware:", firmwaremode)
print("- Tipo actual del Firmware:", firmwaretype)
print("- Gestiòn actual del Firmware:", firmwaremgm)
print("- Versiòn actual del Firmware:", firmwareversion)
print("- Ultima modificacion del Firmware:", firmwaretime)

#GET http://apic-ip-address/api/class/topSystem.json

url_top = "https://10.10.20.14/api/class/topSystem.json"
cabecera_top= {"content-type":"application/json"}
webtoken_top= { "APIC-Cookie": API_TOKEN}
respuesta_top= requests.get(url_top, headers=cabecera_top, cookies=webtoken_top, verify=False)
respuesta_top_json=  respuesta_top.json()
total_equipos_json= respuesta_top_json["totalCount"]
print("")
print("*-*-"*20)
print("Identificacion IP por cada Servidor Disponible")
print("//" *100)
for i in range(0, int(total_equipos_json)):
    ip01 = respuesta_top_json["imdata"][i]["topSystem"]["attributes"]["address"]
    print("Server [", i ,"]  --> Direcciòn IP:" + ip01)
print("//" *100)