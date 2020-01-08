#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def create_stimuli(bCreate_stimuli, iExp, exp_name, exp_lan, locations, num_locations, exp_num_of_items, exp_yes_to_no_ratio,
                   exp_num_trials,
                   exp_num_trial_yes, exp_num_trial_no, exp_num_of_control_for_each_item,
                   exp_num_of_correction_for_each_location_for_each_item, item_num_trial_total, item_num_trial_yes,
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
    import copy
    import sys

    np.random.seed(my_seed[0])
    vanilla_dir = 'vanilla_images1'
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



    sex_levels = ['F', 'M']
    num_sexes = len(sex_levels)
    vanilla_names_en = {'F': ["Nancy", "Vicky", "Tori", "Penny", "Jilly", "Cindy", "Laurie",
"Franny", "Brandy", "Betty", "Kylie", "Carrie", "Tracy", "Chloe",
"Annie", "Mindy", "Molly", "Sally", "Lacey", "Carlie", "Mandy",
"Hailey", "Lilly", "Jenny", "Judy", "Kerry", "Kelly", "Bonnie",
"Kimmy"],
             'M': ["Freddy", "Ronnie", "Davey", "Jimmy", "Kenny", "Percy", "Sammy",
"Harvey", "Gary", "Ollie", "Danny", "Henry", "Teddy", "Wally",
"Johnny", "Jerry", "Timmy", "Benny", "Tommy", "Joey"
                   ]}
             
#             F: "Annie", "Betty", "Bonnie", "Brandy", "Carlie", "Carrie", "Chloe",
#"Cindy", "Franny", "Hailey", "Jenny", "Jilly", "Judy", "Kelly",
#"Kerry", "Kimmy", "Kylie", "Lacey", "Laurie", "Lilly", "Mandy",
#"Mindy", "Molly", "Nancy", "Penny", "Sally", "Tori", "Tracy",
#"Vicky"
#             M: "Benny", "Danny", "Davey", "Freddy", "Gary", "Harvey", "Henry",
#"Jerry", "Jimmy", "Joey", "Johnny", "Kenny", "Ollie", "Percy",
#"Ronnie", "Sammy", "Teddy", "Timmy", "Tommy", "Wally"
#    vanilla_names_ch = {'F':["小李", "小宋", "小郑", "小秦", "小任", "小孔", 
#"小江", "小潘", "小赵", "小熊", "小廖", "小贾", "小谢", 
#"小朱", "小卢", "小汪", "小萧", "小崔", "小胡", "小王", 
#"小薛", "小沈", "小姚", "小邹", "小彭", "小陈", "小程", 
#"小杨", "小曾", "小康", "小吕", "小余", "小魏", "小黄", 
#"小刘", "小郭", "小夏", "小蔡", "小唐", "小吴", "小田", 
#"小梁", "小白", "小张", "小姜"],
#                                 'M':["小方", "小叶", "小曹", 
#"小蒋", "小谭", "小范", "小陆", "小徐", "小石", "小冯", 
#"小邱", "小傅", "小丁", "小高", "小罗", "小钟", "小邓", 
#"小杜", "小许", "小戴", "小马", "小郝", "小苏", "小毛", 
#"小史", "小阎", "小孙", "小何", "小袁", "小金", "小韩", 
#"小董", "小林", "小周", "小于"]}
                                 
#    vanilla_names_ch = {'F':["小李", "小宋", "小郑", "小秦", "小任", "小孔", 
#"小江", "小潘", "小赵", "小熊", "小廖", "小贾", "小谢", 
#"小朱", "小卢", "小汪"],
#                                 'M':["小方", "小叶", "小曹", 
#"小蒋", "小谭", "小范", "小陆", "小徐", "小石", "小冯", 
#"小邱", "小傅", "小丁"]}
                                 
    vanilla_names_ch = {'F':["王芳", "李娜", "张敏", "李静", "李梅", "张丽", 
"王静", "张静", "李敏", "王敏", "王丽", "李娟", "张艳", 
"李燕", "王娟", "李霞", "刘敏", "李丽", "刘芳", "张悦", 
"李妍"],
                        'M':["张伟", "王伟", "李伟", "刘伟", "李强", "张磊", 
"王磊", "李军", "刘洋", "王勇", "张勇", "王艳", "李杰", 
"王强", "王军", "张杰", "张涛", "王涛", "李明", "王超", 
"李勇", "刘杰", "张军", "张强", "王平", "王刚", "王杰"]}                               
                                 
    if exp_lan == 'en':
        vanilla_names = copy.deepcopy(vanilla_names_en)
