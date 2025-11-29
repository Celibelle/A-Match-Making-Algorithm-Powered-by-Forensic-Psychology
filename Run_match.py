from matchmaker.algorithm.matchmaker_engine import MatchmakerEngine
from matchmaker.algorithm.weighting import research_weights

# Placeholder profiles (will be replaced with real data later)
person1 = {}
person2 = {}

engine = MatchmakerEngine(weights=research_weights())

score = engine.final_score(person1, person2)

print("✨ Final Compatibility Score:", score)
