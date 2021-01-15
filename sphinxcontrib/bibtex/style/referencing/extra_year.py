import dataclasses

from typing import TYPE_CHECKING, List, Iterable
from pybtex.style.template import field
from sphinxcontrib.bibtex.style.template import reference
from . import BaseReferenceStyle, BracketStyle

if TYPE_CHECKING:
    from pybtex.richtext import BaseText
    from pybtex.style.template import Node


@dataclasses.dataclass
class ExtraYearReferenceStyle(BaseReferenceStyle):
    """Reference just by year."""

    bracket: BracketStyle = BracketStyle()

    def get_role_names(self) -> Iterable[str]:
        return ['year', 'yearpar']

    def get_outer(
            self, role_name: str, children: List["BaseText"]) -> "Node":
        return self.bracket.get_outer(
            children,
            brackets='par' in role_name,
            capfirst=False,
        )

    def get_inner(self, role_name: str) -> "Node":
        return reference[field('year')]
