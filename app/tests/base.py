from django import setup
from dotenv import load_dotenv
import os


os.environ["DJANGO_SETTINGS_MODULE"] = "app.settings.ci"
setup()

load_dotenv()

from django.test import TestCase
from django.test.utils import setup_test_environment
from django.contrib.auth.models import User

# Local imports
from blog.models import Post, Category
from .utils import create_unique_post, create_comment


class SetUp(TestCase):
    setup_test_environment()

    @classmethod
    def setUpTestData(cls):
        cls.admin_user_password = "admin"
        cls.comment_only_user_password = "comment_only"
        cls.default_category = Category.objects.get(slug="uncategorized")
        cls.admin_user = User.objects.get(username="admin")
        cls.comment_only_user = User.objects.get(username="comment_only")
        cls.first_post = create_unique_post()
        cls.first_comment = create_comment(cls.first_post)
        cls.draft_post = create_unique_post(draft=True)

    def tearDown(self):
        Post.objects.all().delete()
