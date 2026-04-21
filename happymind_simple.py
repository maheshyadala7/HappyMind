# HappyMind - Stress Relief Recommender
# pip install scikit-learn
# python happymind_simple.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --- DATASET ---
# [mood(1-5), screen_hours, sleep_hours, stress(1-3)]
X = [
    [1, 8, 4, 3], [1, 7, 3, 3], [2, 6, 5, 2], [2, 7, 4, 3],
    [3, 4, 6, 2], [3, 5, 6, 2], [4, 2, 8, 1], [4, 3, 7, 1],
    [5, 1, 9, 1], [5, 2, 8, 1], [1, 9, 3, 3], [2, 5, 5, 2],
    [3, 3, 7, 1], [4, 4, 6, 2], [1, 8, 3, 3], [2, 6, 4, 2],
]
# 0=Walk  1=Call Friend  2=Movie  3=Meditate  4=Journal  5=Rest
y = [3, 4, 0, 1, 0, 2, 2, 1, 5, 2, 3, 1, 5, 0, 4, 3]

ACTIVITIES = {
    0: "🚶 Go for a Walk",
    1: "📞 Call a Friend",
    2: "🎬 Watch a Movie",
    3: "🧘 Meditate",
    4: "📓 Journal",
    5: "😴 Rest / Nap"
}

# --- TRAIN MODEL ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print(f"Model Accuracy: {round(accuracy_score(y_test, model.predict(X_test)) * 100)}%\n")

# --- USER INPUT ---
print("Answer 4 quick questions (press Enter after each):\n")
mood   = int(input("Your mood today?     (1=Very Sad → 5=Very Happy) : "))
screen = int(input("Screen time (hours)? (0 to 12)                   : "))
sleep  = int(input("Sleep last night?    (0 to 12 hours)             : "))
stress = int(input("Stress level?        (1=Low  2=Medium  3=High)   : "))

# --- PREDICT ---
result = model.predict([[mood, screen, sleep, stress]])[0]
print(f"\n✅ HappyMind suggests: {ACTIVITIES[result]}")
print("💛 Do this to reduce stress and feel happier!\n")
