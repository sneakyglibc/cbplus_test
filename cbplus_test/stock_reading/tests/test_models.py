import datetime

from django.core.exceptions import ValidationError
from django.db.utils import DataError, IntegrityError
from django.test import TestCase

from ..models import StockReading


class TestStockReading(TestCase):

    def setUp(self):
        super().setUp()
        self.date = datetime.date.today()
        self.reference_id = '1234567890123'
        self.stock_reading = StockReading.objects.create(
            reference_id=self.reference_id,
            expiry_date=self.date
        )

    def test_create_stock_reading_with_existing_last(self):
        stock_reading = StockReading.objects.create(
            reference_id=self.reference_id,
            expiry_date=self.date
        )
        stock_reading.refresh_from_db()

        self.assertEqual(stock_reading.reference_id, self.reference_id)
        self.assertEqual(stock_reading.expiry_date, self.date)
        self.assertTrue(stock_reading.creation_date)
        self.assertTrue(stock_reading.uuid)

    def test_create_stock_reading_with_not_enough_charac_for_reference_id(self):
        with self.assertRaises(DataError) as e:
            StockReading.objects.create(
                reference_id='12345678901234',
                expiry_date=self.date,
            )
        self.assertEqual(
            str(e.exception),
            "value too long for type character varying(13)\n"
        )

    def test_create_stock_reading_with_too_many_charac_for_reference_id(self):
        with self.assertRaises(ValidationError) as e:
            self.stock_reading.reference_id = '123456789012'
            self.stock_reading.full_clean()
        self.assertEqual(
            str(e.exception),
            "{'reference_id': ['The reference_id field has to be 13 digits.']}"
        )

    def test_create_stock_reading_with_no_digits_for_reference_id(self):
        with self.assertRaises(ValidationError) as e:
            self.stock_reading.reference_id = '123456789abc'
            self.stock_reading.full_clean()
        self.assertEqual(
            str(e.exception),
            "{'reference_id': ['The reference_id field has to be 13 digits.']}"
        )