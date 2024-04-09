#This script is for the impact regression model

install.packages("tidyverse")
install.packages("broom")
install.packages("grf")
library(tidyverse)
library(broom)
library(readr)
#ensure the directory is correctly specified locally
updated_final_dataframe <- read_csv("Desktop/Uni/Data Science in Economics/empirical_project/climate_agriculture_project/updated_final_dataframe.csv")
#check if the dataset has been loaded correctly
View(updated_final_dataframe)
str(updated_final_dataframe)
head(updated_final_dataframe)
#Check for missing values before regression
sum(is.na(updated_final_dataframe$Country))
sum(is.na(updated_final_dataframe$Code))
sum(is.na(updated_final_dataframe$Year))
sum(is.na(updated_final_dataframe$`Precipitation mm per year`))
sum(is.na(updated_final_dataframe$`Cereal yield kg per hectar`))
sum(is.na(updated_final_dataframe$Annual_Temp))
sum(is.na(updated_final_dataframe$`Annual CO₂ emissions (per capita)`))
#Beware that the CO₂ is noted diffrently in the dataset not as CO2
names(updated_final_dataframe)
#dropping missing values
updated_final_dataframe <- na.omit(updated_final_dataframe)
model <- lm(`Cereal yield kg per hectar` ~ `Annual_Temp` + `Annual CO₂ emissions (per capita)` + `Precipitation mm per year`, data = updated_final_dataframe)
summary(model)