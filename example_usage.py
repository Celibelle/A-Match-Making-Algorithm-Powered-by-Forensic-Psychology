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
