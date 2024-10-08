import typing

from ._api import Notepad


class NotepadTree(Notepad):
    """
    `NotepadTree` implements :class:`Notepad` using a tree where each tree node corresponds to a (sub)section. The node
    can have `0..n` children.

    Each node has a :attr:`label`, a collection of issues, and children with subsections. For convenience, the node
    has :attr:`level` to correspond to the depth of the node within the tree (the level of the root node is `0`).

    The nodes can be accessed via :attr:`children` property or through convenience methods for tree traversal,
    either using the visitor pattern (:func:`visit`) or by iterating over the nodes via :func:`iterate_nodes`.
    In both cases, the traversal is done in the depth-first fashion.
    """

    # NOT PART OF THE PUBLIC API!

    def __init__(
        self,
        label: str,
        level: int,
    ):
        super().__init__(label, level)
        self._children: typing.MutableSequence["NotepadTree"] = []

    def add_subsection(self, label: str) -> "NotepadTree":
        sub = NotepadTree(label, self._level + 1)
        self._children.append(sub)
        return sub

    def add_subsections(
        self,
        *labels: str,
    ) -> typing.Sequence["NotepadTree"]:
        nodes = []
        for label in labels:
            parent = self if len(nodes) == 0 else nodes[-1]
            node = NotepadTree(label, parent.level + 1)
            nodes.append(node)

        return tuple(nodes)

    def iter_sections(self) -> typing.Iterator["Notepad"]:
        """
        Iterate over nodes in the depth-first fashion.

        Returns: a depth-first node iterator.
        """
        stack = [
            self,
        ]
        while stack:
            node = stack.pop()
            stack.extend(reversed(node._children))
            yield node

    def __str__(self):
        return (
            "NotepadTree("
            f"label={self._label}, "
            f"level={self._level}, "
            f"children={[ch.label for ch in self._children]}"
            ")"
        )
