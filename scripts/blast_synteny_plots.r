#Plots all blast data and uses %ID coloumn to build a color gradient.
ggplot(df, aes(x=query_id, y=subject_id, color = pct_identity)) + 
  geom_point() + 
  scale_color_gradient(low="blue", high = "red") + 
  ylab("pMPPla107") + xlab("pBASL58") + 
  labs(color="Percent ID") + 
  theme(axis.line = element_line(size = 1, colour = "black"), panel.background = element_rect(fill = "white"))

#Plots a generic scatter plot for the 40, 50, 60, 70% filtered BALST data.
ggplot(df2, aes(x=QueryID, y=Subject.ID)) + 
  geom_point(shape = 1) + 
  ylab("pMPPla107") + xlab("pBASL58") +
  theme(axis.line = element_line(size = 1, colour = "black"), panel.background = element_rect(fill = "white")) 