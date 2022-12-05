# import pytest
# import factory
# from pytest_factoryboy import register
# from rest_framework.test import APIClient, APIRequestFactory
# from django.contrib.auth import get_user_model
# from django.contrib.auth.hashers import make_password
# from django import VERSION as DJANGO_VERSION
# from django.test import TestCase
# from django.urls import reverse
#
# from account.models import Account
#
#
# class ConfTest(TestCase):
#
#     @pytest.mark.django_db
#     def test_register_success(self):
#         superuser = Account.objects.create_superuser(
#             username="admin",
#             email="admin@admin.com",
#             password="admin"
#         )
#         superuser.save()
#         assert Account.objects.count() > 0
#
#     @pytest.mark.django_db
#     def create_test_user(self):
#         test_user = Account.objects.create(
#             username="test_user",
#             email="test_user@test_user.com",
#             password="test_user"
#         )
#         test_user.save()
#         return test_user
