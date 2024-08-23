import dataclasses

from stairval import Auditor
from stairval.notepad import Notepad

"""
A toy implementation of person and address auditors.
"""


@dataclasses.dataclass
class Address:
    street: str
    city: str
    zip_code: str
    country: str


@dataclasses.dataclass
class Person:
    name: str
    age: int
    address: Address


class PersonAuditor(Auditor[Person]):

    def __init__(
        self,
        address_auditor: Auditor[Address],
    ):
        self._address_auditor = address_auditor

    def audit(
        self,
        item: Person,
        notepad: Notepad,
    ) -> Person:
        if item.age < 0:
            notepad.add_error("`age` must not be negative")

        address_notepad = notepad.add_subsection("address")
        self._address_auditor.audit(item.address, address_notepad)


class AddressAuditor(Auditor[Address]):

    def audit(
        self,
        item: Address,
        notepad: Notepad,
    ):
        if len(item.street) == 0:
            notepad.add_warning("`street` should not be empty")

        if int(item.zip_code) < 0:
            notepad.add_error("`zip_code` must not be negative")
