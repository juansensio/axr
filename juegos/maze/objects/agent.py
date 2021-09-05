from src.utils import load_image
import numpy as np
import pygame
from tqdm import tqdm


class Agent:
    def __init__(self, maze, its=20, pos=(0, 0), verbose=False, step=(32, 32), sprite="./maze/assets/sprites/character0.png"):
        self.step = step
        self.sprite, self.rect = load_image(sprite, {'scale': [(32, 32)]}, -1)
        self.init_pos = (pos[0]*step[0], pos[1]*step[1])
        self._init_pos = list(pos)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.num_states, self.probas_trans = self.get_probas_trans(maze)
        self.rewards = self.get_rewards(maze)
        self.pi = self.get_ini_policy(self.num_states)
        self.its = its
        self.pi, v = self.value_iteration(self.pi)
        if verbose:
            print(v.reshape((int(v.shape[0]**0.5), int(v.shape[0]**0.5))))

    def get_probas_trans(self, maze):
        num_states = maze.size[0]*maze.size[1]
        probas_trans = np.zeros((
            num_states,
            4,
            num_states
        ))
        # acciones
        for i in range(maze.size[0]):
            for j in range(maze.size[1]):
                s = i*maze.size[1] + j

                t = s-maze.size[1]
                r = s+1
                b = s+maze.size[1]
                l = s-1

                if i == 0 or t in maze.block_states:
                    probas_trans[s, 0, s] = 1
                else:
                    probas_trans[s, 0, t] = 1

                if i == maze.size[0] - 1 or b in maze.block_states:
                    probas_trans[s, 2, s] = 1
                else:
                    probas_trans[s, 2, b] = 1

                if j == 0 or l in maze.block_states:
                    probas_trans[s, 3, s] = 1
                else:
                    probas_trans[s, 3, l] = 1

                if j == maze.size[1] - 1 or r in maze.block_states:
                    probas_trans[s, 1, s] = 1
                else:
                    probas_trans[s, 1, r] = 1
        # estados terminales
        for terminal_state in maze.terminal_states:
            probas_trans[terminal_state[0], :, :] = 0
        return num_states, probas_trans

    def get_rewards(self, maze):
        num_states = maze.size[0]*maze.size[1]
        recompensas = -1*np.ones((num_states, 4, num_states))  # todas a -1
        # estados terminales
        for terminal_state in maze.terminal_states:
            recompensas[terminal_state[0], :, :] = 0
        return recompensas

    def get_ini_policy(self, num_states):
        # random
        return 0.25*np.ones((num_states, 4))

    def eval_pol(self, pi, gamma=1, its=1, v=None):
        v = np.zeros(self.num_states) if v is None else v
        for it in range(its):
            v_prev = v.copy()
            for s in range(self.num_states):
                v[s] = np.sum([
                    pi[s, a]*np.sum([
                        self.probas_trans[s][a][sp] *
                        (self.rewards[s][a][sp] + gamma*v_prev[sp])
                        for sp in range(self.num_states)
                    ])
                    for a in range(4)
                ])
        return v

    def eval_q(self, v, gamma=1):
        q = np.zeros((self.num_states, 4))
        for s in range(self.num_states):
            for a in range(4):
                q[s, a] = np.sum([
                    self.probas_trans[s][a][sp] *
                    (self.rewards[s][a][sp] + gamma*v[sp])
                    for sp in range(self.num_states)
                ])
        return q

    def greedy_pol(self, q):
        p = np.zeros((self.num_states, 4))
        p[range(self.num_states), q.argmax(axis=1)] = 1
        return p

    def value_iteration(self, pi):
        v = np.zeros(self.num_states)
        for it in tqdm(range(self.its)):
            v = self.eval_pol(pi, its=1, v=v)
            q = self.eval_q(v)
            pi = self.greedy_pol(q)
        return pi, v

    def start(self):
        self.rect.topleft = self.init_pos
        self.pos = [*self._init_pos]  # copy

    def update(self, maze):
        state = self.pos[1]*maze.size[1] + self.pos[0]
        a = np.random.choice(np.arange(4), 1, p=self.pi[state])
        if a == 0:
            newpos = self.rect.move((0, -self.step[1]))
            if self.valid_move(maze, newpos):
                self.pos[1] -= 1
                self.rect = newpos
        elif a == 1:
            newpos = self.rect.move((self.step[0], 0))
            if self.valid_move(maze, newpos):
                self.pos[0] += 1
                self.rect = newpos
        elif a == 2:
            newpos = self.rect.move((0, self.step[1]))
            if self.valid_move(maze, newpos):
                self.pos[1] += 1
                self.rect = newpos
        elif a == 3:
            newpos = self.rect.move((-self.step[0], 0))
            if self.valid_move(maze, newpos):
                self.pos[0] -= 1
                self.rect = newpos
        else:
            raise ValueError('invalid move')

    def valid_move(self, maze, newpos):
        return self.area.contains(newpos) and not maze.block(newpos)

    def render(self, screen):
        screen.blit(self.sprite, self.rect)
