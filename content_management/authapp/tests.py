from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

#just to check setup
class FirstTestCase(TestCase):
    def setUp(self):
        print('setup called')

    def tests_equal(self):
        self.assertEqual(1,1)


#test cases for httpresponse 
class ContentTest(APITestCase):
    def test_register(self):
        _data={
            "username":"shubh",
            "password":"shubh",
            "first_name":"shubh",
            "last_name":"solanke",
            "email": "shubh@gmail.com"

        }  

        _response=self.client.post('/v1/register/',data=_data, format="json") 

        _data=_response.json()
        self.assertEqual(_response.status_code,status.HTTP_201_CREATED)

    def test_get_content(self):
        _response=self.client.get('/v1/content/')  
        _data=_response.json()
        self.assertEqual(_response.status_code,status.HTTP_200_OK)      