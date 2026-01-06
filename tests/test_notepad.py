import typing

import pytest

from stairval.notepad import Notepad, create_notepad


class TestNotepad:
    @pytest.fixture
    def notepad(self) -> Notepad:
        return create_notepad("badumtss")

    def test_add_subsection(
        self,
        notepad: Notepad,
    ):
        sub = notepad.add_subsection("subtss")

        assert sub.label == "subtss"
        assert sub.level == 1

    def test_subsection_labels_can_be_an_int(
        self,
        notepad: Notepad,
    ):
        assert not notepad.has_subsections()

        sub = notepad.add_subsection(321)

        assert sub.label == 321
        assert sub.level == 1

    def test_add_subsections(
        self,
        notepad: Notepad,
    ):
        assert not notepad.has_subsections()
        subs = notepad.add_subsections("foo", "bar", "baz")
        assert notepad.has_subsections()

        assert len(subs) == 3
        labels = [sub.label for sub in subs]
        assert labels == ["foo", "bar", "baz"]
        levels = [sub.level for sub in subs]
        assert levels == [1, 2, 3]
        all_labels = sorted(section.label for section in notepad.iter_sections())
        assert all_labels == ["badumtss", "bar", "baz", "foo"]

    def test_can_add_subsections_labeled_with_strs_and_ints(
        self,
        notepad: Notepad,
    ):
        assert not notepad.has_subsections()

        subs = notepad.add_subsections("foo", 493, "baz")
        assert notepad.has_subsections()

        assert len(subs) == 3
        assert [sub.label for sub in subs] == ["foo", 493, "baz"]

    def test_has_subsections(
        self,
        notepad: Notepad,
    ):
        assert not notepad.has_subsections()

        sub = notepad.add_subsection("subtss")
        assert not sub.has_subsections()

        assert notepad.has_subsections()

    def test_iter_sections_is_iterable(
        self,
        notepad: Notepad,
    ):
        assert isinstance(notepad.iter_sections(), typing.Iterable)

    def test_errors_is_iterable(
        self,
        notepad: Notepad,
    ):
        assert isinstance(notepad.errors(), typing.Iterable)

    def test_warnings_is_iterable(
        self,
        notepad: Notepad,
    ):
        assert isinstance(notepad.warnings(), typing.Iterable)
