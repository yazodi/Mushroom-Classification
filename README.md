# 🍄 Mushroom Classification with Machine Learning

This project aims to classify mushrooms as **edible** or **poisonous** using machine learning algorithms based on various morphological features.

## 📁 Dataset

- **Source**: UCI Machine Learning Repository – [Mushroom Dataset](https://archive.ics.uci.edu/dataset/73/mushroom)
- **Samples**: 8124 mushrooms
- **Features**: 22 categorical features (cap shape, color, odor, stalk-root, etc.)
- **Target**: `edible (e)` or `poisonous (p)`

Dataset has been **preprocessed** using **One-Hot Encoding** for model compatibility.

---

## 🧠 Models Used

The following classification algorithms were applied:

| Model                 | Accuracy |
|----------------------|----------|
| Decision Tree        | 100%     |
| Random Forest        | XX%      |
| Logistic Regression  | XX%      |
| Naive Bayes          | XX%      |
| K-Nearest Neighbors  | XX%      |
| Support Vector Machine | XX%   |

> *Note: All models were trained on 80% of the data and evaluated on 20% test set.*

---

## 🔍 Feature Importance (Top 5)

Using the Decision Tree model, the most influential features were:

1. **odor=n**
2. **stalk-root=c**
3. **spore-print-color=r**
4. **stalk-surface-below-ring=y**
5. **habitat=d**

---

## 🔁 Cross Validation

5-fold cross-validation was applied to ensure generalizability:

- **Average Accuracy**: 96.6%

---

## 📊 Visualization

Decision tree structure was plotted to interpret how decisions are made based on features.

---

## 📌 Conclusion

- The mushroom dataset is highly separable.
- Simple models like Decision Trees already achieve **perfect classification** on the given dataset.
- `odor` and `stalk-root` are the most critical features for classification.

---

## 🚀 How to Run

```bash
pip install pandas scikit-learn matplotlib
```

Then open and run the Jupyter notebook:

```bash
jupyter notebook Mushroom_Classification.ipynb
```

---

## 📄 License

This project is licensed under the MIT License.
