import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# Veriyi yükle
df = pd.read_csv("mushroom.csv")

# Hedef değişkeni oluştur (class=e sütunundan)
df["target"] = df["class=e"].apply(lambda x: 'e' if x == 1 else 'p')

# Özelliklerden class=e ve class=p sütunlarını çıkar
X = df.drop(columns=["class=e", "class=p", "target"])
y = df["target"]

# Eğitim/test ayrımı
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model oluştur ve eğit
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Kaydet
joblib.dump(model, "mushroom_model.pkl")
print("✅ Model eğitildi ve mushroom_model.pkl olarak kaydedildi.")
