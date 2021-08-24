import json
from channels.generic.websocket import WebsocketConsumer
from . import models


class JobConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        job = text_data_json['job']

        if job.get('courier_lat') and job.get('courier_lng'):
            self.scope['user'].courier.lat = job['courier_lat']
            self.scope['user'].courier.lng = job['courier_lng']
            self.scope['user'].courier.save()
        # print("Job", job)
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))
