from django.test import TestCase

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

#Models
from Pedido.models import Pedido

class UserTestCase(TestCase):
    """
    def setUp(self):
        pedido = Pedido(
            cui='2994932450101'
        )        
        pedido.save()
    """

    def test_signup_user(self):
        """Check if we can create an user"""        
        client = APIClient()
        response = client.post(
                '/api/v1/pedido', {
                'cui': '2994932450101'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
