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
