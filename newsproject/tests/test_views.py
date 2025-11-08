from django.urls import reverse
from user.models import CustomUser
from django.test import TestCase
from articles.models import Articles, Categories, SubCategories
from django.core.files.uploadedfile import SimpleUploadedFile


class ArticleViewTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')

    def test_article_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/main.html')

    def test_article_detail_view(self):
        image = SimpleUploadedFile(
            "test.jpg",
            b"file_content",
            content_type="image/jpeg"
        )

        category = Categories.objects.create(name='Tech', slug='tech')
        subcategory = SubCategories.objects.create(name='AI', category=category, slug='ai')
        article = Articles.objects.create(
            title='Test Article',
            category=category,
            subcategory=subcategory,
            slug='test-article',
            content='This is a test article.',
            user=self.user,
            status='published',
            image=image
        )
        response = self.client.get(reverse('article_detail', args=[article.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article.html')
        self.assertContains(response, 'Test Article')

    def test_category_view(self):
        category = Categories.objects.create(name='Tech', slug='tech')
        response = self.client.get(reverse('category', args=[category.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/category.html')

    def test_create_article_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('create_article'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/create.html')

    def test_edit_article_view(self):
        self.client.login(username='testuser', password='12345')
        category = Categories.objects.create(name='Tech', slug='tech')
        subcategory = SubCategories.objects.create(name='AI', category=category, slug='ai')
        article = Articles.objects.create(
            title='Test Article',
            category=category,
            subcategory=subcategory,
            slug='test-article',
            content='This is a test article.',
            user=self.user,
            status='published'
        )
        response = self.client.get(reverse('update_article', args=[article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/update.html')

    def test_delete_article_view(self):
        self.client.login(username='testuser', password='12345')
        category = Categories.objects.create(name='Tech', slug='tech')
        subcategory = SubCategories.objects.create(name='AI', category=category, slug='ai')
        article = Articles.objects.create(
            title='Test Article',
            category=category,
            subcategory=subcategory,
            slug='test-article',
            content='This is a test article.',
            user=self.user,
            status='published'
        )
        response = self.client.post(reverse('delete_article', args=[article.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        



class UserViewTestCase(TestCase):
    def test_registration_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
            'email': 'ggg@gmail.com'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        user = CustomUser.objects.get(email='ggg@gmail.com')
        self.assertEqual(user.username, 'newuser')

    def test_login_view(self):
        user = CustomUser.objects.create_user(username='testuser', password='12345', email='ggg@gmail.com')
        response = self.client.post(reverse('login'), {
            'password': '12345',
            'username': 'ggg@gmail.com'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    

