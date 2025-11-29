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
        
        """
matchmaker_profiles.py
Profile definitions for the Mystic Enchantress Match-Making Algorithm.
"""

class UserProfile:
    """
    Stores a user’s complete psychological + magical profile.
    Every attribute here will be filled in by your workbook answers.
    """

    def __init__(self,
                 name: str,

                 # Core Personality
                 mbti=None,
                 enneagram=None,
                 big5=None,

                 # Attachment system
                 attachment_style=None,
                 trauma_triggers=None,
                 soothing_style=None,

                 # Emotional Intelligence
                 empathy_level=None,
                 communication_style=None,
                 conflict_style=None,

                 # Life Alignment
                 values=None,
                 goals=None,
                 lifestyle_needs=None,

                 # Magical / Intuitive layer
                 soul_archetype=None,
                 love_language=None,
                 aura_color=None):

        self.name = name
        self.mbti = mbti
        self.enneagram = enneagram
        self.big5 = big5

        self.attachment_style = attachment_style
        self.trauma_triggers = trauma_triggers or []
        self.soothing_style = soothing_style

        self.empathy_level = empathy_level
        self.communication_style = communication_style
        self.conflict_style = conflict_style

        self.values = values or []
        self.goals = goals or []
        self.lifestyle_needs = lifestyle_needs or []

        self.soul_archetype = soul_archetype
        self.love_language = love_language
        self.aura_color = aura_color

    def to_vector(self):
        """
        Converts all profile attributes into a comparable numeric vector.
        For now it’s a placeholder — we will fill in the math once your workbook is complete.
        """
        vector = {}

        # TODO: Replace with real scoring logic
        vector["mbti"] = hash(self.mbti) % 100 if self.mbti else None
        vector["enneagram"] = hash(self.enneagram) % 100 if self.enneagram else None

        return vector
