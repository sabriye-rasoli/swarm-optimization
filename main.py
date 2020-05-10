import pso_simulation as pso_sim
import cso_simulation as cso_sim

def main():
    userInput = int(input('1-particle swarm optimization simulation\n2-cat swarm optimization\n'))
    if userInput == 1:
        pso_sim.main()
    elif userInput == 2:
        cso_sim.main()

if __name__ == '__main__':
    main()
