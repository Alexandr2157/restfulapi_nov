import requests
from endpoints.base_endpoint import Endpoint


class GetObject(Endpoint):

    def get_object(self, obj_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
        self.response_json = self.response.json()

    def check_id(self, obj_id):
        assert self.response_json['id'] == obj_id

    def get_by_id(self, obj_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')

    def check_response_is_404(self):
        assert self.response.status_code == 404
        print('Объект удален')

