# 🧠 HappyMind — Stress Relief Recommender

A simple Python ML project that suggests an activity to reduce stress and increase happiness.

## 🚀 Run in 2 Steps

```bash
pip install scikit-learn
python happymind_simple.py
```

## 💬 What It Does

Asks you 4 questions → predicts the best activity for you.

```
Your mood today?     (1=Very Sad → 5=Very Happy) : 2
Screen time (hours)? (0 to 12)                   : 7
Sleep last night?    (0 to 12 hours)             : 4
Stress level?        (1=Low  2=Medium  3=High)   : 3

✅ HappyMind suggests: 🧘 Meditate
💛 Do this to reduce stress and feel happier!
```

## 🔧 Tech Used

- Python
- scikit-learn (Random Forest Classifier)

## 📊 Activities It Suggests

| Output | Activity      |
|--------|---------------|
| 0      | 🚶 Go for a Walk |
| 1      | 📞 Call a Friend |
| 2      | 🎬 Watch a Movie |
| 3      | 🧘 Meditate      |
| 4      | 📓 Journal       |
| 5      | 😴 Rest / Nap    |

## 🎓 ML Concepts Used

- Supervised Learning
- Random Forest Classifier
- Train / Test Split
- Accuracy Score
