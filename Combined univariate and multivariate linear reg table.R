# import required packages
library(readxl)
library(dplyr)
library(gtsummary)
library(stringr)

# load the data
healthcare_data <- read_excel("Machine Learning/Supervised Learning/Linear Regression/healthcare_data.xlsx", 
                              sheet = "healthcare_data")

# check columns
colnames(healthcare_data)  


# explanatory variables
explanatory <- c("age", "bmi", "blood_pressure", "cholesterol_level",
                 "smoker", "exercise_freq", "diabetes", "region" ,"sex")
#dependent varibale
dependent <- "medical_cost"

# sample univariate model
un <- lm(medical_cost~ age, data = healthcare_data)

summary(un)

# creating each will be tiresome 

# Univariate linear regression model using GT Summary
univ_model <- healthcare_data %>% 
  dplyr::select(all_of(explanatory), all_of(dependent)) %>% ## select variables of interest
  tbl_uvregression(                         ## produce univariate table
    method = lm,                            ## define regression (linear model)
    y = dependent,                          ## define outcome variable
    exponentiate = FALSE,                    ## do not exponentiate, as we're dealing with linear regression
    # add labels
    label =list(
      age ~ "Age",
      bmi ~ "Body Mass Index",
      blood_pressure ~ "Blood Pressure",
      cholesterol_level ~ "Cholesterol Level",
      smoker ~ "Smoker",
      exercise_freq ~ "Exercise Frequency",
      diabetes ~ "Diabetes",
      sex ~ "Sex",
      region ~ "Region"
      
    )
  )

# View univariate results table 
univ_model

# Multivariate model

# Multivariate linear regression model
mv_reg_model <- explanatory %>%  ## begin with vector of explanatory column names
  str_c(collapse = "+") %>%      ## combine all names of the variables of interest separated by a plus
  str_c(paste0(dependent, " ~ "), .) %>%    ## combine the names of variables of interest with outcome in formula style
  lm(data = healthcare_data)       ## define your dataset and fit the linear model


# Fit the multivariable linear regression model into a Gt summary table
mv_final_table <- tbl_regression(
  mv_reg_model, intercept = TRUE, # include intercept
  # add labels
  label =list(
    age ~ "Age",
    bmi ~ "Body Mass Index",
    blood_pressure ~ "Blood Pressure",
    cholesterol_level ~ "Cholesterol Level",
    smoker ~ "Smoker",
    exercise_freq ~ "Exercise Frequency",
    diabetes ~ "Diabetes",
    sex ~ "Sex",
    region ~ "Region"
  )
)


# Merge the two tables
combined_tab <- tbl_merge(
  tbls = list(univ_model, mv_final_table),   # combine
  tab_spanner = c("**Univariate**", "**Multivariable**") # set header names
)

# Print the combined table
print(combined_tab)
