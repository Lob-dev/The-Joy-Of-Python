import unittest
from collections import namedtuple
from dataclasses import dataclass
from datetime import date
from typing import Optional, NamedTuple


def make_batch_and_line(ref: str, order_id: str, sku: str, batch_qty: int, line_qty: int, eta: date) -> object:
    return (
        Batch(ref=ref, sku=sku, qty=batch_qty, eta=eta),
        OrderLine(order_id=order_id, sku=sku, qty=line_qty)
    )


# def test_allocating_to_a_batch_reduces_the_available_quantity() -> None:
#     batch: Batch = Batch(ref='batch-001', sku='SMALL_TABLE', qty=20, eta=date.today())
#     line: OrderLine = OrderLine(order_id='order-ref', sku='SMALL_TABLE', qty=2)
#
#     batch.allocate(line)
#
#     assert batch.available_quantity == 18


class DomainModelTest(unittest.TestCase):

    def test_make(self) -> None:
        batch, line = make_batch_and_line(ref='batch-001', order_id='order-1', sku='SMALL_TABLE', batch_qty=20,
                                          line_qty=2, eta=date.today())
        print(batch)
        print(line)

    def test_cannot_allocate_if_available_greater_then_required(self) -> None:
        batch, line = make_batch_and_line(ref='batch_001', order_id='order-123', sku='ELEGANT-LAMP', batch_qty=20,
                                          line_qty=2, eta=date.today())
        assert batch.can_allocate(line) is True

    def test_cannot_allocate_if_available_greater_then_required(self) -> None:
        batch, line = make_batch_and_line(ref='batch_001', order_id='order-123', sku='ELEGANT-LAMP', batch_qty=2,
                                          line_qty=20, eta=date.today())
        assert batch.can_allocate(line) is False

    def test_batches(self) -> None:
        batch, line = make_batch_and_line(ref='batch_001', order_id='order-123', sku='ANGULAR-DESK', batch_qty=20,
                                          line_qty=2, eta=date.today())
        batch.allocate(line)
        batch.allocate(line)
        assert batch.available_quantity == 18

    def test_quantity(self) -> None:
        assert Money('gbp', 10) == Money('gbp', 10)
        assert Name('Harry', 'Percival') != Name('Bob', 'Gregory')
        assert Line('RED-CHAIR', 5) == Line('RED-CHAIR', 5)


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
        self.eta: Optional[date] = eta
        self._purchased_quantity: int = qty
        self._allocations: set[OrderLine] = set()

    def allocate(self, line: OrderLine) -> None:
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine) -> None:
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def __str__(self) -> str:
        return f'Batch(reference = {self.reference}, sku = {self.sku}, available_quantity = {self.available_quantity}, eta = {self.eta})'

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str


class Money(NamedTuple):
    currency: str
    value: int


Line = namedtuple('Line', ['sku', 'qty'])
