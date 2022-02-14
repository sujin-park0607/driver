from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):

    #사용자와 websocket연결이 맺어졌을때 호출
    def connect(self):
        self.accept()

    #사용자와 websocket 연결이 끊겼을때 호출
    def disconnect(self, close_code):
        pass

    #사용자가 메시지를 보내면 호출
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message':message
        }))