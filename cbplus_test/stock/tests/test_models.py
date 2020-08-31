import datetime

from django.core.exceptions import ValidationError
from django.db.utils import DataError, IntegrityError
from django.test import TestCase

from ..models import StockReading


class TestStockReading(TestCase):

    def setUp(self):
        super().setUp()
        self.date = datetime.date.today()
        self.stock_reading = StockReading.objects.create(
            reference_id='9999999999998',
            expiry_date=self.date
        )

    def test_create_stock_reading_with_existing_last(self):
        stock_reading = StockReading.objects.create(
            reference_id='9999999999998',
            expiry_date=self.date
        )
        stock_reading.refresh_from_db()

        self.assertEqual(stock_reading.reference_id, '9999999999998')
        self.assertEqual(stock_reading.expiry_date, self.date)
        self.assertEqual(stock_reading.last, True)
        self.assertTrue(stock_reading.creation_date)
        self.assertTrue(stock_reading.last_update)

        self.stock_reading.refresh_from_db()
        self.assertEqual(self.stock_reading.last, False)

    def test_create_stock_reading_unique_together(self):
        with self.assertRaises(IntegrityError) as e:
            StockReading.objects.create(
                reference_id='9999999999998',
                expiry_date=self.date,
            )
            self.stock_reading.last = True
            self.stock_reading.save()
        self.assertEqual(
            str(e.exception),
            "duplicate key value violates unique constraint \"unique_reference_id_last\"\nDETAIL:  Key "
            "(reference_id, last)=(9999999999998, t) already exists.\n"
        )

    def test_create_stock_reading_with_wrong_reference_id(self):
        with self.assertRaises(DataError) as e:
            StockReading.objects.create(
                reference_id='99999999999999',
                expiry_date=self.date,
            )
        self.assertEqual(
            str(e.exception),
            "value too long for type character varying(13)\n"
        )

        with self.assertRaises(ValidationError) as e:
            self.stock_reading.reference_id = '999999999999'
            self.stock_reading.full_clean()
        self.assertEqual(
            str(e.exception),
            "{'reference_id': ['The reference_id field has to be 13 digits.']}"
        )

