df <- read.csv(file_name,header = TRUE, fileEncoding="UTF-8",na.strings=c("", "NA","--undefined--"))


#df = df[df$wordlabel != 'sp']
# df$verb = as.factor(df$verb)


# df_Agent = df[(df$condition=='Agent' | df$condition=='Verb') & df$word_num=='3',]
# 
# df_Verb = df[(df$condition=='Verb'| df$condition=='Patient') & df$word_num=='5',]
# 
# df_Patient = df[(df$condition=='Patient'| df$condition=='Agent') & df$word_num=='6',]

df_Agent = df[(df$condition=='Agent' | df$condition=='YesControl') & df$word_num=='3',]
# df_Agent inheri row hum from df

df_Verb = df[(df$condition=='Verb'| df$condition=='YesControl') & df$word_num=='5',]

df_Patient = df[(df$condition=='Patient'| df$condition=='YesControl') & df$word_num=='6',]

print(sum(is.na(df_Agent)))

# relevant_columns = c('participant','verb','condition','duration','meanIntensity','meanpit')
# df_Agent = df_Agent[relevant_columns]
# df_Verb = df_Verb[relevant_columns]
# df_Patient = df_Patient[relevant_columns]
sum(is.na(df[new.df$word != 'sp',]))
# new.df[(new.df$meanpit == '--undefined--') && (new.df$word != 'sp'),]
# it seems that the only undefined is meanpitch for sp

# df_Agent = df_Agent[df_Agent$duration!='--undefined--' & df_Agent$meanIntensity!='--undefined--' &  df_Agent	$meanpit!='--undefined--' ,]
# df_Agent = transform(df_Agent,duration=as.numeric(duration))
# df_Agent = transform(df_Agent, meanIntensity = as.numeric(meanIntensity))
# df_Agent = transform(df_Agent, meanpit = as.numeric(meanpit))
# 
# df_Patient = df_Patient[df_Patient$duration!='--undefined--' & df_Patient$meanIntensity!='--undefined--' &  df_Patient$meanpit!='--undefined--' ,]
# df_Patient = transform(df_Patient,duration=as.numeric(duration))
# df_Patient = transform(df_Patient, meanIntensity = as.numeric(meanIntensity))
# df_Patient = transform(df_Patient, meanpit = as.numeric(meanpit))
# 
# df_Verb = df_Verb[df_Verb$duration!='--undefined--' & df_Verb$meanIntensity!='--undefined--' &  df_Verb$meanpit!='--undefined--' ,]
# df_Verb = transform(df_Verb,duration=as.numeric(duration))
# df_Verb = transform(df_Verb, meanIntensity = as.numeric(meanIntensity))
# df_Verb = transform(df_Verb, meanpit = as.numeric(meanpit))

df_Verb = normalize_data(df_Verb, TRUE)
df_Agent = normalize_data(df_Agent, TRUE)
df_Patient = normalize_data(df_Patient, TRUE)
print(sum(is.na(df_Agent)))