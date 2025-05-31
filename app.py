import streamlit as st
import pandas as pd
import joblib

# Modeli yükle
model = joblib.load("mushroom_model.pkl")

# Özellikler listesi
features = [
    'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
    'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
    'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
    'stalk-surface-below-ring', 'stalk-color-above-ring',
    'stalk-color-below-ring', 'veil-type', 'veil-color',
    'ring-number', 'ring-type', 'spore-print-color',
    'population', 'habitat'
]

# Başlık
st.title("🍄 Mushroom Classification")
st.write("Bu uygulama, verilen mantar özelliklerine göre yenilebilir mi yoksa zehirli mi olduğunu tahmin eder.")

# Kullanıcı girişleri için alanlar
user_input = {}
for feature in features:
    user_input[feature] = st.selectbox(f"{feature.replace('-', ' ').capitalize()}:", 
                                       ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

# Tahmin butonu
if st.button("Tahmin Et"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]

    if prediction == 'e':
        st.success("✅ Tahmin: Edible (Yenilebilir)")
    else:
        st.error("❌ Tahmin: Poisonous (Zehirli)")
