from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
 
from .models import *
 
 
class BlogTests(TestCase):
 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
 
        self.aboutme = AboutMe.objects.create(
            user='A good title',
            first_name='Nice body content',
            last_name=self.user,
        )
        
    def test_string_representation(self):
        aboutme = AboutMe(user='A sample title')
        self.assertEqual(str(AboutMe), aboutme.user)
 
    def test_post_content(self):
        self.assertEqual(f'{self.abotme.user}', 'A good user')
        self.assertEqual(f'{self.aboutme.first_name}', 'testuser')
        self.assertEqual(f'{self.aboutme.last_name}', 'Nice body content')
 
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')
 
    def test_post_detail_view(self):
        response = self.client.get('/aboutme/1/')
        no_response = self.client.get('/aboutme/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'about_detail.html')