#        verb_cat = copy.deepcopy(verb_cat_en)
#        verbs = copy.deepcopy(verb_en)
        verbs = np.array(["Kiss", "Kick", "Poke", "Lift", "Push", "Pull"])
        verbs = ["Kiss", "Kick", "Poke", "Lift", "Push", "Pull"]

    elif exp_lan == 'ch':
        vanilla_names = copy.deepcopy(vanilla_names_ch)
        verbs = np.array(["Kiss", "Kick", "Poke", "Push", "Pull"])
        verbs = ["Kiss", "Kick", "Poke", "Push", "Pull"]


        
     
# names used in items will be removed to avoid repition in items        
    names = copy.deepcopy(vanilla_names)
     

    verb_cat = {'M_F_verbs': ["Kick", "Kiss", "Lift", "Pull", "Push", "Poke"],
    'F_M_verbs' : ["Kick", "Kiss", "Lift", "Poke", "Push"],
    'F_F_verbs' : ["Lift", "Poke", "Pull", "Push"],
    'M_M_verbs' : ["Lift", "Poke", "Pull"]}
    
    
#    verbs = np.tile(np.array(["Kiss", "Kick", "Poke", "Lift", "Push", "Pull"]), (4, 1))[iExp]
    
    
    verbs_ch = {'Kick':'踢了',
               'Kiss':'亲了',
               'Poke':'戳了',
               'Push':'推了',
               'Pull':'拉了'}
    agent_sex_mapped_to_verb = {'Kiss':'F',
                                'Kick':'F',
                                'Poke':'F',
                                'Lift':'M',
                                'Push':'M',
                                'Pull':'F'}
    
    patient_sex_mapped_to_verb = {'Kiss':'M',
                                  'Kick':'M',
                                  'Poke':'F',
                                  'Lift':'M',
                                  'Push':'F',
                                  'Pull':'F'}
    
