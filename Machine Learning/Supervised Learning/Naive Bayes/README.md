# 🧠 Introduction to Naive Bayes Classifier

Naive Bayes is a simple yet powerful probabilistic classifier based on **Bayes’ Theorem** with a strong (naive) assumption of independence among features. It is widely used for text classification, spam detection, medical diagnosis, and sentiment analysis.

---

## 📌 What is Naive Bayes?

Naive Bayes is a **supervised learning algorithm** used for classification tasks. It assumes that the presence (or absence) of a particular feature in a class is independent of the presence (or absence) of other features.

Despite its simplicity and the strong independence assumption, it performs remarkably well on many real-world problems.

---

## 📐 Bayes' Theorem

At the core of Naive Bayes lies **Bayes' Theorem**, which is used for calculating conditional probability.

Conditional probability is a measure of the probability of an event occurring given that another event has (by assumption, presumption, assertion, or evidence) occurred.

Bayes' theorem describes the probability of an event based on prior knowledge of conditions related to the event.

### **Formula:**

$$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$$

Where:

- $$P(A|B)$$: Posterior probability of class $$A$$ given predictor $$B$$  
- $$P(B|A)$$: Likelihood of predictor $$B$$ given class $$A$$  
- $$P(A)$$: Prior probability of class $$A$$  
- $$P(B)$$: Prior probability of predictor $$B$$

In classification:

$$
P(\text{Class} | \text{Features}) = \frac{P(\text{Features} | \text{Class}) \cdot P(\text{Class})}{P(\text{Features})}
$$

---

## 🧮 Simple Example: Weather & Play Tennis

| Outlook | Temperature | Humidity | Wind  | PlayTennis |
|---------|-------------|----------|-------|------------|
| Sunny   | Hot         | High     | Weak  | No         |
| Overcast| Hot         | High     | Strong| Yes        |
| Rain    | Mild        | High     | Weak  | Yes        |
| Sunny   | Cool        | Normal   | Strong| Yes        |

We want to compute:

$$
P(\text{PlayTennis} = \text{Yes} | \text{Outlook} = \text{Sunny})
$$

Using Bayes’ Theorem:

$$
P(\text{Yes} | \text{Sunny}) = \frac{P(\text{Sunny} | \text{Yes}) \cdot P(\text{Yes})}{P(\text{Sunny})}
$$

Assume:

- $$P(\text{Sunny} | \text{Yes}) = \frac{2}{9}$$
- $$P(\text{Yes}) = \frac{9}{14}$$  
- $$P(\text{Sunny}) = \frac{5}{14}$$

Then:

$$
P(\text{Yes} | \text{Sunny}) = \frac{\frac{2}{9} \cdot \frac{9}{14}}{\frac{5}{14}} = \frac{2}{5} = 0.4
$$

We’d also compute \( P(\text{No} | \text{Sunny}) \) and classify based on the higher value.

---

## 🤔 Why "Naive"?

Because it **naively assumes that all features are independent**, which is rarely true in real life. However, this assumption simplifies computation and still yields competitive performance.

### Formula for multiple features:

$$
P(C | x_1, x_2, ..., x_n) \propto P(C) \cdot \prod_{i=1}^{n} P(x_i | C)
$$

Where:

- \( C \): Class  
- \( x_1, ..., x_n \): Feature values

---

## 🔍 Types of Naive Bayes Classifiers

1. **Gaussian Naive Bayes** – Assumes features follow a normal distribution  
2. **Multinomial Naive Bayes** – Best for discrete counts (e.g., word counts)  
3. **Bernoulli Naive Bayes** – For binary features (e.g., word present or not)

---

## 💼 Applications

- **Text classification** (spam filtering, sentiment analysis)  
- **Medical diagnosis**  
- **Recommendation systems**  
- **Credit scoring**  
- **Email filtering**

---

## ✅ Pros and ❌ Cons

### ✅ Pros:
- Fast and efficient for large datasets  
- Performs well with high-dimensional data  
- Easy to implement and interpret  
- Handles categorical data well  
- Robust to irrelevant features

### ❌ Cons:
- Strong independence assumption is often unrealistic  
- Not ideal for continuous features unless assumptions are met  
- Can struggle with unseen feature values (zero-frequency)

---

## 🛠️ Laplace Smoothing

To address the **zero-frequency problem**, where a feature-class combination is not seen in training data:

$$
P(x_i | C) = \frac{\text{count}(x_i \text{ in } C) + 1}{\text{count}(C) + k}
$$

Where \( k \) is the number of unique values of \( x_i \).

---

## 📚 Summary

- Naive Bayes is a probabilistic classifier based on Bayes’ Theorem.  
- Assumes feature independence for simplification.  
- Despite this, it performs surprisingly well in many real-world tasks.  
- Commonly used in text and document classification.

---



## 📎 References

- Murphy, K. P. (2012). *Machine Learning: A Probabilistic Perspective*  
- [Wikipedia: Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)  
- [scikit-learn docs on Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)
