# Goal: Create a simple Python script to represent the basic structure of a neuron using text-based visualization

class Neuron:
    def __init__(self, name):
        self.name = name
        self.dendrites = [] # receive electricity from other neurons
        self.axon = None # transmits electicity away from the soma
        self.axon_terminals = [] # connect to other neurons

    def add_dendrite(self, dendrite):
        self.dendrites.append(dendrite) # add a dendrite to the neuron

    def set_axon(self, axon):
        self.axon = axon # set the axon of the neuron

    def add_axon_terminal(self, terminal):
        self.axon_terminals.append(terminal) # add an axon terminal to the neuron

    def display_structure(self):
        print(f"Neuron: {self.name}")
        print("Dendrites:")
        for dendrite in self.dendrites:
            print(f" - {dendrite}")
        print(f"Axon: {self.axon}")
        print("Axon Terminals:")
        for terminal in self.axon_terminals:
            print(f" - {terminal}")

# Create a neuron
neuron = Neuron("Motor Neuron")
neuron.add_dendrite("Dendrite 1")
neuron.add_dendrite("Dendrite 2")
neuron.set_axon("Axon")
neuron.add_axon_terminal("Terminal 1")
neuron.add_axon_terminal("Terminal 2")

# Display the structure of the neuron
neuron.display_structure()