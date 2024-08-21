import pytest
import io


from .simple import Person, Address, PersonAuditor, AddressAuditor


class TestAuditor:

    @pytest.fixture(scope='class')
    def auditor(self) -> PersonAuditor:
        return PersonAuditor(
            address_auditor=AddressAuditor(),
        )

    def test_ok_person(
        self,
        auditor: PersonAuditor,
    ):
        person = Person(
            name="Jack Black",
            age=43,
            address=Address(
                street="331 Farmington Ave",
                city="West Hartford",
                zip_code="06119",
                country="United States of America",
            )
        )

        notepad = auditor.prepare_notepad('person')
        auditor.process(person, notepad)

        buf = io.StringIO()
        notepad.summarize(file=buf)

        assert buf.getvalue() == "No errors or warnings were found"
