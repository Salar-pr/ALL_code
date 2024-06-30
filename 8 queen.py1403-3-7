import random as rnd

n = int(input("enter your n:"))
p_s = n*n
n1 = n


def init_population(populaiton_size, n):
    populaiton_list = []
    for i in range(populaiton_size):
        new_member = []
        for j in range(n):
            new_member.append(rnd.randint(1, n))
        new_member.append(0)
        populaiton_list.append(new_member)
    return populaiton_list


def fitnees(population_list, n):
    i = 0
    lenght = len(population_list)
    conflict = 0
    while i < lenght:
        j = 0
        conflict = 0
        while j < n:
            l = j+1
            while l < n:
                if population_list[i][j] == population_list[i][l]:
                    conflict += 1
                if abs(j-l) == abs(population_list[i][j]-population_list[i][l]):
                    conflict += 1
                l += 1
            j += 1
        population_list[i][len(population_list[j])-1] = conflict
        i += 1
    return population_list


population = init_population(p_s, n)
population = fitnees(population, n)

for i in population:
    print(i)
