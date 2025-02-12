import inspect
import numpy as np
import os
import tensorflow as tf

from stable_baselines3 import PPO, A2C, DQN, HER, DDPG, SAC, TD3
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common import results_plotter
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.results_plotter import load_results, ts2xy, plot_results
from stable_baselines3.common.noise import NormalActionNoise

from CybORG import CybORG
from CybORG.Agents.BaseAgent import BaseAgent

class RLAgent(BaseAgent):

    def __init__(self, env, agent_type, model_name=None):
        super().__init__()
        self.agent_type = agent_type

        if model_name is None:
            if agent_type == "PPO":
                self.model = PPO('MlpPolicy', env, tensorboard_log= "./tb_logs/", verbose=1)
            elif agent_type == "A2C":
                self.model = A2C('MlpPolicy',env, tensorboard_log= "./tb_logs/", verbose=1 )
            elif agent_type == "DQN":
                self.model = DQN('MlpPolicy',env, tensorboard_log= "./tb_logs/", verbose=1, exploration_fraction = 0.90)
            else:
                raise Exception("Unknown Agent Type {}".format(agent_type))
        else:
            #print('loading...')
            self.load(agent_type, model_name)

    def train(self, timesteps,log_name, callback = None):
      self.model.learn(timesteps, tb_log_name=log_name)

    def get_action(self, observation, action_space):

        if self.agent_type == "DQN":
            action, _states = self.model.predict(observation, deterministic=True)
        else:
            action, _states = self.model.predict(observation)
            #if action > 40:
             #   print(action)
            #print("Returning action...", action)
        return action

    def save(self, name = None):
        if name is None:
            name = "{}-{}".format(datetime.datetime.now(), self.agent_type)
        self.model.save(name)

    def load(self,agent_type, model_name):
        #print("Loading up RL algorithm {agent_type} with name {model_name}")
        if agent_type == "PPO":
            #print("Loading PPO Agent")
            self.model = PPO.load(model_name)
        elif agent_type == "A2C":
            self.model = A2C.load(model_name)
        elif agent_type == "DQN":
            self.model = DQN.load( model_name)

        self.agent_type = "{} ({})".format(self.agent_type,  model_name)

    def __str_(self):
        return self.agent_type
