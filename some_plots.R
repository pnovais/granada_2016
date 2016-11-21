install.packages('lattice')
install.packages('car')
install.packages('mclust')
install.packages('corrgram')
install.packages('ellipse')
install.packages('corrplot')
library(mclust)
library(lattice)
library(car)
library(ggplot2)
library(corrgram)
library(ellipse)
library(corrplot)
library(RColorBrewer)



datas1 = read.csv('data/all_parameters_group1.csv', header = TRUE)
datas2 = read.csv('data/all_parameters_group2.csv', header = TRUE)
datas3 = read.csv('data/all_parameters_group3.csv', header = TRUE)
data = rbind(datas1,datas2,datas3)

#Paleta de cores Brewer Color
colors <- c('#edf8fb',
             '#ccece6',
             '#99d8c9',
             '#66c2a4',
             '#41ae76',
             '#238b45',
             '#005824')


colors2 <- c('#fee5d9',
             '#fcbba1',
             '#fc9272',
             '#fb6a4a',
             '#ef3b2c',
             '#cb181d',
             '#99000d')

colors3 <- c('#eff3ff',
            '#c6dbef',
            '#9ecae1',
            '#6baed6',
            '#4292c6',
            '#2171b5',
            '#084594')

colors4 <- c('#f2f0f7',
              '#dadaeb',
              '#bcbddc',
              '#9e9ac8',
              '#807dba',
              '#6a51a3',
              '#4a1486')

#TODAS as morfologias
#Selecao das subamostras
Y = data[,c(3,7,10,24,25)]
Hu = data[,11:17]
geo = data[,c(3,18,19,20,21,22,23,24,25)]
all=data[,-c(1,2,4,6,8)]
class = data$X.Populacao

#Correlogramas 
png(height=1200, width=1200, pointsize=25, file='populacionais_all.png')
corrgram(data, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors)
dev.off()


png(height=1200, width=1200, pointsize=25, file='populacionais_RTSC.png')
corrgram(Y, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors)
dev.off()


png(height=1200, width=1200, pointsize=25, file='populacionais_hu.png')
corrgram(Hu, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors)
dev.off()


png(height=1200, width=1200, pointsize=25, file='populacionais_geom.png')
corrgram(geo, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors)
dev.off()

