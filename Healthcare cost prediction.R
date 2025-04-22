# steps
# 1. Import the data
# 2. Explore the data and conduct inferential
# 3. Build the model
# 4. Interpret the model
# 5. Evaluate the model




# Linear Regression in R

# Using medical data to predict medical cost


# import the data and all required packages

library(readxl)
library(dplyr)
library(ggplot2)
library(ggthemes)
library(corrplot)
library(gtsummary)


healthcare_data <- read_excel("Machine Learning/Supervised Learning/Linear Regression/healthcare_data.xlsx", 
                              sheet = "healthcare_data")

# perform EDA
str(healthcare_data)

summary(healthcare_data)

# summary table of all variables
healthcare_data %>% 
  tbl_summary(
    type = list(
      age ~ "continuous2",
      bmi ~ "continuous2",
      blood_pressure ~ "continuous2",
      cholesterol_level ~ "continuous2",
      medical_cost ~ "continuous2",
      all_dichotomous() ~ "categorical"
    ),
    statistic = all_continuous() ~ c("{median} ({p25}, {p75})", "{mean}, {sd}", "{min}, {max}")
  )


# check for missing values
sum(is.na(healthcare_data))

# draw a histogram, for the target variable (medical_cost) with a density plot
ggplot(healthcare_data, aes(x = medical_cost)) +
  geom_histogram(aes(y = ..density..), bins = 30, fill = "#4682B4", color = "black") +
  geom_density(alpha = 0.2, fill = "red") +
  labs(x = "Medical Cost", 
       y = "Density", 
       title = "Distribution of Medical Cost") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5))

# Box plot for medical cost
ggplot(healthcare_data) +
  aes(x = "", y = medical_cost) +
  geom_boxplot(fill = "#4682B4") +
  labs(y = "Medical Cost", title = "Boxplot for Medical Cost") +
  theme_minimal()



# draw a boxplot  for the target variable (medical_cost) with respect to the categorical variable (smoker)
ggplot(healthcare_data, aes(x = smoker, y = medical_cost, fill = smoker)) +
  geom_boxplot() +
  labs(x = "Smoker", 
       y = "Medical Cost", 
       title = "Medical Cost vs Smoker") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5))

# draw subboxplot for each of the categorical variables region, sex, smoker and diabetes against the target variables
ggplot(healthcare_data, aes(x = region, y = medical_cost, fill = region)) +
  geom_boxplot() +
  labs(x = "Region", 
       y = "Medical Cost", 
       title = "Medical Cost vs Region") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5))




library(ggplot2)
library(dplyr)
library(tidyr)
library(reshape2)
library(stringr)


# Reshape the data into long format for easier plotting with facets
health_data_long <- healthcare_data %>%
  pivot_longer(cols = c("sex", "region", "smoker", "diabetes"), 
               names_to = "categorical_variable", 
               values_to = "category")

# Create boxplots with facets
ggplot(health_data_long, aes(x = category, y = medical_cost, fill = category)) +
  geom_boxplot() +
  facet_wrap(~ categorical_variable, scales = "free_x", nrow = 2) + # Create subplots
  labs(
    x = "Category",
    y = "Medical Cost",
    title = "Medical Cost by Categorical Variables"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, size = 20),
    axis.text.x = element_text(angle = 45, hjust = 1),
    strip.text = element_text(size = 15) # Increase facet label size
  ) +
  scale_fill_tableau()



# correlation matrix between Z and continuous variables

library(corrplot)
library(RColorBrewer)

# Select only numeric columns
numeric_cols <- sapply(healthcare_data, is.numeric)
numeric_data <- healthcare_data[, numeric_cols]

# Calculate the correlation matrix
correlation_matrix <- cor(numeric_data)
# Plot the correlation matrix
corrplot(correlation_matrix, type="upper", order="hclust", method="shade",
         col=brewer.pal(n=8, name="RdBu"), addCoef.col = "black")





# build a linear model

medical_cost_model <- lm(medical_cost ~ ., data = healthcare_data)



summary(medical_cost_model)

  
# plot the model
plot(medical_cost_model)
