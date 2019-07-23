import numpy as np
import seaborn
from matplotlib import pyplot as plt

class BanditN:
    def __init__(self,action_values):
        self.action_values = action_values
        self.average_rewards = np.zeros(len(action_values))
        self.n_pulls = np.zeros(len(action_values))

    def play(self,eps):
        #Give reward of q(A_t) + \eps where \eps~N(0,1)
        index = np.argmax(self.average_rewards)
        other_indices = np.delete(np.arange(len(self.average_rewards)), index)
        final_index = np.random.choice([index, np.random.choice(other_indices)], 
                p = [1-eps, eps])

        self.n_pulls[final_index] += 1
        reward = self.action_values[final_index] + np.random.normal()
        self.update_average_rewards(reward, final_index)
        #print(
        #"""
        #   On iteration: {}
        #  Action Values: {}
        #Average rewards: {}
        #        N_pulls: {}
        #            Eps: {}
        #     You played: {}
        #         Reward: {}
        #""".format(j,
        #    self.action_values,
        #    self.average_rewards,
        #    self.n_pulls,
        #    eps, 
        #    final_index, 
        #    reward)
        #)

        
        return reward

    def update_average_rewards(self,reward, index):
        n_pulls = self.n_pulls[index]
        self.average_rewards[index] = (reward + self.average_rewards[index] * (n_pulls-1)) / n_pulls



if __name__=="__main__":
    #Different tolerances
    n = 10
    action_values = np.random.multivariate_normal(np.zeros(n), np.eye(n))
    bandit = BanditN(action_values)

    for eps in [0,0.1,0.01]:
        #Different experiments
        reward_trajectory_list = []
        for i in range(2000):
            print('{}/2000'.format(i))
            action_values = np.random.multivariate_normal(np.zeros(n), np.eye(n))
            bandit = BanditN(action_values)
            reward_trajectory = []
            for j in range(100):
                reward = bandit.play(eps)
                reward_trajectory.append(reward)
            reward_trajectory_list.append(reward_trajectory)
        #average all runs
        averages = np.array(reward_trajectory_list).mean(axis = 0)
        plt.plot(averages, label = 'eps = {}'.format(eps))
        plt.legend()
    plt.show()



