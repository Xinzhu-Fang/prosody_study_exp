def create_stimuli(bCreate_stimuli, iExp, positions, num_positions, exp_name, exp_num_of_items, exp_yes_to_no_ratio,
                   exp_num_trials,
                   exp_num_trial_yes, exp_num_trial_no, exp_num_of_control_for_each_item,
                   exp_num_of_correction_for_each_position_for_each_item, item_num_trial_total, item_num_trial_yes,
                   item_num_trial_no, item_num_trial_for_each_item, filler_num_trial_total, filler_num_trial_yes,
                   filler_num_trial_no, my_seed):
    import numpy as np
    import pandas as pd
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw
    import glob
    import os
    import shutil

    np.random.seed(my_seed[0])
    vanilla_dir = 'vanilla_images0'
    output_dir = os.path.join(exp_name, 'images')
    if not os.path.isdir(exp_name):
        # print("I")
        os.mkdir(exp_name)
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
        # print("cannot")
    # else:
    os.mkdir(output_dir)
    # print("believe")

    # female_names = ["ANNIE", "BETTY", "BONNIE", "BRANDY", "CARLIE", "CHLOE", "DOLLY",
    # "DORRY", "DORY", FRANNY", "JENNY", "JUDY", "KELLY",
    # "KIMMY", "LACEY", "LARRY", "LAURIE", "LINDY", "MANDY", "MARY",
    # "MERRY", "MINDY", "MOLLY", "PAMMY", "PENNY", "RUDY", "SANDY",
    # "TORI"]
    # male_names = ["ANDY", "BILLY", "CODY", "COREY", "DANNY", "DONNY", "EDDIE",
    # "Freddy", "GARY", "HARVEY", "JERRY", "JOHNNY", "KENNY", "LONNIE",
    # "OLLIE", "PERCY", "RONNIE", "TAMMY", "TEDDY", "TIMMY", "WALLY",
    # "WILLY"]
    #
    # other names, cindy, nancy, zoey, morrie, joey, willy, randy, tracey, casey, terry, kerry, kylie, darcy, neddy, mory, benny, manny, jilly, nelly, carrie, hailey, sammy
    # names i threw out myself, fanny, SANDY, dorry

    # lily,

    sex_levels = ['F', 'M']
    num_sexes = len(sex_levels)
    names = {'F': ["Nancy", "Vicky", "Tori", "Penny", "Jilly", "Cindy", "Laurie", 
"Franny", "Brandy", "Betty", "Kylie", "Carrie", "Tracy", "Chloe", 
"Annie", "Mindy", "Molly", "Sally", "Lacey", "Carlie", "Mandy", 
"Hailey", "Lilly", "Jenny", "Judy", "Kerry", "Kelly", "Bonnie", 
"Kimmy"],
             'M': ["Freddy", "Ronnie", "Davey", "Jimmy", "Kenny", "Percy", "Sammy", 
"Harvey", "Gary", "Ollie", "Danny", "Henry", "Teddy", "Wally", 
"Johnny", "Jerry", "Timmy", "Benny", "Tommy", "Joey"
                   ]}
    #    a small pool to test the latter any trial with characters of the same name? test
    #    names = {'F': ["Annie", "Betty", "Bonnie", "Brandy", "Carlie", "Chloe", "Dolly", "Dory", "Franny", "Jenny", "Judy",
    #                   "Kelly"],
    #             'M': ["Andy", "Billy", "Cody", "Corey", "Danny", "Donny", "Eddie",
    #                   "Freddy", "GARY", "Harvey"]}
    #    ted thinks ambiguous or bad sandy, andy, dory, larry, rudy, tammy, willy, dolly, lindy, pammy, lonnie, morrie, randy, casey, terry, mary, merry

    f_f_verbs = ["Lift", "Poke", "Pull", "Push"]
    f_m_verbs = ["Kick", "Kiss", "Lift", "Poke", "Push"]
    m_f_verbs = ["Kick", "Kiss", "Lift", "Pull", "Push", "Poke"]
    m_m_verbs = ["Lift", "Poke", "Pull"]
    verbs = ["Kiss", "Kick", "Poke", "Lift", "Push", "Pull"]
    agent_sex_mapped_to_verb = ['F', 'F', 'F', 'M', 'M', 'F']
    patient_sex_mapped_to_verb = ['M', 'M', 'F', 'M', 'F', 'F']
    num_verbs = len(verbs)

    item_correct_verb = np.tile(np.array(["Kick", "Kiss", "Push", "Pull"]), (3, 1))[iExp]

    # item
    item_correct_agent_sex = [agent_sex_mapped_to_verb[verbs.index(i)] for i in item_correct_verb]
    item_correct_patient_sex = [patient_sex_mapped_to_verb[verbs.index(i)] for i in item_correct_verb]

    item_correct_agent = [names[i].pop() for i in item_correct_agent_sex]
    item_correct_patient = [names[i].pop() for i in item_correct_patient_sex]

    vItem_correct_verb = np.repeat(item_correct_verb, item_num_trial_for_each_item)

    vItem_correct_agent = np.repeat(item_correct_agent, item_num_trial_for_each_item)

    vItem_correct_patient = np.repeat(item_correct_patient, item_num_trial_for_each_item)

    vItem_correct_agent_sex = np.repeat(item_correct_agent_sex, item_num_trial_for_each_item)

    vItem_correct_patient_sex = np.repeat(item_correct_patient_sex, item_num_trial_for_each_item)

    # item_wrong_verb = [verbs[num_verbs - 1 - verbs.index(i)] for i in item_correct_verb]
    item_wrong_verb = [verbs[(verbs.index(i) + np.random.randint(1, num_verbs)) % num_verbs] for i in
                       vItem_correct_verb]
    ##

    # item_wrong_agent_oppo_sex =  [names[ sex_levels[num_sexes - 1 - sex_levels.index(i)]].pop() for i in item_correct_agent_sex]
    # item_wrong_agent_same_sex =  [names[i].pop() for i in item_correct_agent_sex]
    # item_wrong_agent = [names[i].pop() for i in item_correct_agent_sex]
    # ^ too wasteful, these can be repeated
    item_wrong_agent = [names[i][np.random.randint(len(names[i]))] for i in vItem_correct_agent_sex]
    # item_wrong_patient_oppo_sex =  [names[ sex_levels[num_sexes - 1 - sex_levels.index(i)]].pop() for i in item_correct_patient_sex]
    # item_wrong_patient_same_sex =  [names[i].pop() for i in item_correct_patient_sex]
    # item_wrong_patient = [names[i].pop() for i in item_correct_patient_sex]
    item_wrong_patient = [names[i][np.random.randint(len(names[i]))] for i in vItem_correct_patient_sex]

    item_id0 = ["{:02d}".format(i) for i in range(1, exp_num_of_items + 1)]
    item_id = ["item_" + i for i in item_id0]
    vItem_id = np.repeat(item_id, item_num_trial_for_each_item)

    vItem_position_condition = np.tile(
        np.concatenate((np.repeat(positions, exp_num_of_correction_for_each_position_for_each_item),
                        np.repeat(['Control'], exp_num_of_control_for_each_item))), exp_num_of_items)

    ## start of item agent
    # vItem_agent_in_picture = np.repeat(item_correct_agent, item_num_trial_for_each_item)

    # vItem_agent_in_question = np.copy(vItem_agent_in_picture)

    tItem_agent = pd.DataFrame(
        list(zip(vItem_id, vItem_position_condition, vItem_correct_agent, vItem_correct_agent)),
        columns=['vItem_id', 'vItem_position_condition', 'vItem_agent_in_picture', 'vItem_agent_in_question'])

    for iTrial, iRow in tItem_agent.iterrows():
        if iRow.vItem_position_condition == 'Agent':
            tItem_agent.loc[iTrial, 'vItem_agent_in_question'] = item_wrong_agent[iTrial]
    # for iItem in item_id:
    #     tItem_agent.loc[np.logical_and(tItem_agent.vItem_position_condition == 'Agent',
    #                                    tItem_agent.vItem_id == iItem), 'vItem_agent_in_question'] = item_wrong_agent[
    #         item_id.index(iItem)]
    # print(tItem_agent)
    ## end of item agent

    ## start of item patient
    # vItem_patient_in_picture = np.repeat(item_correct_patient, item_num_trial_for_each_item)

    # vItem_patient_in_question = np.copy(vItem_patient_in_picture)

    tItem_patient = pd.DataFrame(
        list(zip(vItem_id, vItem_position_condition, vItem_correct_patient, vItem_correct_patient)),
        columns=['vItem_id', 'vItem_position_condition', 'vItem_patient_in_picture', 'vItem_patient_in_question'])

    for iTrial, iRow in tItem_patient.iterrows():
        if iRow.vItem_position_condition == 'Patient':
            tItem_patient.loc[iTrial, 'vItem_patient_in_question'] = item_wrong_patient[iTrial]
    # for iItem in item_id:
    #     tItem_patient.loc[np.logical_and(tItem_patient.vItem_position_condition == 'Patient',
    #                                    tItem_patient.vItem_id == iItem), 'vItem_patient_in_question'] = item_wrong_patient[
    #         item_id.index(iItem)]
    # print(tItem_patient)
    ## end of item patient

    ## start of item verb
    # vItem_verb_in_picture = np.repeat(item_correct_verb, item_num_trial_for_each_item)

    # vItem_verb_in_question = np.copy(vItem_verb_in_picture)

    tItem_verb = pd.DataFrame(
        list(zip(vItem_id, vItem_position_condition, vItem_correct_verb, vItem_correct_verb)),
        columns=['vItem_id', 'vItem_position_condition', 'vItem_verb_in_picture', 'vItem_verb_in_question'])

    for iTrial, iRow in tItem_verb.iterrows():
        if iRow.vItem_position_condition == 'Verb':
            tItem_verb.loc[iTrial, 'vItem_verb_in_question'] = item_wrong_verb[iTrial]
    # for iItem in item_id:
    #     tItem_verb.loc[np.logical_and(tItem_verb.vItem_position_condition == 'Verb',
    #                                    tItem_verb.vItem_id == iItem), 'vItem_verb_in_question'] = item_wrong_verb[
    #         item_id.index(iItem)]
    # print(tItem_verb)
    ## end of item verb

    tItem = pd.concat([tItem_agent, tItem_verb, tItem_patient], axis=1)
    tItem = tItem.loc[:, ~tItem.columns.duplicated()]
    tItem.columns = ["filler_or_item_id", "position_condition", "agent_in_picture", "agent_in_question",
                     "verb_in_picture", "verb_in_question", "patient_in_picture", "patient_in_question"]

    filler_id0 = ["{:02d}".format(i) for i in range(1, filler_num_trial_total + 1)]
    filler_id = ["filler_" + i for i in filler_id0]
    filler_position_condition_for_no = [positions[i] for i in
                                        np.random.randint(num_positions, size=filler_num_trial_no)]
    vFiller_position_condition = np.concatenate(
        (filler_position_condition_for_no, np.tile(['Control'], filler_num_trial_yes)))

    np.random.seed(my_seed[1])
    filler_wrong_verb = [verbs[np.random.randint(0, num_verbs)] for i in range(filler_num_trial_total)]
    # filler_correct_verb = [verbs[num_verbs - 1 - verbs.index(i)] for i in filler_wrong_verb]
    filler_correct_verb = [verbs[(verbs.index(i) + np.random.randint(1, num_verbs)) % num_verbs] for i in
                           filler_wrong_verb]
    # to check should be all false
    # [filler_wrong_verb[i] == filler_correct_verb[i] for i in range(len(filler_wrong_verb))]

    filler_wrong_agent_sex = [agent_sex_mapped_to_verb[verbs.index(i)] for i in filler_wrong_verb]
    filler_wrong_patient_sex = [patient_sex_mapped_to_verb[verbs.index(i)] for i in filler_wrong_verb]

    ## start of filler agent
    np.random.seed(my_seed[2])
    filler_wrong_agent = [names[i][np.random.randint(len(names[i]))] for i in filler_wrong_agent_sex]

    filler_correct_agent = []
    for i in range(len(filler_wrong_agent)):
        cur_sex = filler_wrong_agent_sex[i]
        cur_name_pool = names[cur_sex]
        cur_wrong_name_index = cur_name_pool.index(filler_wrong_agent[i])
        cur_correct_name_index = (cur_wrong_name_index + np.random.randint(1, len(cur_name_pool))) % len(cur_name_pool)
        cur_correct_name = cur_name_pool[cur_correct_name_index]
        filler_correct_agent.append(cur_correct_name)

    # filler_agent_in_question = filler_wrong_agent[:]

    # filler_agent_in_picture = filler_agent_in_question[:]

    tFiller_agent = pd.DataFrame(
        zip(filler_id, vFiller_position_condition, filler_wrong_agent, filler_wrong_agent),
        columns=['filler_id', 'vFiller_position_condition', 'filler_agent_in_question', 'filler_agent_in_picture'])
    for iFiller in filler_id:
        tFiller_agent.loc[np.logical_and(tFiller_agent.vFiller_position_condition == 'Agent',
                                         tFiller_agent.filler_id == iFiller), 'filler_agent_in_picture'] = \
            filler_correct_agent[filler_id.index(iFiller)]
    # end of filler agent

    ## start of filler patient
    np.random.seed(my_seed[3])
    filler_wrong_patient = [names[i][np.random.randint(len(names[i]))] for i in filler_wrong_patient_sex]

    filler_correct_patient = []
    for i in range(len(filler_wrong_patient)):
        cur_sex = filler_wrong_patient_sex[i]
        cur_name_pool = names[cur_sex]
        cur_wrong_name_index = cur_name_pool.index(filler_wrong_patient[i])
        cur_correct_name_index = (cur_wrong_name_index + np.random.randint(1, len(cur_name_pool))) % len(cur_name_pool)
        cur_correct_name = cur_name_pool[cur_correct_name_index]
        filler_correct_patient.append(cur_correct_name)

    # filler_patient_in_question = filler_wrong_patient[:]

    # filler_patient_in_picture = filler_patient_in_question[:]

    tFiller_patient = pd.DataFrame(
        list(zip(filler_id, vFiller_position_condition, filler_wrong_patient, filler_wrong_patient)),
        columns=['filler_id', 'vFiller_position_condition', 'filler_patient_in_question', 'filler_patient_in_picture'])
    for iFiller in filler_id:
        tFiller_patient.loc[np.logical_and(tFiller_patient.vFiller_position_condition == 'Patient',
                                           tFiller_patient.filler_id == iFiller), 'filler_patient_in_picture'] = \
            filler_correct_patient[filler_id.index(iFiller)]
    # end of filler patient

    ## start of filler verb
    # filler_verb_in_question = filler_wrong_verb[:]

    # filler_verb_in_picture = filler_verb_in_question[:]

    tFiller_verb = pd.DataFrame(
        list(zip(filler_id, vFiller_position_condition, filler_wrong_verb, filler_wrong_verb)),
        columns=['filler_id', 'vFiller_position_condition', 'filler_verb_in_question', 'filler_verb_in_picture'])
    for iFiller in filler_id:
        tFiller_verb.loc[np.logical_and(tFiller_verb.vFiller_position_condition == 'Verb',
                                        tFiller_verb.filler_id == iFiller), 'filler_verb_in_picture'] = \
            filler_correct_verb[filler_id.index(iFiller)]
    # end of filler verb

    tFiller = pd.concat([tFiller_agent, tFiller_verb, tFiller_patient], axis=1)
    tFiller = tFiller.loc[:, ~tFiller.columns.duplicated()]
    tFiller.columns = ["filler_or_item_id", "position_condition", "agent_in_question", "agent_in_picture",
                       "verb_in_question", "verb_in_picture", "patient_in_question", "patient_in_picture"]


                
    
    # make sure there is no such case that the agent and the patient is the same
    print("any trial with characters of the same name?")
    print(sum(np.logical_or(np.logical_or(tFiller.agent_in_picture == tFiller.patient_in_picture,
                                          tFiller.agent_in_picture == tFiller.patient_in_question),
                            np.logical_or(tFiller.agent_in_question == tFiller.patient_in_picture,
                                          tFiller.agent_in_question == tFiller.patient_in_question))
              ))
        

