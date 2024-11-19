import requests
from endpoints.base_endpoint import Endpoint


class UpdateObject(Endpoint):

    def update_object(self, payload, obj_id):
        self.response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
        self.response_json = self.response.json()


    def check_name_update(self, name):
        assert self.response_json['name'] == name