from player import Player
import numpy as np
import copy
import random
import os
from config import CONFIG


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # TODO : DONE
        # child: an object of class `Player`
        mu, sigma = 0, 2
        layer_sizes = child.nn.sizes
        a1 = np.random.random()
        if a1 <= 0.2:
            weight1_noise = np.random.normal(mu, np.random.random(), size=(layer_sizes[1], layer_sizes[0]))
            child.nn.inputLayer1Weights += weight1_noise
        a2 = np.random.random()
        if a2 <= 0.2:
            weight2_noise = np.random.normal(mu, np.random.random(), size=(layer_sizes[2], layer_sizes[1]))
            child.nn.layer2OutputWeights += weight2_noise
        a3 = np.random.random()
        if a3 <= 0.2:
            bias1_noise = np.random.normal(mu, np.random.random(), size=((layer_sizes[1], 1)))
            child.nn.bias1 += bias1_noise
        a4 = np.random.random()
        if a4 <= 0.2:
            bias2_noise = np.random.normal(mu, np.random.random(), size=((layer_sizes[2], 1)))
            child.nn.bias2 += bias2_noise



    def generate_new_population(self, num_players, prev_players=None):
        total = 0
        teenage_mutant_ninja_turtles = []
        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # TODO : IN DONE
            # num_players example: 150
            # prev_players: an array of `Player` objects

            # TODO: crossover
            # prev_players =self.crossover(num_players, prev_players)

            for player in prev_players:
                total += player.fitness

            # TODO (additional): a selection method other than `fitness proportionate`: DONe
            #probs = [1/len(prev_players) for _ in prev_players]
            probs = [chromosome.fitness/total for chromosome in prev_players]

            new_players = np.random.choice(prev_players,num_players, p=probs)


            for new_player in new_players:
                cp = copy.deepcopy(new_player)
                self.mutate(cp)
                teenage_mutant_ninja_turtles.append(cp)

            return teenage_mutant_ninja_turtles

    def next_population_selection(self, players, num_players):

        # TODO: DONE
        # num_players example: 100
        # players: an array of `Player` objects
        players.sort(key=lambda x: x.fitness, reverse = True)
        # TODO (additional): a selection method other than `top-k` : DONE
        # TODO (additional): plotting : IN PROGRESS
        sum = 0
        for i in players:
            sum += i.fitness
        self.write_output(players[0].fitness, players[len(players)-1].fitness, sum/len(players))

        return players[: num_players]

    """def next_population_selection(self, players, num_players):
        sample_quantity = 5
        chosen_ones = []
        while len(chosen_ones) != num_players:
            samples = random.sample(players, sample_quantity)
            samples.sort(key=lambda x: x.fitness, reverse=True)
            for i in range(len(samples)):
                if samples[i] not in chosen_ones:
                    chosen_ones.append(samples[i])
                    break
        return chosen_ones"""

    def crossover(self, num_players, players):
        chosen_ones = []
        for i in range(num_players):
            parents = random.sample(players, 2)
            a = random.random()
            if a >= 0.8 :
                #do crossover
                copied = copy.deepcopy(parents)
                copied[0].nn.inputLayer1Weights  = copied[0].nn.inputLayer1Weights
                copied[0].nn.layer2OutputWeights = copied[1].nn.layer2OutputWeights
                copied[0].nn.bias1 = copied[0].nn.bias1
                copied[0].nn.bias2 = copied[1].nn.bias2
                chosen_ones.append(copied[0])
            else:
                chosen_ones.append(parents[0])
        return chosen_ones

    def write_output(self, max, min, average):
        with open(f"./plot/data.txt", "a") as f:
            f.write(str(max) + " "+ str(min) + " "+ str(average)+ "\n")
            f.close()
