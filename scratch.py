np.logical_or(np.logical_or(tFiller.agent_in_picture == tFiller.patient_in_picture, tFiller.agent_in_picture == tFiller.patient_in_question), np.logical_or(tFiller.agent_in_question == tFiller.patient_in_picture, tFiller.agent_in_question == tFiller.patient_in_question))
