import requests
import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject


def test_create_object(all_tests):
    new_object_endpoint = CreateObject()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_name(name=payload['name'])
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_data(data=payload['data'])


def test_get_object(obj_id):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_object(obj_id)
    get_object_endpoint.check_id(obj_id)
    get_object_endpoint.check_response_is_200()


def test_put_object(obj_id):
    update_object_endpoint = UpdateObject()
    payload = {
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2020,
            "price": 1849.99,
            "CPU model": "M10",
            "Hard disk size": "1 TB"
        }
    }
    update_object_endpoint.update_object(payload=payload, obj_id=obj_id)
    update_object_endpoint.check_name_update(name=payload['name'])
    update_object_endpoint.check_response_is_200()


def test_delete_object(obj_id):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_by_id(obj_id)
    delete_object_endpoint.check_response_is_200()
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_is_404()

