from scipy.stats import multinomial as mn
import numpy as np

class BanditN:
    def __init__(self,n):
        self.n = n
        self.rewards = np.random.multivariate_normal(np.zeros(n), np.eye(n))
        print(np.shape(self.rewards))

        

        #self.array = [1,0]
        #self.probs = [[.1,.9], [.5,.5], [.9,.1]]
        #self.n = np.zeros(3)
        #self.reward = rewards
        #self.reward = np.random.multivariate_normal(mean

    def play(self,arm):
        reward = self.rewards[arm-1] + np.random.normal()

        #i = 0
        #for i in range(10000):
        #    i+=1
        #    #print('Round {}'.format(i))
        #    answer = np.random.choice(np.arange(1,4))
        ##    answer = input('Which arm do you want to pull?')
        #    answer = int(answer)
        #    #print('Your answer: %d' % answer)
        #    #print(self.probs[answer - 1])
        #    reward = np.random.choice([0,1],1,p=self.probs[answer - 1])
        #    #print('Reward = {}!'.format(reward))
        #    self.total_reward[answer - 1] += reward
        #    self.n[answer-1] += 1
        #print('N pulls on each arm: ', self.n)
        #print('Average Reward = {}'.format(self.total_reward/self.n))
        #print('Total Reward = {}'.format(self.total_reward))





if __name__=="__main__":
    for eps in [0,0.1,0.01]:
        for i in range(2000):
            bandit = BanditN(n)
            for j in range(1000):


    for i in range(1000):
        bandit.play
