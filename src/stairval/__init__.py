"""
Stairval is a framework for validating hierarchical data structures.
"""


from ._auditor import Auditor, Notepad, Issue, Level

__version__ = "0.1.0.dev0"

__all__ = [
    "Auditor", "Notepad", "Issue", "Level",
]
