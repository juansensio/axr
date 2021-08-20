import math
import numpy as np
import pygame


class Agent():
    def __init__(self, ms_per_click, verbose):
        self.ms_per_click = ms_per_click
        self.verbose = verbose

    def start(self):
        self.acciones = {k: 0 for k in range(5)}
        self.last_click = pygame.time.get_ticks()

    def click(self, t):
        ms = pygame.time.get_ticks() - self.last_click
        if ms > self.ms_per_click:
            self.last_click = pygame.time.get_ticks()
            return self.get_action(t)
        return None

    def get_action(self, t):
        return None

    def update(self, a):
        self.acciones[a] += 1
        if self.verbose:
            print("N", self.acciones)


class AgentEGreedy(Agent):
    def __init__(self, ms_per_click, epsilon, alpha, Q0=0, verbose=True):
        super().__init__(ms_per_click, verbose)
        self.epsilon = epsilon
        self.alpha = alpha
        self.Q0 = Q0

    def start(self):
        super().start()
        self.Q = {k: self.Q0 for k in range(5)}

    def get_action(self, t):
        # acción aleatoria
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.randint(5)
        # acción con mayor valor
        return max(self.Q, key=self.Q.get)

    def update(self, a, reward):
        self.Q[a] += self.alpha*(reward - self.Q[a])
        if self.verbose:
            print("Q", self.Q)
        super().update(a)


class AgentUCB(AgentEGreedy):
    def __init__(self, ms_per_click, alpha, c, Q0, verbose):
        super().__init__(ms_per_click, 0, alpha, Q0, verbose)
        self.c = c

    def get_action(self, t):
        A = {
            j: self.Q[j] + self.c*math.sqrt(math.log(t)/(self.acciones[j]+1))
            for j in range(5)
        }
        return max(A, key=A.get)

    def update(self, a, reward):
        super().update(a, reward)


def softmax(x):
    return np.exp(x)/sum(np.exp(x))


class AgentGradientAscent(Agent):
    def __init__(self, ms_per_click, alpha, verbose):
        super().__init__(ms_per_click, verbose)
        self.alpha = alpha

    def start(self):
        super().start()
        self.H = np.zeros(5)
        self.pi = softmax(self.H)
        self.recompensas = []

    def get_action(self, t):
        return np.random.choice(range(5), 1, p=self.pi)[0]

    def update(self, a, reward):
        # actualizar preferencias
        self.recompensas.append(reward)
        recompensa_media = np.mean(self.recompensas)
        for j in range(5):
            if j == a:
                self.H[j] += self.alpha * \
                    (reward - recompensa_media)*(1-self.pi[j])
            else:
                self.H[j] -= self.alpha*(reward - recompensa_media)*self.pi[j]
        # actualizar probabilidades
        self.pi = softmax(self.H)
        if self.verbose:
            print("pi", self.pi)
        super().update(a)
