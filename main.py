import retro

env = retro.make(
            'StreetFighterIISpecialChampionEdition-Genesis',
            scenario='scenario',
            obs_type=retro.Observations.RAM
      )

observation = env.reset()

while True:
    env.render()
    print(observation)
    
    action = env.action_space.sample()
    
    observation, reward, done, info = env.step(action)
    
    if done:
        break

env.close()
