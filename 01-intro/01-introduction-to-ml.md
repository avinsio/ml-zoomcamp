# Machine Learning

## 1. What is Machine Learning?

**Machine Learning (ML)** is a field of AI where we use **data to learn patterns** and use those patterns to make **predictions or decisions** on new, unseen data.

Instead of writing rules for every possible situation, we give the model data and let it learn useful patterns.

### Basic Idea
> **Machine Learning = Learn patterns from data → Use those patterns to make predictions on new data.**

```text
┌──────────┐ → ┌────────────────┐ → ┌─────────┐ → ┌──────────┐ → ┌────────────┐
│   Data   │   │ Learn Patterns │   │  Model  │   │ New Data │   │ Prediction │
└──────────┘   └────────────────┘   └─────────┘   └──────────┘   └────────────┘
```

## 2. Rule-Based Systems vs Machine Learning

### Rule-Based System

Humans **manually write rules**.

```text
Email → Check Rules → Decision
```

Example:

```text
IF sender = promotions@online.com → Spam
IF body contains "deposit" → Spam
```

### Machine Learning

The model **learns patterns from data**.

```text
Past Emails + Labels → Train Model → New Email → Spam / Not Spam
```

### Main Difference

> **Rule-Based → Humans define the rules.**
> **ML → Model learns the patterns from data.**

## 3. Supervised Machine Learning

**Supervised Learning** = training a model using **features (X)** and **known answers/targets (y)**.

```text
Features (X) + Target (y)
           ↓
        Training
           ↓
         Model
           ↓
      New Data → Prediction
```

## 4. X and y

* **X (Feature Matrix):** 2D data → rows = observations, columns = features.
* **y (Target):** 1D array/vector → the value we want to predict.

```text
X (Features)              y (Target)

┌──────────┬──────┐
│ Mileage  │ Year │ ───→ Price
├──────────┼──────┤
│ 100k     │ 2018 │ ───→ $18k
│ 60k      │ 2020 │ ───→ $22k
└──────────┴──────┘
```

## 5. Types of Supervised Learning

```text
             Supervised Learning
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
   Regression   Classification  Ranking
                    │
              ┌─────┴─────┐
              ↓           ↓
           Binary    Multi-class
```
---
### Types of Supervised Learning

| **Regression** | **Classification** | **Ranking** |
|---|---|---|
| **Target = Number** | **Target = Category** | **Ranks items by relevance/score** |
| House → `$500,000` | **Binary:** Spam / Not Spam<br>**Multi-class:** Cat / Dog / Car | Google Search<br>Product Recommendations |
---