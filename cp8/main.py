from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import figure
import networkx as nx


class GraphVisualizer(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initGraph()
        self.initLabel()
    
    def initUI(self):
        # Text Container
        self.inputFrame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[0, 0])
        self.inputFrame.place(relheight=1, relwidth=0.15)

        # Text
        self.editor = Text(self.inputFrame)
        self.editor.place(relheight=0.93, relwidth=1)
        # Enter button
        self.btn = ttk.Button(self.inputFrame, text="Enter", command=self.getGraph)
        self.btn.pack(side="bottom", fill=X)
    
    def initGraph(self):
        # Graph Container
        self.GraphFrame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[0, 0])
        self.GraphFrame.place(relheight=0.93, relwidth=0.85, relx=0.15)
        self.f = plt.figure(figsize=(5, 5))
        plt.axis('off')
        self.G = nx.Graph()
        self.G.add_edges_from([])
        self.pos = nx.circular_layout(self.G)
        nx.draw_networkx(self.G, pos=self.pos)
        self.canvas = FigureCanvasTkAgg(self.f, master=self.GraphFrame)
        self.canvas.get_tk_widget().pack(side="bottom", fill="both", expand=1)
    def initLabel(self):
        self.LabelFrame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[0, 0])
        self.LabelFrame.place(relheight=0.07, relwidth=0.85, relx=0.15, rely=0.93)
        self.label = ttk.Label(master=self.LabelFrame, text="Поиск максимального паросочетания в двудольном графе")
        self.label.pack(side="bottom", fill="both", expand=1)
    def changeLabel(self):
        self.LabelFrame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[0, 0])
        self.LabelFrame.place(relheight=0.07, relwidth=0.85, relx=0.15, rely=0.93)
        self.text = self.maxMatch()
        print(str(self.text))
        self.label = ttk.Label(master=self.LabelFrame, text=str(self.text))
        self.label.pack(side="bottom", fill="both", expand=1)

    def buildGraph(self):
        # Graph Container
        self.GraphFrame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[0, 0])
        self.GraphFrame.place(relheight=0.93, relwidth=0.85, relx=0.15)
        self.f = plt.figure(figsize=(5, 5))
        plt.axis('off')
        self.G = nx.Graph()
        self.G.add_edges_from(self.graph)
        self.pos = nx.circular_layout(self.G)
        nx.draw_networkx(self.G, pos=self.pos, edge_color=self.edgeColor(), width=3, node_color='black', node_size=1000, font_color='w')
        self.canvas = FigureCanvasTkAgg(self.f, master=self.GraphFrame)
        self.canvas.get_tk_widget().pack(side="bottom", fill="both", expand=1)
    
    def getGraph(self):
        self.graph = (self.editor.get("1.0", "end")).split('\n')[:-1]
        self.graph = list(filter(lambda a: a != '', self.graph))
        for i in range(len(self.graph)):
            self.graph[i] = list(map(int, list(filter(lambda a: a != '', self.graph[i].split(' ')))))
        self.buildGraph()
        self.changeLabel()

    def maxMatch(self):
        self.match = nx.bipartite.maximum_matching(self.G)
        self.match = [[key, value] for key, value in self.match.items()][:len(self.match) // 2]
        return self.match
    def edgeColor(self):
        #Find matching
        self.match = self.maxMatch()
        self.color_mass = []
        for i in range(len(self.graph)):
            if self.graph[i] in self.match:
                self.color_mass.append('r')
            else:
                self.color_mass.append('black')
        return self.color_mass

    


        


def main():
    root = Tk()
    root.title("GRAPH VISUALIZER")
    root.geometry("640x480")
    app = GraphVisualizer()

    root.mainloop()
    

if __name__ == "__main__":
    main()