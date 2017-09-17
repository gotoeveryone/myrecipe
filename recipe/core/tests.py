""" コアライブラリのテストケース """
import random
from django.test import TestCase
from recipe.core.models import Cuisine

# Create your tests here.

class CuisineModelTests(TestCase):
    """ レシピモデルのテスト """
    cuisines = []
    classifications = ['主食', '主菜', '副菜', 'デザート']

    @classmethod
    def setUpTestData(cls):
        # テストデータを10件登録しておく
        for x in range(1,10):
            cuisine = Cuisine()
            cuisine.name = 'テスト%d' % x
            cuisine.classification = random.choice(cls.classifications)
            cuisine.ingestion_kcal = x * 100
            cuisine.save()
            cls.cuisines.append(cuisine)

    def test_is_search_cuisine(self):
        """ レシピの検索 """

        # DBから取得して比較
        exists = Cuisine.objects.filter(name__contains='テスト').all()
        for e in exists:
            self.assertIsNotNone(e.id)
            self.assertIn('テスト', e.name)

    def test_is_search_cuisine_by_name(self):
        """ レシピの検索 """

        # DBから取得して比較
        exists = Cuisine.objects.filter(name='テスト1').first()
        self.assertIsNotNone(exists.id)
        self.assertEqual(exists.name, 'テスト1')
