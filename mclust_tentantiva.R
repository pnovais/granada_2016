install.packages('mclust')
library(mclust)
datas1 = read.csv('data/all_parameters_group1.csv', header = TRUE)
datas2 = read.csv('data/all_parameters_group2.csv', header = TRUE)
datas3 = read.csv('data/all_parameters_group3.csv', header = TRUE)
data = rbind(datas1,datas2,datas3)

class = data$X.Populacao
class
X = data[,-{1:2}]
X
clPairs(X, class)

#Y = data[,c(3,7,10)]
Y = data[,c(3,7,10,25)]

jpeg('graph_trending.jpg')
clPairs(Y,class)
dev.off()
BIC = mclustBIC(Y)
jpeg('bic.jpg')
plot(BIC)
dev.off()

summary(BIC)
mod1 = Mclust(Y, x = BIC)
summary(mod1, parameters = TRUE)
jpeg('mod.jpg')
plot(mod1, what = "classification")
dev.off()
table(class, mod1$classification)
jpeg('mod_sep.jpg')
par(mfrow = c(2,2))
plot(mod1, what = "uncertainty", dimens = c(2,1), main = "")
plot(mod1, what = "uncertainty", dimens = c(3,1), main = "")
plot(mod1, what = "uncertainty", dimens = c(2,3), main = "")
par(mfrow = c(1,1))
dev.off()
ICL = mclustICL(X)
summary(ICL)
jpeg('icl.jpg')
plot(ICL)
dev.off()
LRT = mclustBootstrapLRT(Y, modelName = "VVV")
LRT



hu = data[,c(11,12,13,14,15,16,17)]
jpeg('graph_trending_hu.jpg')
clPairs(hu,class)
dev.off()

BIC = mclustBIC(hu)
mod1 = Mclust(hu, x = BIC)
summary(mod1, parameters = TRUE)
png(height=1200, width=1200, pointsize=25, file="cluster_hu.png")
plot(mod1, what = "classification")
dev.off()
