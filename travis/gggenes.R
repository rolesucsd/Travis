library(tidyverse)
library(data.table)
library(dplyr)
library(gggenes)

# Load input
args <- commandArgs(trailingOnly = TRUE)
path_file <- read.delim(args[1])
path_anno <- read.delim(args[2], check.names = F)
output <- args[3]

# Add annotation information
path <- left_join(path_file, path_anno[,c("Gene","Length","Label")])

# Add xmin and xmax for each gene 
path <- path %>%
  arrange(Path, Position) %>%
  group_by(Path) %>%
  mutate(
    xmin = cumsum(lag(Length, default = 0)) + 1,
    xmax = cumsum(Length)
  )

ps_path$Path <- gsub("path","",ps_path$Path)
ps_path$Path <- as.numeric(ps_path$Path)

Label <- unique(path_anno$Label)
# Generate the rainbow colors
Color <- rainbow(length(Label))
# Randomly sample from the rainbow colors without replacement
Color <- sample(Color, length(Label), replace = FALSE)
names(Color) <- Label

# Plot the operons 
ggplot(path, aes(xmin=xmin, xmax=xmax, y=as.character(Path), fill=Label))+
  geom_gene_arrow(arrowhead_height = unit(3, "mm"), arrowhead_width = unit(1, "mm"))+
  geom_gene_label(align = "left")+
  facet_wrap(~Path, scales="free_y", ncol=1)+
  theme_minimal() +
  theme(strip.text = element_blank())+
  scale_fill_manual(values=Color)
ggsave(paste(output,"/path_plot.png",sep=""), dpi=300, units="in", height=5, width=15)