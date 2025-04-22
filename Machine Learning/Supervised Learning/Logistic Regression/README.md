# 📊 Logistic Regression – A Comprehensive Introduction

## 📘 What is Logistic Regression?

**Logistic Regression** is a statistical modeling technique used to predict the **probability of a binary outcome** (i.e., a variable that takes values like 0/1, True/False, Yes/No). It is a **modified version of Linear Regression**, tailored for **classification tasks**, where the dependent variable is categorical rather than continuous.

Unlike linear regression, which predicts real-valued outputs, logistic regression maps predictions to **probabilities** using the **sigmoid function**. This makes it suitable for **classification** rather than regression.

---

## 🔍 Applications Across Industries

Logistic regression is widely used across domains for **classification problems**, including:

- **Healthcare**: Predicting disease presence (e.g., diabetes = yes/no)
- **Finance**: Loan default prediction, fraud detection
- **Marketing**: Predicting whether a customer will buy a product
- **E-commerce**: Click-through rate prediction
- **Human Resources**: Employee attrition prediction

---

## 📀 Logistic Regression Equation

Logistic Regression models the **log-odds** of the probability $p$ as a linear function of the input features:

$$
\log\left(\frac{p}{1 - p}\right) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_k x_k
$$

Solving for $p$ gives the **sigmoid function**:

$$
p = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_k x_k)}}
$$

---

## 📈 The Sigmoid Function
- Takes any values and outputs it to be between 0 and 1
- This means we can take our Linear Regression Solution and place it into the Sigmoid Function 

The **sigmoid** (or logistic) function is:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

- It has an S-shaped curve that:
  - Maps any real value $z$ to a value between 0 and 1
  - Is centered at 0
  - Is differentiable and useful for optimization

![image](https://github.com/user-attachments/assets/58674b3c-7efa-4fa7-8735-ee0a099d1b3d)

- The function is used for three models: Probit, logistic, Complementary Log-Log Response Function

- The linear regression is converted to logistic regression such that we only have two outcomes
- The probability threshold is set at 0.5, meaning values less than 0.5 are set to 0 will those above set to 1

![image](https://github.com/user-attachments/assets/76b77b9e-04ba-4507-bd6e-79baeee8d302)

---

## ✅ Why Not Use Linear Regression for Classification?

**Non-Normal Error Terms**
- One assumption of a linear regression is the normality of error terms. For binary 0, 1 response variable each error term can take two values

$$
\epsilon_i = Y_i - (\beta_0 + \beta_1 X_i)
$$

When 

$$ Y_i = 1 $$

Then

  $$ \epsilon_i = 1 - \beta_0 - \beta_1 X_i $$
  
And when

$$ Y_i = 0 $$

Then

$$ \epsilon_i = -\beta_0 - \beta_1 X_i $$

- This difference is called residuals, and they are not normally distributed because the outcomes are discrete (0,1), not continuous

![image](https://github.com/user-attachments/assets/c32cbbd5-d088-460e-b8c2-6b61560ff1c2)

**Non-Constant Error Variance**
- Linear regression also assumes the equality of variances of error terms (Homoscedasticity). This means that the variability of the residuals (errors) should be the same across all levels of the independent variables.
- Binary response outcomes violates this assumption

$$
\sigma^2 [Y_i ]= E[Y_i - E[Y_i ]]^2 = (1 - \pi_i)^2 \pi_i + 0(1 - \pi_i )^2 (1 - \pi_i ) = \pi_i (1 - \pi_i ) = E[Y_i](1 - E[Y_i])
$$

$$
\sigma^2 [Y_i ]= E[Y_i](1 - E[Y_i]) = (\beta_0 + \beta_1 X_i)(1 - \beta_0 - \beta_1 X_i)
$$

This shows that the variance of the error terms depends on the value of X. Thus, error variances depend on the value of X, and ordinary least squares will no longer be optimal.

**Constraints on Response Function**
- Since the response function represents probabilities when the outcome variable is a 0, 1 indicator variable, the mean responses (probabilities) should be constrained as follows

$$
0 \leq E[Y] = \pi \leq 1
$$

- On the other hand, the mean response for a linear regression is given by

$$
\hat{Y} = \beta_0 + \beta_1 X
$$

- As a result, the linear model can produce probabilities that are less than 0 or greater than 1, which are not valid probabilities. Thus, the probabilities 0 and 1 are reached asymptotically, in the logistic model using an S-shaped curve

![image](https://github.com/user-attachments/assets/8800a697-5aa8-4455-92f0-292fa1fd82b6)

---

## 🧐 Key Assumptions of Logistic Regression

1. **Binary Outcome Variable**: The dependent variable is binary (0/1).
2. **Linearity of Log-Odds**: The log-odds are linearly related to the independent variables.
3. **Independence**: Observations are independent of each other.
4. **Little to No Multicollinearity**: Predictors are not highly correlated with each other.
5. **Large Sample Size**: Helps ensure reliable estimates and convergence of maximum likelihood estimation.

---

## ⚙️ Fitting a simple Logistic Regression Model

- Considering the sigmoid properties and the Bernoulli distribution, we can fit the logistic function.
- The function takes the usual form of:

$$
Y_i = E[Y_i] + \epsilon_i
$$

- The distribution of the error term (ei) depends on the Bernoulli distribution of the response (Yi)
- Thus, it is preferable to state the simple logistic regression model in the following fashion: Yi are independent Bernoulli random variables with expected values pi, where:

$$
\pi_i = \frac{\exp(\beta_0 + \beta_1 X_i)}{1 + \exp(\beta_0 + \beta_1 X_i)}
$$

- The X observations are assumed to be known constants. Alternatively, if the X observations are random, E[Y_i] is viewed as a conditional mean, given the value of X_i.

---

## 📊 Output Interpretation

- The interpretation of the estimated regression coefficient Beta1 in the fitted logistic response function is not as straightforward as the slope interpretation in a linear regression model.
- The reason is that the effect of a unit increase in \( X \) varies for the logistic regression model according to the location of the starting point on the \( X \) scale.
  - We consider the value of the fitted logit response function at:

$$
\( X = X_j \): \pi(X_j) = \beta_0 + \beta_1 X_j
$$

  - We also consider the value of the fitted logit response function at:

$$
\( X = X_j + 1 \): \pi(X_j + 1) = \beta_0 + \beta_1 (X_j + 1)
$$

- The difference between the two fitted values is simply:

$$
\pi(X_j + 1) - \pi(X_j) = \beta_1
$$

- which represents the odds ratio of \( X_j \):

$$
\log(odds_{S_2}) - \log(odds_{S_1}) = \frac{\log(odds_{S_2})}{\log(odds_{S_1})} = \beta_1
$$

- Taking the antilog, we obtain the odds ratio:

$$
\hat{OR} = \frac{odds_{S_2}}{odds_{S_1}} = \exp(\beta_1)
$$


---








