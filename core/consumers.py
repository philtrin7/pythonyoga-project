import json
from channels.generic.websocket import WebsocketConsumer
from . import models

class JobConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads()
        job = text_data_json['job']
        
        print("Job", job)
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))


