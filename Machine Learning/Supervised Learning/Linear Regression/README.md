# Linear Regression

## Introduction

Linear regression is a fundamental statistical and machine learning technique used to model relationships between a dependent variable and one or more independent variables. It assumes a linear relationship between input features and output predictions.

## Applications of Linear Regression

Linear regression is widely used in various industries, including:
- **Finance:** Predicting stock prices, credit risk assessment, and portfolio optimization.
- **Healthcare:** Estimating patient recovery time, analyzing drug effectiveness.
- **Marketing:** Forecasting sales based on advertising spend, customer behavior modeling.
- **Economics:** Understanding the impact of inflation on consumer spending.
- **Engineering:** Predicting system performance based on environmental variables.

---

## Assumptions of Linear Regression
For linear regression to work effectively, the following assumptions should be met:
1. **Linearity:** The relationship between independent and dependent variables is linear.
2. **Independence:** Observations are independent of each other.
3. **Homoscedasticity:** Constant variance of errors across all levels of the independent variable.
4. **Normality of Residuals:** Residuals should be approximately normally distributed.
5. **No Multicollinearity:** Independent variables should not be highly correlated with each other.

---

## Simple Linear Regression

In simple linear regression, the relationship between the dependent variable $Y$ and a single independent variable $X$ is modeled as:

$$
Y = b_0 + b_1X + \epsilon
$$

Where:
- $Y$ = Dependent variable
- $X$ = Independent variable
- $b_0$ = Intercept (bias term)
- $b_1$ = Slope (coefficient of $X$)
- $\epsilon$ = Error term

---

## Multiple Linear Regression

When there are multiple independent variables, the equation extends to:

$$
Y = b_0 + b_1X_1 + b_2X_2 + ... + b_nX_n + \epsilon
$$

Where $X_1, X_2, ..., X_n$ are independent variables.

---

## Derivation of $b_0$ and $b_1$ Using the Least Squares Approach

Using the ordinary least squares (OLS) method, the best-fitting line minimizes the sum of squared residuals:

$$
b_1 = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sum (X_i - \bar{X})^2}
$$

$$
b_0 = \bar{Y} - b_1 \bar{X}
$$

Where:
- $\bar{X}$ and $\bar{Y}$ are the means of $X$ and $Y$.
- $X_i, Y_i$ are individual data points.

---

## Checking Assumptions

Before applying linear regression, we validate the assumptions using:
- **Scatter plots:** Check for linearity.
- **Residual plots:** Evaluate homoscedasticity.
- **Histogram/Q-Q plot:** Assess normality of residuals.
- **Variance Inflation Factor (VIF):** Detect multicollinearity.

---

## Model Evaluation

To assess the performance of a linear regression model, we use:
- **R-squared ($R^2$)**: Explains the proportion of variance captured by the model.
- **Adjusted $R^2$**: Adjusted version of $R^2$ for multiple predictors.
- **Mean Squared Error (MSE)**: Measures the average squared difference between actual and predicted values.
- **Root Mean Squared Error (RMSE)**: Square root of MSE, useful for interpretation.
- **Residual Plots:** Visual validation of assumptions and model fit.

---

## Conclusion

Linear regression is an essential statistical and machine learning tool used across industries for predictive modeling and relationship analysis. A proper understanding of its assumptions, derivation, and evaluation techniques ensures optimal applications in real-world scenarios.

---