#Matrizes de correlação
M = cor(Y, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_RTSC.png")
corrplot(M, method = 'circle',
         col=colors,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

M = cor(Hu, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_hu.png")
corrplot(M, method = 'circle',
         col=colors,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

M = cor(geo, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_geo.png")
corrplot(M, method = 'circle',
         col=colors,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

M = cor(all, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_all.png")
cex.before <- par("cex")
par(cex = 0.7)
corrplot(M, method = 'circle',
         col=colors,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

#CLUSTERING
Y = data[,c(3,7,10,25)]
geo = data[,c(3,18,19,20,21,22,23,25)]
BIC = mclustBIC(Y)
mod1 = Mclust(Y, x = BIC)
summary(mod1, parameters = TRUE)
png(height=1200, width=1200, pointsize=25, file="cluster_RTSC.png")
plot(mod1, what = "classification")
dev.off()

BIC = mclustBIC(Hu)
mod1 = Mclust(Hu, x = BIC)
summary(mod1, parameters = TRUE)
png(height=1200, width=1200, pointsize=25, file="cluster_hu.png")
plot(mod1, what = "classification")
dev.off()

BIC = mclustBIC(geo)
mod1 = Mclust(geo, x = BIC)
summary(mod1, parameters = TRUE)
png(height=1200, width=1200, pointsize=25, file="cluster_geom.png")
plot(mod1, what = "classification")
dev.off()



#######################################################
#Fazendo o mesmo, para os diferentes tipos morfológicos
#######################################################

#GRUPO 1
#E, S0

#Selecao das subamostras
Y = datas1[,c(3,7,10,24,25)]
Hu = datas1[,11:17]
geo = datas1[,c(3,18,19,20,21,22,23,24,25)]
all=datas1[,-c(1,2,4,6,8)]

#Correlogramas 
png(height=1200, width=1200, pointsize=25, file='populacionais_all_1.png')
corrgram(data, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors2)
dev.off()


png(height=1200, width=1200, pointsize=25, file='populacionais_RTSC_1.png')
corrgram(Y, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors2)
dev.off()


png(height=1200, width=1200, pointsize=25, file='populacionais_hu_1.png')
corrgram(Hu, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors2)
dev.off()


png(height=1200, width=1200, pointsize=25, file='populacionais_geom_1.png')
corrgram(geo, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors2)
dev.off()

#Matrizes de correlação
M = cor(Y, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_RTSC_1.png")
corrplot(M, method = 'circle',
         col=colors2,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

M = cor(Hu, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_hu_1.png")
corrplot(M, method = 'circle',
         col=colors2,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

M = cor(geo, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_geo_1.png")
corrplot(M, method = 'circle',
         col=colors2,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

M = cor(all, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_all_1.png")
cex.before <- par("cex")
par(cex = 0.7)
corrplot(M, method = 'circle',
         col=colors2,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()


#GRUPO 3
#Sc, Sd/Irr

#Selecao das subamostras
Y = datas3[,c(3,7,10,24,25)]
Hu = datas3[,11:17]
geo = datas3[,c(3,18,19,20,21,22,23,24,25)]
all=datas2[,-c(1,2,4,6,8)]

#Correlogramas 
png(height=1200, width=1200, pointsize=25, file='populacionais_all_3.png')
corrgram(data, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors4)
dev.off()


png(height=1200, width=1200, pointsize=25, file='populacionais_RTSC_3.png')
corrgram(Y, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors4)
dev.off()


png(height=1200, width=1200, pointsize=25, file='populacionais_hu_3.png')
corrgram(Hu, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors4)
dev.off()


png(height=1200, width=1200, pointsize=25, file='populacionais_geom_3.png')
corrgram(geo, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors4)
dev.off()

#Matrizes de correlação
M = cor(Y, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_RTSC_3.png")
corrplot(M, method = 'circle',
         col=colors4,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

M = cor(Hu, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_hu_3.png")
corrplot(M, method = 'circle',
         col=colors4,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

M = cor(geo, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_geo_3.png")
corrplot(M, method = 'circle',
         col=colors4,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

M = cor(all, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_all_3.png")
cex.before <- par("cex")
par(cex = 0.7)
corrplot(M, method = 'circle',
         col=colors4,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()


#GRUPO 2
#Sa/Sab, Sb, Sbc

#Selecao das subamostras
Y = datas2[,c(3,7,10,24,25)]
Hu = datas2[,11:17]
geo = datas2[,c(3,18,19,20,21,22,23,24,25)]
all=datas2[,-c(1,2,4,6,8)]

#Correlogramas 
png(height=1200, width=1200, pointsize=25, file='populacionais_all_2.png')
corrgram(data, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors3)
dev.off()


png(height=1200, width=1200, pointsize=25, file='populacionais_RTSC_2.png')
corrgram(Y, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors3)
dev.off()


png(height=1200, width=1200, pointsize=25, file='populacionais_hu_2.png')
corrgram(Hu, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors3)
dev.off()


png(height=1200, width=1200, pointsize=25, file='populacionais_geom_2.png')
corrgram(geo, order = TRUE,
         lower.panel = panel.ellipse, 
         upper.panel = panel.pts, 
         text.panel = panel.txt,
         diag.panel = panel.minmax,
         main="Algumas Correlações",
         col = colors3)
dev.off()

#Matrizes de correlação
M = cor(Y, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_RTSC_2.png")
corrplot(M, method = 'circle',
         col=colors3,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

M = cor(Hu, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_hu_2.png")
corrplot(M, method = 'circle',
         col=colors3,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

M = cor(geo, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_geo_2.png")
corrplot(M, method = 'circle',
         col=colors3,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()

M = cor(all, method = 'spearman')
png(height=1200, width=1200, pointsize=25, file="corr_map_all_2.png")
cex.before <- par("cex")
par(cex = 0.7)
corrplot(M, method = 'circle',
         col=colors3,
         is.corr=TRUE,
         cl.cex = 1/par("cex"),
         addCoef.col = rgb(0,0,0, alpha = 0.7),
         type = 'lower',
         tl.col='black',
         tl.cex = 1/par("cex"))
dev.off()


