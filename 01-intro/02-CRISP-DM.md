# ML Project Process — CRISP-DM

> **CRISP-DM = A structured process for organizing Machine Learning projects.**

## CRISP-DM Process

```text
┌─────────────────────────┐    ┌──────────────────────┐    ┌──────────────────────┐
│ Business Understanding  │ →  │ Data Understanding   │ →  │ Data Preparation     │
└─────────────────────────┘    └──────────────────────┘    └──────────────────────┘
                                                                      ↓
┌─────────────────────────┐    ┌──────────────────────┐    ┌──────────────────────┐
│ Deployment              │ ←  │ Evaluation           │ ←  │ Modeling             │
└─────────────────────────┘    └──────────────────────┘    └──────────────────────┘
             ↑
             └──────────────────── Iterate ────────────────┘
```
## The 6 Steps

| **1. Business Understanding**                     | **2. Data Understanding**                            | **3. Data Preparation**                                              |
| ------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------- |
| Define the **problem** and a **measurable goal**. | Understand the **available data** and its quality.   | Prepare raw data for the ML model.                                   |
| **Example:** Reduce spam complaints by 50%.       | Is it reliable? Is it large enough? What is missing? | Clean data → Extract features → Build pipelines → Create `X` and `y` |

| **4. Modeling**                                     | **5. Evaluation**                                    | **6. Deployment**                                                  |
| --------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------ |
| Train different models and select the **best one**. | Check whether the model meets the **business goal**. | Put the model into **production** for real users.                  |
| `X + y → Train → Compare → Best Model`              | `Model → Evaluate → Goal achieved?`                  | Focus on **reliability, monitoring, maintainability, scalability** |

## Iteration

ML projects **do not end after deployment**.

```text
Build → Evaluate → Deploy → Learn from Feedback
  ↑                                      ↓
  └────────────── Improve ───────────────┘
```

> **Start simple → Deploy → Learn from feedback → Improve → Repeat**