#    agent_sex_mapped_to_verb = ['F', 'F', 'F', 'M', 'M', 'F']
#    patient_sex_mapped_to_verb = ['M', 'M', 'F', 'M', 'F', 'F']
    num_verbs = len(verbs)

    item_correct_verb = np.array(["Kick", "Kiss", "Push", "Pull"])
    item_correct_verb = ["Kick", "Kiss", "Push", "Pull"]

    # item
    item_correct_agent_sex = [agent_sex_mapped_to_verb[i] for i in item_correct_verb]
    item_correct_patient_sex = [patient_sex_mapped_to_verb[i] for i in item_correct_verb]

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

    vItem_location_condition = np.tile(
        np.concatenate((np.repeat(locations, exp_num_of_correction_for_each_location_for_each_item),
                        np.repeat(['Control'], exp_num_of_control_for_each_item))), exp_num_of_items)

    ## start of item agent
    # vItem_agent_in_picture = np.repeat(item_correct_agent, item_num_trial_for_each_item)

    # vItem_agent_in_question = np.copy(vItem_agent_in_picture)

    tItem_agent = pd.DataFrame(
        list(zip(vItem_id, vItem_location_condition, vItem_correct_agent, vItem_correct_agent)),
        columns=['vItem_id', 'vItem_location_condition', 'vItem_agent_in_picture', 'vItem_agent_in_question'])

    for iTrial, iRow in tItem_agent.iterrows():
        if iRow.vItem_location_condition == 'Agent':
            tItem_agent.loc[iTrial, 'vItem_agent_in_question'] = item_wrong_agent[iTrial]
    # for iItem in item_id:
    #     tItem_agent.loc[np.logical_and(tItem_agent.vItem_location_condition == 'Agent',
    #                                    tItem_agent.vItem_id == iItem), 'vItem_agent_in_question'] = item_wrong_agent[
    #         item_id.index(iItem)]
    # print(tItem_agent)
    ## end of item agent

    ## start of item patient
    # vItem_patient_in_picture = np.repeat(item_correct_patient, item_num_trial_for_each_item)

    # vItem_patient_in_question = np.copy(vItem_patient_in_picture)

    tItem_patient = pd.DataFrame(
        list(zip(vItem_id, vItem_location_condition, vItem_correct_patient, vItem_correct_patient)),
        columns=['vItem_id', 'vItem_location_condition', 'vItem_patient_in_picture', 'vItem_patient_in_question'])

    for iTrial, iRow in tItem_patient.iterrows():
        if iRow.vItem_location_condition == 'Patient':
            tItem_patient.loc[iTrial, 'vItem_patient_in_question'] = item_wrong_patient[iTrial]
    # for iItem in item_id:
    #     tItem_patient.loc[np.logical_and(tItem_patient.vItem_location_condition == 'Patient',
    #                                    tItem_patient.vItem_id == iItem), 'vItem_patient_in_question'] = item_wrong_patient[
    #         item_id.index(iItem)]
    # print(tItem_patient)
    ## end of item patient

    ## start of item verb
    # vItem_verb_in_picture = np.repeat(item_correct_verb, item_num_trial_for_each_item)

    # vItem_verb_in_question = np.copy(vItem_verb_in_picture)

    tItem_verb = pd.DataFrame(
        list(zip(vItem_id, vItem_location_condition, vItem_correct_verb, vItem_correct_verb)),
        columns=['vItem_id', 'vItem_location_condition', 'vItem_verb_in_picture', 'vItem_verb_in_question'])

    for iTrial, iRow in tItem_verb.iterrows():
        if iRow.vItem_location_condition == 'Verb':
            tItem_verb.loc[iTrial, 'vItem_verb_in_question'] = item_wrong_verb[iTrial]
    # for iItem in item_id:
    #     tItem_verb.loc[np.logical_and(tItem_verb.vItem_location_condition == 'Verb',
    #                                    tItem_verb.vItem_id == iItem), 'vItem_verb_in_question'] = item_wrong_verb[
    #         item_id.index(iItem)]
    # print(tItem_verb)
    ## end of item verb

    tItem = pd.concat([tItem_agent, tItem_verb, tItem_patient], axis=1)
    tItem = tItem.loc[:, ~tItem.columns.duplicated()]
    tItem.columns = ["filler_or_item_id", "location_condition", "agent_in_picture", "agent_in_question",
                     "verb_in_picture", "verb_in_question", "patient_in_picture", "patient_in_question"]

    filler_id0 = ["{:02d}".format(i) for i in range(1, filler_num_trial_total + 1)]
    filler_id = ["filler_" + i for i in filler_id0]
    filler_location_condition_for_no = [locations[i] for i in
                                        np.random.randint(num_locations, size=filler_num_trial_no)]
    vFiller_location_condition = np.concatenate(
        (filler_location_condition_for_no, np.tile(['Control'], filler_num_trial_yes)))

    np.random.seed(my_seed[1])
    filler_wrong_verb = [verbs[np.random.randint(0, num_verbs)] for i in range(filler_num_trial_total)]
    # filler_correct_verb = [verbs[num_verbs - 1 - verbs.index(i)] for i in filler_wrong_verb]


    filler_correct_verb = []
#    for iV in filler_wrong_verb:
#        for iC in verb_cat.values():
#            if iV in iC:
#                break
#        print(iV)
#        print(iC)
#        iNum_verbs = len(iC)
#        correct_verb = iC[(iC.index(iV) + np.random.randint(1, iNum_verbs)) % iNum_verbs]
#        print(correct_verb)
##        filler_correct_verb.append(correct_verb)
    for iV in filler_wrong_verb:
        cur_cat = agent_sex_mapped_to_verb[iV] + '_' + patient_sex_mapped_to_verb[iV] + '_verbs'
        iC = verb_cat[cur_cat]
#        print("new round")
#        print(iV)
#        print(cur_cat)
#        print(iC)
        iNum_verbs = len(iC)
        correct_verb = iC[(iC.index(iV) + np.random.randint(1, iNum_verbs)) % iNum_verbs]
