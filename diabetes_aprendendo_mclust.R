install.packages('mclust')
install.packages('car')
library(mclust)
data(diabetes)
X = diabetes[,-1]
class = diabetes$class
clPairs(X, class)
BIC = mclustBIC(X)
plot(BIC)


data("faithful")
head(faithful)
library("ggplot2")
ggplot(faithful, aes(x=eruptions, y=waiting)) +
  geom_point() +  # Scatter plot
  geom_density2d() # Add 2d density estimation
Mclust(data, G = NULL)

