#!/usr/bin/env Rscript

library('ggplot2')

m <- read.table('benchmark_25_10_snaptron_only.tsv', header=T, sep='\t')
m$TabixC <- grepl('Tabix-Compressed', m$Query.Type)
m$TabixU <- grepl('Tabix-Uncompressed', m$Query.Type)
m$Constrained <- factor(grepl('Constraint', m$Query.Type), labels=c('R query', 'R+F query'))
m$NoIndex <- grepl('NoIndex', m$Query.Type)
#m$Type <- ifelse(m$TabixC, 'Tabix, R-tree, compressed', ifelse(m$TabixU, 'Tabix, R-tree, uncompressed', ifelse(m$NoIndex, 'SQLite, no index, uncompressed', 'SQLite, B-tree, uncompressed')))
m$Type <- ifelse(m$TabixC, 'Tabix, R-tree, compressed', ifelse(m$TabixU, 'Tabix, R-tree', ifelse(m$NoIndex, 'SQLite, no index', 'SQLite, B-tree')))

pdf(file="benchmark_fig.pdf", height=4, width=5.5)
ggplot(m, aes(x=Query.Size, y=Query.Time, color=Type, linetype=Constrained)) + labs(x='Query size (100KB)', y='Time (seconds)') + geom_line() + geom_point() + theme_bw() + theme(legend.title=element_blank()) + scale_y_continuous(limits=c(0, 17))
dev.off()