#        print(correct_verb)
        filler_correct_verb.append(correct_verb)
    
    
#    filler_correct_verb = [verbs[(verbs.index(i) + np.random.randint(1, num_verbs)) % num_verbs] for i in
#                           filler_wrong_verb]
    # to check should be all false
    # [filler_wrong_verb[i] == filler_correct_verb[i] for i in range(len(filler_wrong_verb))]

    filler_wrong_agent_sex = [agent_sex_mapped_to_verb[i] for i in filler_wrong_verb]
    filler_wrong_patient_sex = [patient_sex_mapped_to_verb[i] for i in filler_wrong_verb]

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
        zip(filler_id, vFiller_location_condition, filler_wrong_agent, filler_wrong_agent),
        columns=['filler_id', 'vFiller_location_condition', 'filler_agent_in_question', 'filler_agent_in_picture'])
    for iFiller in filler_id:
        tFiller_agent.loc[np.logical_and(tFiller_agent.vFiller_location_condition == 'Agent',
                                         tFiller_agent.filler_id == iFiller), 'filler_agent_in_picture'] = \
            filler_correct_agent[filler_id.index(iFiller)]
    # end of filler agent

    ## start of filler patient
    np.random.seed(my_seed[3])
    
#    filler_wrong_patient = [names[i][np.random.randint(len(names[i]))] for i in filler_wrong_patient_sex]
    filler_wrong_patient = []
    for i in range(len(filler_wrong_agent)):
        cur_sex = filler_wrong_patient_sex[i]
        cur_name_pool = names[cur_sex]
        if filler_wrong_agent[i] in cur_name_pool:
            cur_wrong_agent_index = cur_name_pool.index(filler_wrong_agent[i])
        else:
            cur_wrong_agent_index = 0
#        cur_wrong_name_index = cur_name_pool.index(filler_wrong_patient[i])
        cur_correct_name_index = (cur_wrong_agent_index + np.random.randint(1, len(cur_name_pool))) % len(cur_name_pool)
        cur_correct_name = cur_name_pool[cur_correct_name_index]
        filler_wrong_patient.append(cur_correct_name)
        
        
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
        list(zip(filler_id, vFiller_location_condition, filler_wrong_patient, filler_wrong_patient)),
        columns=['filler_id', 'vFiller_location_condition', 'filler_patient_in_question', 'filler_patient_in_picture'])
    for iFiller in filler_id:
        tFiller_patient.loc[np.logical_and(tFiller_patient.vFiller_location_condition == 'Patient',
                                           tFiller_patient.filler_id == iFiller), 'filler_patient_in_picture'] = \
            filler_correct_patient[filler_id.index(iFiller)]
    # end of filler patient

    ## start of filler verb
    # filler_verb_in_question = filler_wrong_verb[:]

    # filler_verb_in_picture = filler_verb_in_question[:]

    tFiller_verb = pd.DataFrame(
        list(zip(filler_id, vFiller_location_condition, filler_wrong_verb, filler_wrong_verb)),
        columns=['filler_id', 'vFiller_location_condition', 'filler_verb_in_question', 'filler_verb_in_picture'])
    for iFiller in filler_id:
        tFiller_verb.loc[np.logical_and(tFiller_verb.vFiller_location_condition == 'Verb',
                                        tFiller_verb.filler_id == iFiller), 'filler_verb_in_picture'] = \
            filler_correct_verb[filler_id.index(iFiller)]
    # end of filler verb

    tFiller = pd.concat([tFiller_agent, tFiller_verb, tFiller_patient], axis=1)
    tFiller = tFiller.loc[:, ~tFiller.columns.duplicated()]
    tFiller.columns = ["filler_or_item_id", "location_condition", "agent_in_question", "agent_in_picture",
                       "verb_in_question", "verb_in_picture", "patient_in_question", "patient_in_picture"]




    # make sure there is no such case that the agent and the patient is the same
    print("any trial with characters of the same name?")
    print(sum(np.logical_or(np.logical_or(tFiller.agent_in_picture == tFiller.patient_in_picture,
                                          tFiller.agent_in_picture == tFiller.patient_in_question),
                            np.logical_or(tFiller.agent_in_question == tFiller.patient_in_picture,
                                          tFiller.agent_in_question == tFiller.patient_in_question))
              ))


