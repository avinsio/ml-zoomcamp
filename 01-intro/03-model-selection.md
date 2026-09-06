# Model Selection

> **Model Selection = Try different models → Compare their performance → Choose the best one.**

## Train / Validation / Test

We split the data into **3 separate sets**:

```text
┌──────────────┬──────────────┬──────────────┐
│    Train     │  Validation  │     Test     │
│     60%      │     20%      │     20%      │
└──────────────┴──────────────┴──────────────┘
      ↓               ↓               ↓
   Train Model    Select Model     Final Check
````

* **Train:** Used to train the model.
* **Validation:** Used to compare models and select the best one.
* **Test:** Used only at the end to check the final model.

## Model Selection

```text
Train Data → Train Models → Validation Data
                              ↓
                       Compare Performance
                              ↓
                         Best Model
```

Example:

| Model               | Validation Accuracy |
| ------------------- | ------------------: |
| Logistic Regression |                 66% |
| Decision Tree       |                 60% |
| Random Forest       |                 67% |
| Neural Network      |               80% ⭐ |

→ **Neural Network is selected.**

## Multiple Comparison Problem

When we test many models on the same validation set, one model may perform well **just by chance**.

```text
Many Models → Same Validation Set → One May Get Lucky
```

That's why we need a separate **test set**.

## Final Model

After selecting the best model:

```text
Train + Validation Data
          ↓
    Train Final Model
          ↓
       Test Data
          ↓
   Final Performance
```

This lets the final model learn from **more data**.

## Main Idea

> **Validation → Select the best model**
> **Test → Check the final model**

---

