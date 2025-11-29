"""
Core matchmaking algorithm based on forensic psychology & magical weighting.
"""

from typing import Dict
from math import sqrt

# Import from flat file (no folder)
from matchmaker_profiles import UserProfile


class Matchmaker:
    """
    The master algorithm that calculates compatibility between two profiles.
    """

    def __init__(self):
        # research-based weight placeholders
        self.weights = {
            "mbti": 0.15,
            "enneagram": 0.15,
            "ocean": 0.20,
            "attachment": 0.10,
            "love_languages": 0.05,
            "values": 0.15,
            "goals": 0.10,
            "trauma_patterns": 0.10,
        }

    def calculate_score(self, profile_a: UserProfile, profile_b: UserProfile) -> Dict[str, float]:
        """
        Returns a dictionary with:
        - category scores
        - overall compatibility
        - magical adjustment
        """

        category_results = {}
        total_weight = 0
        weighted_sum = 0

        for category, weight in self.weights.items():
            score_a = profile_a.scores.get(category)
            score_b = profile_b.scores.get(category)

            if score_a is None or score_b is None:
                continue

            diff = abs(score_a - score_b)
            category_score = max(0, 100 - (diff * 20))  # temporary scoring curve

            category_results[category] = category_score
            weighted_sum += category_score * weight
            total_weight += weight

        # Raw compatibility
        raw_score = weighted_sum / total_weight if total_weight > 0 else 0

        # Magical multiplier (Mystic Enchantress energy ✨)
        magical_factor = sqrt(raw_score) * 1.2

        final_score = min(100, (raw_score + magical_factor) / 2)

        return {
            "category_scores": category_results,
            "raw_compatibility": round(raw_score, 2),
            "final_compatibility": round(final_score, 2),
        }
        
        """
matchmaker.py
Core algorithm for Mystic Enchantress Match-Making.
"""

from matchmaker_profiles import UserProfile

class MatchMaker:
    """
    Computes compatibility between two UserProfile objects.
    """

    def __init__(self):
        # Weight settings (can be changed later)
        self.weights = {
            "mbti": 0.25,
            "enneagram": 0.25,
            "attachment": 0.25,
            "values": 0.25
        }

    def compare_strings(self, a, b):
        """Simple string similarity placeholder."""
        if not a or not b:
            return 0
        return 100 if a.lower() == b.lower() else 0

    def compare_lists(self, list_a, list_b):
        """Compare list overlap (e.g., values, goals)."""
        if not list_a or not list_b:
            return 0
        overlap = len(set(list_a).intersection(set(list_b)))
        total = max(len(list_a), len(list_b))
        return (overlap / total) * 100

    def compatibility_score(self, p1: UserProfile, p2: UserProfile):
        """Calculates full compatibility score."""
        scores = {}

        # MBTI match
        scores["mbti"] = self.compare_strings(p1.mbti, p2.mbti)

        # Enneagram match
        scores["enneagram"] = self.compare_strings(p1.enneagram, p2.enneagram)

        # Attachment style safety
        scores["attachment"] = self.compare_strings(
            p1.attachment_style,
            p2.soothing_style
        )

        # Shared values
        scores["values"] = self.compare_lists(p1.values, p2.values)

        # Weighted score
        final_score = sum(scores[key] * self.weights[key] for key in scores)

        return round(final_score, 2), scores