# this happens when agent and patient are of the same sex, and when the answer is no, and the name of the 
# position condition (e.g., agent) in picture is the same as -- in this case -- the patient's
#    if exp_name == 'exp2':
    for iTrial, iRow in tFiller.iterrows():
        if iRow.agent_in_picture == iRow.patient_in_picture:
            print("bad row to be fixed")
            print(iTrial)
#                print(iRow)
#                if iRow.position_condition == 'Agent':
            cur_sex = filler_wrong_agent_sex[iTrial]
            cur_name_pool = names[cur_sex]
            cur_name_pool.remove(iRow.agent_in_question)
            cur_name_pool.remove(iRow.patient_in_question)
            if iRow.position_condition == 'Agent':
                tFiller.iloc[iTrial, :].agent_in_picture = cur_name_pool[np.random.randint(1, len(cur_name_pool))]
            if iRow.position_condition == 'Patient':
                tFiller.iloc[iTrial, :].patient_in_picture = cur_name_pool[np.random.randint(1, len(cur_name_pool))]



    tAll_trials = pd.concat([tItem, tFiller], sort=False)

#    tAll_trials['picture_file'] = [a + '_is_' + v + "ing" + '_' + p + '.png' for a, v, p in
#                                   zip(tAll_trials.agent_in_picture, tAll_trials.verb_in_picture,
#                                       tAll_trials.patient_in_picture)]
#    tAll_trials['question_file'] = ["Is_" + a + '_' + v + "ing" + '_' + p + '.wav' for a, v, p in
#                                    zip(tAll_trials.agent_in_question, tAll_trials.verb_in_question,
#                                        tAll_trials.patient_in_question)]
                                    
    tAll_trials['picture_file'] = [a + 'Is' + v + "ing"  + p + '.png' for a, v, p in
                                   zip(tAll_trials.agent_in_picture, tAll_trials.verb_in_picture,
                                       tAll_trials.patient_in_picture)]
    tAll_trials['question_file'] = ["Is" + a + v + "ing" + p + '.wav' for a, v, p in
                                    zip(tAll_trials.agent_in_question, tAll_trials.verb_in_question,
                                        tAll_trials.patient_in_question)]                        

    tAll_trials['answer_script'] = [a + " is " + v.lower() + "ing " + p + "." for a, v, p in
                                    zip(tAll_trials.agent_in_picture, tAll_trials.verb_in_picture,
                                        tAll_trials.patient_in_picture)]

    tAll_trials = tAll_trials.replace({'Pokeing': 'Poking'}, regex=True)

    exp_trial_id = ["{:02d}".format(i) for i in range(1, exp_num_trials + 1)]

    trial_order = range(tAll_trials.shape[0])
    tAll_trials.index = trial_order
    tAll_trials = tAll_trials.sort_index()

    for iTrial, iRow in tAll_trials.iterrows():
        # print(tAll_trials.loc[iTrial, 'position_condition'])
        if tAll_trials.loc[iTrial, 'position_condition'] == 'Control':
            tAll_trials.loc[iTrial, 'answer_script'] = 'Yes ' + tAll_trials.loc[iTrial, 'answer_script']
        else:
            tAll_trials.loc[iTrial, 'answer_script'] = 'No ' + tAll_trials.loc[iTrial, 'answer_script']

    tAll_trials.insert(loc=0, column='trial_id', value=exp_trial_id)
    #    tAll_trials['trial_id'] = exp_trial_id
    tAll_trials.to_csv(os.path.join(exp_name, 'tAll_trials_ordered.csv'), encoding='utf-8', index=False)


    np.random.seed(my_seed[4])
    np.random.shuffle(trial_order)
    tAll_trials.index = trial_order
    tAll_trials = tAll_trials.sort_index()

    # tAll_trials['trial_id'] = exp_trial_id
    tAll_trials.to_csv(os.path.join(exp_name, 'tAll_trials.csv'), encoding='utf-8', index=False)

    if bCreate_stimuli == 1:
        # image = "sample-out.png"
        # img = Image.open(image)
        # draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        # font = ImageFont.truetype("sans-serif.ttf", 16)
        font0 = ImageFont.truetype("/Library/Fonts/Arial.ttf", 80)
        width1 = 80
        width2 = 900
        height = 1900
        color0 = (0, 0, 0, 0)

        # img.save('sample-out.png')

        for iTrial, iRow in tAll_trials.iterrows():
            cur_vanilla = glob.glob(os.path.join(vanilla_dir, '*' + iRow.verb_in_question + '*.png'))[0]
            print(iTrial)
            # print(cur_vanilla)
            cur_img = Image.open(cur_vanilla)
            draw = ImageDraw.Draw(cur_img)
            draw.text((width1, height), iRow.agent_in_picture, color0, font=font0)
            draw.text((width2, height), iRow.patient_in_picture, color0, font=font0)
            cur_img.save(os.path.join(output_dir, iRow.picture_file))
