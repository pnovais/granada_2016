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

M = cor(Y, method = 'spearman')
hist(M, main="R, t, M, Sym, Conc", breaks = 10 , xlab = "Freq. de correlacoes - Spearman", xaxt='n')
axis(side=1, at=seq(-1,1, 0.2))
#hist(M, main="R, t, M, Sym, Conc")

M = cor(Hu, method = 'spearman')
hist(M, main="Hu moments", breaks = 10 , xlab = "Freq. de correlacoes - Spearman", xaxt='n')
axis(side=1, at=seq(-1,1, 0.2))

M = cor(geo, method = 'spearman')
hist(M, main="Hu moments", breaks = 10 , xlab = "Freq. de correlacoes - Spearman", xaxt='n')
axis(side=1, at=seq(-1,1, 0.2))

M = cor(all, method = 'spearman')
hist(M, main="Todos os parametros", breaks = 10, xlab = "Freq. de correlacoes - Spearman", xaxt='n')
axis(side=1, at=seq(-1,1, 0.2))
