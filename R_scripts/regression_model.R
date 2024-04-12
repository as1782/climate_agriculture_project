#This script is for the impact regression model

#ensure the directory is correctly specified locally

library(readr)

dataframe <- read_csv("dataframe.csv")

#check if the dataset has been loaded correctly

View(dataframe)

str(dataframe)

head(dataframe)

#Check for missing values before regression

sum(is.na(dataframe$Country))

sum(is.na(dataframe$Code))

sum(is.na(dataframe$Year))

sum(is.na(dataframe$`Precipitation mm per year`))

sum(is.na(dataframe$`Cereal yield kg per hectar`))

sum(is.na(dataframe$Annual_Temp))

sum(is.na(dataframe$`Annual CO₂ emissions (per capita)`))

#Beware that the CO₂ is noted diffrently in the dataset not as CO2

names(dataframe)

#dropping missing values

dataframe <- na.omit(dataframe)

model <- lm(`Cereal yield kg per hectar` ~ `Annual_Temp` + `Annual CO₂ emissions (per capita)` + `Precipitation mm per year`, data = dataframe)

summary(model)
