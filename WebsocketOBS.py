import websocket
import json
import hashlib
import base64


ws = websocket.WebSocket()

def sceneinit():
    print("Szenen werden geladen...")
    talk = json.dumps({'request-type': "GetSceneList"})
    ws.connect("ws://localhost:4444")
    passwort()
    ws.send(talk)
    re = ws.recv()
    j = json.loads(re)
    print("Szenen wurden geladen!")
    return j

def passwort():
    data = json.dumps({'request-type': 'GetAuthRequired', 'message-id':''})
    ws.connect("ws://localhost:4444")
    ws.send(data)
    empf = ws.recv()
    j = json.loads(empf)
    pw = "[Your Password]"
    salt = j['salt']
    challenge = j['challenge']
    secstr1 = pw + salt
    hashingsha1 = hashlib.sha256(secstr1.encode('utf8'))
    stage1 = hashingsha1.digest()
    stage2 = base64.b64encode(stage1)
    secstr2 = stage2 + challenge.encode('utf-8')
    hashingsha2 = hashlib.sha256(secstr2)
    stage3 = hashingsha2.digest()
    stage4 = base64.b64encode(stage3)
    final = stage4.decode('utf-8')
    authing = json.dumps({'request-type': 'Authenticate' , 'auth': final, 'message-id':''})
    ws.send(authing)
    empf2= ws.recv()
    print(empf2)
    return authing

def szene1():
    data = json.dumps({'request-type': 'SetCurrentScene' , 'scene-name':"Szene", 'message-id':''})
    ws.connect("ws://localhost:4444")
    passwort()
    ws.send(data)
    empf = ws.recv()
    print(empf)

def szene2():
    data = json.dumps({'request-type': 'SetCurrentScene' , 'scene-name':"Szene 2", 'message-id':''})
    ws.connect("ws://localhost:4444")
    passwort()
    ws.send(data)
    empf = ws.recv()
    print(empf)