# this happens when agent and patient are of the same sex, and when the answer is no, and the name of the
# location condition (e.g., agent) in picture is the same as -- in this case -- the patient's
#    if exp_name == 'exp2':
    for iTrial, iRow in tFiller.iterrows():
        if iRow.agent_in_picture == iRow.patient_in_picture:
            print("bad row to be fixed")
            print(iTrial)
            print(iRow)
#                if iRow.location_condition == 'Agent':
            cur_sex = filler_wrong_agent_sex[iTrial]
            cur_name_pool = names[cur_sex]
            # add this conditioning because in rare cases that when there are multiple bad trials, the
            # bad name in a later trial is already removed in the previus trials
            if iRow.agent_in_question in cur_name_pool:
                cur_name_pool.remove(iRow.agent_in_question)
            if iRow.agent_in_question in cur_name_pool:
                cur_name_pool.remove(iRow.patient_in_question)
            if iRow.location_condition == 'Agent':
                tFiller.iloc[iTrial, :].agent_in_picture = cur_name_pool[np.random.randint(1, len(cur_name_pool))]
            if iRow.location_condition == 'Patient':
                tFiller.iloc[iTrial, :].patient_in_picture = cur_name_pool[np.random.randint(1, len(cur_name_pool))]



    tAll_trials = pd.concat([tItem, tFiller], sort=False)

#    tAll_trials['picture_file'] = [a + '_is_' + v + "ing" + '_' + p + '.png' for a, v, p in
#                                   zip(tAll_trials.agent_in_picture, tAll_trials.verb_in_picture,
#                                       tAll_trials.patient_in_picture)]
#    tAll_trials['question_file'] = ["Is_" + a + '_' + v + "ing" + '_' + p + '.wav' for a, v, p in
#                                    zip(tAll_trials.agent_in_question, tAll_trials.verb_in_question,
#                                        tAll_trials.patient_in_question)]

    if exp_lan == 'en':
        tAll_trials['picture_file'] = [a + 'Is' + v + "ing"  + p + '.png' for a, v, p in
                                       zip(tAll_trials.agent_in_picture, tAll_trials.verb_in_picture,
                                           tAll_trials.patient_in_picture)]
        tAll_trials['question_file'] = ["Is" + a + v + "ing" + p + '.wav' for a, v, p in
                                        zip(tAll_trials.agent_in_question, tAll_trials.verb_in_question,
                                            tAll_trials.patient_in_question)]
    
        tAll_trials['answer_script'] = [a + " is " + v.lower() + "ing " + p for a, v, p in
                                        zip(tAll_trials.agent_in_picture, tAll_trials.verb_in_picture,
                                            tAll_trials.patient_in_picture)]
     
    #
    #    tAll_trials['question_script'] = ['Is ' + a + ' ' + v.lower() + 'ing ' + p + '?' for a, v, p in
                                     # zip(tAll_trials.agent_in_question, tAll_trials.verb_in_question,
                                     #     tAll_trials.patient_in_question)]
    #    for google speech recognition comes with the speech recognition package
        tAll_trials['question_script'] = ['is ' + a + ' ' + v.lower() + 'ing ' + p for a, v, p in
                                        zip(tAll_trials.agent_in_question, tAll_trials.verb_in_question,
                                            tAll_trials.patient_in_question)]
    
        tAll_trials = tAll_trials.replace({'Pokeing': 'Poking'}, regex=True)
        tAll_trials = tAll_trials.replace({'pokeing': 'poking'}, regex=True)                                       
                                        
    elif exp_lan == 'ch':
        tAll_trials['picture_file'] = [a + verbs_ch[v] + p + '.png' for a, v, p in
                                       zip(tAll_trials.agent_in_picture, tAll_trials.verb_in_picture,
                                           tAll_trials.patient_in_picture)]
        tAll_trials['question_file'] = [a + verbs_ch[v] + p + '吗.wav' for a, v, p in
                                        zip(tAll_trials.agent_in_question, tAll_trials.verb_in_question,
                                            tAll_trials.patient_in_question)]
    
        tAll_trials['answer_script'] = [a + verbs_ch[v] + p for a, v, p in
                                        zip(tAll_trials.agent_in_picture, tAll_trials.verb_in_picture,
                                            tAll_trials.patient_in_picture)]        

        tAll_trials['question_script'] = [a + verbs_ch[v] + p + '吗' for a, v, p in
                                        zip(tAll_trials.agent_in_question, tAll_trials.verb_in_question,
                                            tAll_trials.patient_in_question)]                                        




    exp_trial_id = ["{:02d}".format(i) for i in range(1, exp_num_trials + 1)]

    trial_order = range(tAll_trials.shape[0])
    tAll_trials.index = trial_order
