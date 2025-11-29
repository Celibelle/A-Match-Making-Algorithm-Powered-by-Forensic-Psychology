"""
Profile definitions for the Forensic Psychology–Powered Matchmaking Algorithm.
These act as data containers for all personality + psychological inputs.
"""

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class UserProfile:
    """
    A flexible profile structure that will later store:
    - MBTI
    - Enneagram
    - OCEAN
    - Attachment Style
    - Love Language
    - Shadow Traits
    - Trauma Profile
    - Values & Morals
    - Dealbreakers
    - Behavioral Patterns
    - Future Goals
    - Relationship Archetype
    """
    name: str
    traits: Dict[str, Any] = field(default_factory=dict)
    scores: Dict[str, float] = field(default_factory=dict)

    def add_trait(self, category: str, value: Any):
        """Store traits like MBTI='INTJ', Enneagram='5w4', etc."""
        self.traits[category] = value

    def add_score(self, category: str, score: float):
        """Scores will be used in the algorithm weighting system."""
        self.scores[category] = score
