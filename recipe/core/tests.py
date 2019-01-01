""" コアライブラリのテストケース """
import random
from django.test import TestCase
from recipe.core.models import Cuisine, Classification


class CuisineModelTests(TestCase):
    """ レシピモデルのテスト """
    cuisines = []
    classifications = ['Staple foot', 'Main dish', 'Side dish', 'Dessert']

    @classmethod
    def setUpTestData(cls):
        for i, c in enumerate(cls.classifications):
            Classification.objects.create(name=c, sort_order=i)

        # テストデータを10件登録しておく
        for count in range(1, 10):
            cuisine = Cuisine()
            if count % 2 == 0:
                cuisine.name = 'Test Name%d' % count
            else:
                cuisine.name = 'Test Name'
            classification = Classification.objects.filter(
                name=random.choice(cls.classifications)).first()
            cuisine.classification = classification
            cuisine.ingestion_kcal = count * 100
            cuisine.save()
            cls.cuisines.append(cuisine)

    def test_is_search_cuisine(self):
        """ レシピの検索 """

        # DBから取得して比較
        exists = Cuisine.objects.filter(name__contains='Test').all()
        for row in exists:
            self.assertIsNotNone(row.id)
            self.assertIn('Test', row.name)

    def test_is_search_cuisine_by_name(self):
        """ レシピの検索（名前一致） """

        # DBから取得して比較
        exists = Cuisine.objects.filter(name='Test Name').first()
        self.assertIsNotNone(exists.id)
        self.assertEqual(exists.name, 'Test Name')

    def test_is_search_cuisine_by_ingestion_kcal(self):
        """ レシピの検索（Kcal一致） """

        # DBから取得して比較
        exists = Cuisine.objects.filter(ingestion_kcal=200).first()
        self.assertIsNotNone(exists.id)
        self.assertEqual(exists.ingestion_kcal, 200)
