from scipy.stats import multinomial as mn
import numpy as np

class Bandit3:
    def __init__(self):
        self.array = [1,0]
        self.probs = [[.1,.9], [.5,.5], [.9,.1]]
        self.n = np.zeros(3)
        self.total_reward = np.zeros(3)

    def play(self):
        i = 0
        for i in range(10000):
            i+=1
            #print('Round {}'.format(i))
            answer = np.random.choice(np.arange(1,4))
        #    answer = input('Which arm do you want to pull?')
            answer = int(answer)
            #print('Your answer: %d' % answer)
            #print(self.probs[answer - 1])
            reward = np.random.choice([0,1],1,p=self.probs[answer - 1])
            #print('Reward = {}!'.format(reward))
            self.total_reward[answer - 1] += reward
            self.n[answer-1] += 1
        print('N pulls on each arm: ', self.n)
        print('Average Reward = {}'.format(self.total_reward/self.n))
        print('Total Reward = {}'.format(self.total_reward))





if __name__=="__main__":
    bandit = Bandit3()
    bandit.play()
