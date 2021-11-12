import unittest
from dataclasses import dataclass
from datetime import date
from typing import Optional


def test_make_batch_and_line(ref: str, order_id: str, sku: str, batch_qty: int, line_qty: int, eta: date):
    return (
        Batch(ref=ref, sku=sku, qty=batch_qty, eta=eta),
        OrderLine(order_id=order_id, sku=sku, qty=line_qty)
    )


class DomainModel(unittest.TestCase):

    def test_allocating_to_a_batch_reduces_the_available_quantity(self) -> None:
        batch: Batch = Batch(ref='batch-001', sku='SMALL_TABLE', qty=20, eta=date.today())
        line: OrderLine = OrderLine(order_id='order-ref', sku='SMALL_TABLE', qty=2)

        batch.allocate(line)

        assert batch.available_quantity == 18

    def test_make(self) -> None:
        batch, line = test_make_batch_and_line(ref='batch-001', order_id='order-ref',
                                               sku="SMALL_TABLE", batch_qty=20,
                                               line_qty=2, eta=date.today())

        print(batch)
        print(line)


if __name__ == '__main__':
    unittest.main()


@dataclass(frozen=True)
class OrderLine:
    order_id: str
    sku: str
    qty: int


class Batch:
    def __init__(
            self, ref: str, sku: str, qty: int, eta: Optional[date]
    ):
        self.reference: str = ref
        self.sku: str = sku
        self.available_quantity: int = qty
        self.eta: Optional[date] = eta

    def allocate(self, line: OrderLine) -> None:
        self.available_quantity -= line.qty

    def __str__(self) -> str:
        return f'Batch(reference = {self.reference}, sku = {self.sku}, available_quantity = {self.available_quantity}, eta = {self.eta})'
