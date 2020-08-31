import datetime

from django.urls import reverse_lazy

from rest_framework import status
from rest_framework.test import APITestCase

from ..models import StockReading


class TestStockReadingAPI(APITestCase):
    def setUp(self):
        super().setUp()
        self.expiry_date = datetime.date.today()
        self.reference_id = '1234567890123'
        self.stock_reading = StockReading.objects.create(
            reference_id=self.reference_id,
            expiry_date=self.expiry_date
        )
        self.stock_reading.refresh_from_db()

    def test_list_stock_readings(self):
        url = reverse_lazy('stock_readings-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.json(), list))
        self.assertEqual(len(response.json()), 1)
        self.assertDictEqual(
            response.json()[0],
            {
                'id': self.stock_reading.id,
                'reference_id': self.stock_reading.reference_id,
                'expiry_date': str(self.stock_reading.expiry_date),
                'creation_date': str(self.stock_reading.creation_date),
                'last_update_date': str(self.stock_reading.last_update_date)
            }
        )

    def test_list_stock_readings_with_last_filter_at_true(self):
        StockReading.objects.create(
            reference_id='1234567890123',
            expiry_date=self.expiry_date
        )
        stock_reading = StockReading.objects.create(
            reference_id='1234567890123',
            expiry_date=self.expiry_date
        )
        url = reverse_lazy('stock_readings-list')
        response = self.client.get(url, data={'last': True}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.json(), list))
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], stock_reading.id)

    def test_list_stock_readings_with_last_filter_at_false(self):
        stock_reading_1 = StockReading.objects.create(
            reference_id='1234567890123',
            expiry_date=self.expiry_date
        )
        StockReading.objects.create(
            reference_id='1234567890123',
            expiry_date=self.expiry_date
        )
        url = reverse_lazy('stock_readings-list')
        response = self.client.get(url, data={'last': False}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.json(), list))
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(
            [response.json()[0]['id'], response.json()[1]['id']],
            [stock_reading_1.id, self.stock_reading.id]
        )

    def test_list_stock_readings_with_reference_id_filter(self):
        stock_reading = StockReading.objects.create(
            reference_id='1112223334445',
            expiry_date=self.expiry_date
        )
        url = reverse_lazy('stock_readings-list')
        response = self.client.get(url, data={'reference_id': '1112223334445'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.json(), list))
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['reference_id'], stock_reading.reference_id)

    def test_post_stock_readings(self):
        url = reverse_lazy('stock_readings-list')
        response = self.client.post(
            url,
            data={
                'reference_id': self.reference_id,
                'expiry_date': self.expiry_date,
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_stock_readings_with_wrong_reference_id(self):
        url = reverse_lazy('stock_readings-list')
        response = self.client.post(
            url,
            data={
                'reference_id': '123456789012a',
                'expiry_date': self.expiry_date,
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {'reference_id': ['The reference_id field has to be 13 digits.']}
        )
