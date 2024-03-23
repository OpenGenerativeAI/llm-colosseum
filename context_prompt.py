from agent import Robot

def context_prompt(robot: Robot, observation: dict, action: dict):

    side : int = robot.side
    obs_own = robot.observe(observation["P" + str(side)])
    obs_opp = robot.observe(observation["P" + str(abs(1-side))])

    action_hist= action["agent_" + str(side)]


    context = str(
        "The observation for you is: " + str(obs_own) + "\n"
        "The observation for the opponent is: " + str(obs_opp) + "\n"
        "The action history is: " + str(action_hist) + "\n"
    )

    return(context)





