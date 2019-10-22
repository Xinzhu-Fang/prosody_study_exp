def create_stimuli(iExp, exp_name, exp_num_of_items, exp_yes_to_no_ratio, exp_num_trials, exp_num_trial_yes, exp_num_trial_no, exp_num_of_control_for_each_item, exp_num_of_correction_for_each_position_for_each_item, item_num_trial_total, item_num_trial_yes, item_num_trial_no, item_num_trial_for_each_item, filler_num_trial_total, filler_num_trial_yes, filler_num_trial_no)
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw
    import glob


    #female_names = ["ANNIE", "BETTY", "BONNIE", "BRANDY", "CARLIE", "CHLOE", "DOLLY",
    #"DORRY", "DORY", "FANNY", "FRANNY", "JENNY", "JUDY", "KELLY",
    #"KIMMY", "LACEY", "LARRY", "LAURIE", "LINDY", "MANDY", "MARY",
    #"MERRY", "MINDY", "MOLLY", "PAMMY", "PENNY", "RUDY", "SANDY",
    #"TORI"]
    #male_names = ["ANDY", "BILLY", "CODY", "COREY", "DANNY", "DONNY", "EDDIE",
    #"FREEDY", "GARRY", "HARVEY", "JERRY", "JOHNNY", "KENNY", "LONNIE",
    #"OLLIE", "PERCY", "RONNIE", "TAMMY", "TEDDY", "TIMMY", "WALLY",
    #"WILLY"]
    #
    sex_levels = ['F', 'M']
    num_sexes = len(sex_levels)
    names = {'F': ["ANNIE", "BETTY", "BONNIE", "BRANDY", "CARLIE", "CHLOE", "DOLLY",
    "DORRY", "DORY", "FANNY", "FRANNY", "JENNY", "JUDY", "KELLY",
    "KIMMY", "LACEY", "LARRY", "LAURIE", "LINDY", "MANDY", "MARY",
    "MERRY", "MINDY", "MOLLY", "PAMMY", "PENNY", "RUDY", "SANDY",
    "SANNDY", "TORI"],
    'M': ["ANDY", "BILLY", "CODY", "COREY", "DANNY", "DONNY", "EDDIE",
    "FREEDY", "GARRY", "HARVEY", "JERRY", "JOHNNY", "KENNY", "LONNIE",
    "OLLIE", "PERCY", "RONNIE", "TAMMY", "TEDDY", "TIMMY", "WALLY",
    "WILLY"]}



    f_f_verbs = ["Lift", "Poke", "Pull", "Push"]
    f_m_verbs = ["Kick", "Kiss", "Lift", "Poke", "Push"]
    m_f_verbs = ["Kick", "Kiss", "Lift", "Pull", "Push", "Poke"]
    m_m_verbs = ["Lift", "Poke", "Pull"]
    verbs = ["Kiss", "Kick", "Poke", "Lift", "Push", "Pull"]
    agent_sex_mapped_to_verb = ['F', 'F', 'F', 'M', 'M', 'F']
    patient_sex_mapped_to_verb = ['M', 'M', 'F', 'M', 'F', 'F']
    num_verbs = len(verbs)


    item_correct_verb = np.tile(np.array(["Kick", "Kiss", "Push", "Pull"]), (3,1))][iExp]



    # item
    item_correct_agent_sex = [agent_sex_mapped_to_verb[verbs.index(i)] for i in item_correct_verb]
    item_correct_patient_sex = [patient_sex_mapped_to_verb[verbs.index(i)] for i in item_correct_verb]


    #item_wrong_verb = [verbs[num_verbs - 1 - verbs.index(i)] for i in item_correct_verb]
    item_wrong_verb = [verbs[(verbs.index(i) + np.random.randint(1, num_verbs)) % num_verbs] for i in item_correct_verb]
    ##

    item_correct_agent = [names[i].pop() for i in item_correct_agent_sex]
    item_correct_patient = [names[i].pop() for i in item_correct_patient_sex]


    #item_wrong_agent_oppo_sex =  [names[ sex_levels[num_sexes - 1 - sex_levels.index(i)]].pop() for i in item_correct_agent_sex]
    #item_wrong_agent_same_sex =  [names[i].pop() for i in item_correct_agent_sex]
    #item_wrong_agent = [names[i].pop() for i in item_correct_agent_sex]
    # ^ too wasteful, these can be repeated
    item_wrong_agent = [names[i][np.random.randint(len(names[i]))] for i in item_correct_agent_sex]
    #item_wrong_patient_oppo_sex =  [names[ sex_levels[num_sexes - 1 - sex_levels.index(i)]].pop() for i in item_correct_patient_sex]
    #item_wrong_patient_same_sex =  [names[i].pop() for i in item_correct_patient_sex]
    #item_wrong_patient = [names[i].pop() for i in item_correct_patient_sex]
    item_wrong_patient = [names[i][np.random.randint(len(names[i]))] for i in item_correct_patient_sex]


    filler_position_condition_for_no = [positions[i] for i in np.random.randint(num_positions, size = filler_num_trial_no)]
    vFiller_position_condition = np.concatenate((filler_position_condition_for_no, np.tile(['Control'], filler_num_trial_yes)))

    filler_correct_verb = [verbs[np.random.randint(0, num_verbs)] for i in range(filler_num_trial_total)]
    #filler_wrong_verb = [verbs[num_verbs - 1 - verbs.index(i)] for i in filler_correct_verb]
    filler_wrong_verb = [verbs[(verbs.index(i) + np.random.randint(1, num_verbs)) % num_verbs] for i in filler_correct_verb]
    #to check should be all false
    #[filler_correct_verb[i] == filler_wrong_verb[i] for i in range(len(filler_correct_verb))]

    filler_correct_agent_sex = [agent_sex_mapped_to_verb[verbs.index(i)] for i in filler_correct_verb]
    filler_correct_patient_sex = [patient_sex_mapped_to_verb[verbs.index(i)] for i in filler_correct_verb]


    ## start of filler agent
    filler_correct_agent = [names[i][np.random.randint(len(names[i]))] for i in filler_correct_agent_sex]

    filler_wrong_agent = []
    for i in range(len(filler_correct_agent)):
        cur_sex = filler_correct_agent_sex[i]
        cur_name_pool = names[cur_sex]
        cur_correct_name_index = cur_name_pool.index(filler_correct_agent[i])
        cur_wrong_name_index = (cur_correct_name_index + np.random.randint(1, len(cur_name_pool))) % len(cur_name_pool)
        cur_wrong_name = cur_name_pool[cur_wrong_name_index]
        filler_wrong_agent.append(cur_wrong_name)

    filler_agent_in_picture = filler_correct_agent[:]

    filler_agent_in_question = filler_agent_in_picture[:]

    tFiller_agent = pd.DataFrame(zip(filler_id, vFiller_position_condition, filler_agent_in_picture, filler_agent_in_question), columns = ['filler_id', 'vFiller_position_condition', 'filler_agent_in_picture', 'filler_agent_in_question'])
    for iFiller in filler_id:
        tFiller_agent.loc[np.logical_and(tFiller_agent.vFiller_position_condition == 'Agent', tFiller_agent.filler_id == iFiller), 'filler_agent_in_question'] = filler_wrong_agent[filler_id.index(iFiller)]
    # end of filler agent

    ## start of filler patient
    filler_correct_patient = [names[i][np.random.randint(len(names[i]))] for i in filler_correct_patient_sex]

    filler_wrong_patient = []
    for i in range(len(filler_correct_patient)):
        cur_sex = filler_correct_patient_sex[i]
        cur_name_pool = names[cur_sex]
        cur_correct_name_index = cur_name_pool.index(filler_correct_patient[i])
        cur_wrong_name_index = (cur_correct_name_index + np.random.randint(1, len(cur_name_pool))) % len(cur_name_pool)
        cur_wrong_name = cur_name_pool[cur_wrong_name_index]
        filler_wrong_patient.append(cur_wrong_name)

    filler_patient_in_picture = filler_correct_patient[:]

    filler_patient_in_question = filler_patient_in_picture[:]

    tFiller_patient = pd.DataFrame(list(zip(filler_id, vFiller_position_condition, filler_patient_in_picture, filler_patient_in_question)), columns = ['filler_id', 'vFiller_position_condition', 'filler_patient_in_picture', 'filler_patient_in_question'])
    for iFiller in filler_id:
        tFiller_patient.loc[np.logical_and(tFiller_patient.vFiller_position_condition == 'Patient', tFiller_patient.filler_id == iFiller), 'filler_patient_in_question'] = filler_wrong_patient[filler_id.index(iFiller)]
    # end of filler patient

    ## start of filler verb
    filler_verb_in_picture = filler_correct_verb[:]

    filler_verb_in_question = filler_verb_in_picture[:]

    tFiller_verb = pd.DataFrame(list(zip(filler_id, vFiller_position_condition, filler_verb_in_picture, filler_verb_in_question)), columns = ['filler_id', 'vFiller_position_condition', 'filler_verb_in_picture', 'filler_verb_in_question'])
    for iFiller in filler_id:
        tFiller_verb.loc[np.logical_and(tFiller_verb.vFiller_position_condition == 'Verb', tFiller_verb.filler_id == iFiller), 'filler_verb_in_question'] = filler_wrong_verb[filler_id.index(iFiller)]
    # end of filler verb

    item_id0 = ["{:02d}".format(i) for i in range(1, exp_num_of_items + 1)]
    item_id = ["item_" + i for i in item_id0]
    vItem_id = np.repeat(item_id, item_num_trial_for_each_item)

    vItem_position_condition = np.tile(np.concatenate((np.tile(positions, exp_num_of_correction_for_each_position_for_each_item),
                                   np.tile(['Control'], exp_exp_num_of_control_for_each_item))), exp_num_of_items)

    ## start of item agent
    vItem_agent_in_picture = np.repeat(item_correct_agent, item_num_trial_for_each_item)

    vItem_agent_in_question = np.copy(vItem_agent_in_picture)


    tItem_agent = pd.DataFrame(list(zip(vItem_id, vItem_position_condition, vItem_agent_in_picture, vItem_agent_in_question)),
                     columns=['vItem_id', 'vItem_position_condition', 'vItem_agent_in_picture', 'vItem_agent_in_question'])

    for iItem in item_id:
        tItem_agent.loc[np.logical_and(tItem_agent.vItem_position_condition == 'Agent', tItem_agent.vItem_id == iItem), 'vItem_agent_in_question'] =  item_wrong_agent[item_id.index(iItem)]
    ## end of item agent

    ## start of item patient
    vItem_patient_in_picture = np.repeat(item_correct_patient, item_num_trial_for_each_item)

    vItem_patient_in_question = np.copy(vItem_patient_in_picture)


    tItem_patient = pd.DataFrame(list(zip(vItem_id, vItem_position_condition, vItem_patient_in_picture, vItem_patient_in_question)),
                     columns=['vItem_id', 'vItem_position_condition', 'vItem_patient_in_picture', 'vItem_patient_in_question'])

    for iItem in item_id:
        tItem_patient.loc[np.logical_and(tItem_patient.vItem_position_condition == 'Patient', tItem_patient.vItem_id == iItem), 'vItem_patient_in_question'] =  item_wrong_patient[item_id.index(iItem)]
    ## end of item patient

    ## start of verb
    vItem_verb_in_picture = np.repeat(item_correct_verb, item_num_trial_for_each_item)

    vItem_verb_in_question = np.copy(vItem_verb_in_picture)


    tItem_verb = pd.DataFrame(list(zip(vItem_id, vItem_position_condition, vItem_verb_in_picture, vItem_verb_in_question)),
                     columns=['vItem_id', 'vItem_position_condition', 'vItem_verb_in_picture', 'vItem_verb_in_question'])

    for iItem in item_id:
        tItem_verb.loc[np.logical_and(tItem_verb.vItem_position_condition == 'Verb', tItem_verb.vItem_id == iItem), 'vItem_verb_in_question'] =  item_wrong_verb[item_id.index(iItem)]
    ## end of verb

    tItem = pd.concat([tItem_agent, tItem_verb, tItem_patient], axis=1)
    tItem = tItem.loc[:, ~tItem.columns.duplicated()]
    tItem.columns = ["filler_or_item_id", "position_condition", "agent_in_picture", "agent_in_question", "verb_in_picture", "verb_in_question", "patient_in_picture", "patient_in_question"]

    tFiller = pd.concat([tFiller_agent, tFiller_verb, tFiller_patient], axis=1)
    tFiller = tFiller.loc[:, ~tFiller.columns.duplicated()]
    tFiller.columns = ["filler_or_item_id", "position_condition", "agent_in_picture", "agent_in_question", "verb_in_picture", "verb_in_question", "patient_in_picture", "patient_in_question"]

    tAll_trials = pd.concat([tItem, tFiller])


    tAll_trials['question_file'] = ["Is_" + a + '_'+ v + "ing" + '_' + p + '.wav' for a, v, p in zip(tAll_trials.agent_in_question, tAll_trials.verb_in_question, tAll_trials.patient_in_question)]
    tAll_trials['picture_file'] = [a + '_is_' + v + "ing" + '_' + p + '.png' for a, v, p in zip(tAll_trials.agent_in_picture, tAll_trials.verb_in_picture, tAll_trials.patient_in_picture)]

    tAll_trials.to_csv('tAll_trials.csv', encoding='utf-8', index=False)
    exp_trial_id = ["{:02d}".format(i) for i in range(1, exp_num_trials + 1)]



    # image = "sample-out.png"
    # img = Image.open(image)
    # draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    # font = ImageFont.truetype("sans-serif.ttf", 16)
    font0 = ImageFont.truetype("/Library/Fonts/Arial.ttf", 80)
    width1 = 50
    width2 = 900
    height = 1900
    color0 = (0,0,0,0)

    # img.save('sample-out.png')
    vanilla_dir = 'vanilla_images'
    output_dir = 'stimuli/images'
    for iTrial, iRow in tAll_trials.iterrows():
        cur_vanilla = glob.glob(vanilla_dir + '/' + '*' + iRow.verb_in_picture + '*.png')[0]
        print(iTrial)
        print(cur_vanilla)
    #    cur_img = Image.open(cur_vanilla)
    #    draw = ImageDraw.Draw(cur_img)
    #    draw.text((width1, height), iRow.agent_in_picture, color0,font=font0)
    #    draw.text((width2, height), iRow.patient_in_picture, color0, font=font0)
    #    cur_img.save(output_dir + '/' +  iRow.picture_file)
