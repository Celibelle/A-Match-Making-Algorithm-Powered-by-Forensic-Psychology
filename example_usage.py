from matchmaker import Matchmaker
from matchmaker_profiles import UserProfile

# Create profiles
profile1 = UserProfile(name="Araceli")
profile1.add_score("mbti", 90)
profile1.add_score("enneagram", 88)

profile2 = UserProfile(name="Partner")
profile2.add_score("mbti", 85)
profile2.add_score("enneagram", 91)

# Run algorithm
matcher = Matchmaker()
result = matcher.calculate_score(profile1, profile2)

print("\n✨ Matchmaking Result ✨")
print(result)


from matchmaker_profiles import UserProfile
from matchmaker import MatchMaker

# Example profiles until workbook answers are ready
araceli = UserProfile(
    name="Araceli",
    mbti="INTJ",
    enneagram="5w4",
    attachment_style="secure",
    soothing_style="reassurance",
    values=["loyalty", "family", "growth"]
)

partner = UserProfile(
    name="Partner",
    mbti="INTJ",
    enneagram="1w9",
    attachment_style="secure",
    soothing_style="kindness",
    values=["loyalty", "growth", "peace"]
)

mm = MatchMaker()
score, breakdown = mm.compatibility_score(araceli, partner)

print("✨ Compatibility Score:", score)
print("Breakdown:", breakdown)