# 🍄 Mushroom Classification with Machine Learning

This project uses machine learning to classify mushrooms as **edible** (`e`) or **poisonous** (`p`) based on various morphological features.

---

## 📁 Dataset

- **Source**: [UCI Mushroom Dataset](https://archive.ics.uci.edu/dataset/73/mushroom)
- **Samples**: 8124
- **Original Features**: 22 categorical (e.g., cap-shape, odor, stalk-root)
- **Preprocessing**: One-Hot Encoding applied for model compatibility

---

## 🧠 Model Information

- **Algorithm**: Decision Tree Classifier  
- **Training/Test Split**: 80% / 20%  
- **Cross-Validation**: 5-Fold (Average Accuracy: ~96.6%)  
- **Test Accuracy**: ~100%

### 🔍 Feature Importance (Top 5)

Based on the Decision Tree model:

1. `odor=n`
2. `stalk-root=c`
3. `spore-print-color=r`
4. `stalk-surface-below-ring=y`
5. `habitat=d`

---

## ⚙️ How It Works

You provide one-hot encoded features like `cap-shape=c`, `odor=n`, etc.  
The model then predicts:

- `"e"` → Edible  
- `"p"` → Poisonous

Sample input format is shown in `sample_input.json`.

---

## 🚀 Quick Usage (Python)

```python
import joblib
import pandas as pd

model = joblib.load("mushroom_model.pkl")

sample = pd.DataFrame([{
    "cap-shape=c": 1,
    "cap-color=n": 1,
    "odor=n": 1,
    ...
}])

prediction = model.predict(sample)[0]
print("Prediction:", prediction)


📦 Project Files
File Name	Description
mushroom_model.pkl	Trained Decision Tree model
sample_input.json	Example of one-hot encoded input
model.py	Script for model training
app.py	Streamlit web interface
README.md	This project explanation file
requirements.txt	Python dependencies


 How to Run Locally
Install dependencies:

pip install -r requirements.txt

Launch the Streamlit app:
streamlit run app.py


🌐 Live Demo and Deployment
You can deploy this model to:

Hugging Face for API access and hosting the model

GitHub for open sharing and collaboration

Streamlit Cloud for an interactive app


🧪 Model Testing on Hugging Face
You can test the model by uploading:

mushroom_model.pkl

sample_input.json

requirements.txt

README.md

Visit: https://huggingface.co (yazodi)

📄 License
MIT License – for educational and non-commercial purposes.