import requests
from endpoints.base_endpoint import Endpoint

class DeleteObject(Endpoint):

    def delete_by_id(self, obj_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')