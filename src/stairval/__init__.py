"""
Stairval is a framework for validating hierarchical data structures.
"""

from ._api import Level, Issue
from ._auditor import Auditor, ITEM

__version__ = "0.1.1.dev0"

__all__ = [
    "Auditor", "Notepad", "Issue", "Level", "ITEM",
]
