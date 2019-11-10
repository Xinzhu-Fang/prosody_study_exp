library("dplyr")
setwd("/Users/michelleoraaali/Desktop")
gdata = read.csv("somerename.csv", header  = T)
# gdata = transform(gdata,PresentationNum=as.numeric(PresentationNum))
# sort(gdata$PresentationNum, decreasing = FALSE)
colnames(gdata)

# code for word_num
# new.df <- gdata %>% 
#   group_by(participant, question, PresentationNum) %>% 
#   mutate(wordnum=1:n())

# code for getting Nth instance of question
nthdf <- gdata %>%
  group_by(participant, question, condition, item) %>%
  mutate(Appearance=1:n())
write.csv(nthdf,'nthdf.csv')