#    https://stackoverflow.com/questions/20484195/typeerror-range-object-does-not-support-item-assignment
#    http://sweetme.at/2013/10/21/how-to-detect-python-2-vs-3-in-your-python-script/    
    if (sys.version_info >= (3, 0)):
        trial_order = list(trial_order)
#    tAll_trials = tAll_trials.sort_index()

    for iTrial, iRow in tAll_trials.iterrows():
        # print(tAll_trials.loc[iTrial, 'location_condition'])
        if exp_lan == 'en':
            if tAll_trials.loc[iTrial, 'location_condition'] == 'Control':
                tAll_trials.loc[iTrial, 'answer_script'] = 'yes ' + tAll_trials.loc[iTrial, 'answer_script']
            else:
                tAll_trials.loc[iTrial, 'answer_script'] = 'no ' + tAll_trials.loc[iTrial, 'answer_script']
        elif exp_lan == 'ch':
            if tAll_trials.loc[iTrial, 'location_condition'] == 'Control':
                tAll_trials.loc[iTrial, 'answer_script'] = '是' + tAll_trials.loc[iTrial, 'answer_script']
            else:
                tAll_trials.loc[iTrial, 'answer_script'] = '不' + tAll_trials.loc[iTrial, 'answer_script']

    tAll_trials.insert(loc=0, column='trial_id', value=exp_trial_id)
    #    tAll_trials['trial_id'] = exp_trial_id
    tAll_trials.to_csv(os.path.join(exp_name, 'tAll_trials_ordered.csv'), encoding='utf-8', index=False)



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
        font0 = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 80)
#        font0 = ImageFont.truetype("/Library/Fonts/simsum.ttc", 80)
        width1 = 80
        width2 = 900
        height = 1900
#        color0 = (0, 0, 0, 0)


        # img.save('sample-out.png')

        for iTrial, iRow in tAll_trials.iterrows():
            for iS, iNames in vanilla_names.items():
                if iRow.agent_in_picture in iNames:
                    agent_sex = iS
                    break
            for iS, iNames in vanilla_names.items():
                if iRow.patient_in_picture in iNames:
                    patient_sex = iS
                    break          
#            print(agent_sex + '_' + iRow.verb_in_picture + '_' + patient_sex + '.png')
            if exp_lan == 'en':        
                cur_vanilla = glob.glob(os.path.join(vanilla_dir, agent_sex + '_' + iRow.verb_in_picture + '_' + patient_sex + '.png'))[0]
            elif exp_lan == 'ch':
                cur_vanilla = glob.glob(os.path.join(vanilla_dir, '*' + verbs_ch[iRow.verb_in_picture] + '*.png'))[0]

            print(iTrial)
            # print(cur_vanilla)
            cur_img = Image.open(cur_vanilla)
            draw = ImageDraw.Draw(cur_img)
#            draw.text((width1, height), iRow.agent_in_picture, color0, font=font0)
#            draw.text((width2, height), iRow.patient_in_picture, color0, font=font0)
            draw.text((width1, height), iRow.agent_in_picture, fill=(0,0,0), font=font0)
#            draw.text((width1, height), '喜欢啊', fill=(0,0,0), font=font0)

            draw.text((width2, height), iRow.patient_in_picture, fill=(0,0,0), font=font0)
            cur_img.save(os.path.join(output_dir, iRow.picture_file))
