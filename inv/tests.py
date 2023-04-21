from django.test import TestCase, Client

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy, reverse

from .models import Producto, Categoria, User
import json

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        User.obj.create('john', 'lennon@thebeatles.com', 'johnpassword')
        self.list_url = reverse('categoria_list')
        self.list_new = reverse('categoria_new', args=['categoria1'])
        self.categoria1 = Categoria.obj.create(
            name='categoria1',
            estado=True
        )

    def testLogin(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200) 

    def test_project_list_GET(self):

        response = self.client.get(self.list_url)

        assertEqual(response.status_code, 200)
        assertTemplateUsed(response, 'app/inv/categoria_list.html')

    def test_project_new_GET(self):

        response = self.client.get(self.list_new)

        assertEqual(response.status_code, 200)
        assertTemplateUsed(response, 'app/inv/categoria_list.html')
        

