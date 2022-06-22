import requests

def send(msg, wb):
    r = requests.post(wb, data={'content': msg})
    return r.status_code, r.text

print(send("@everyone Убили негра убили негра жаль", 'https://discord.com/api/webhooks/988992230532472832/TpeDCMH2JCh3OkteBHFBwUU3MtC7Kk0yNAh8UrHHz1TH-K9cOCq8ETe9_DXTVUNRPGWB'))