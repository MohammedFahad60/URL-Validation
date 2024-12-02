from graphviz import Digraph

def visualize_dfa():
    dfa = Digraph("DFA for URL Validation", format="png")
    
    # Define nodes
    dfa.attr(rankdir='LR')
    dfa.node("0", "Start")
    dfa.node("1", "Domain")
    dfa.node("2", "Path")
    
    # Define transitions
    dfa.edge("0", "1", label="http:// or https://")
    dfa.edge("1", "1", label="Alnum, -, .")
    dfa.edge("1", "2", label="/")
    dfa.edge("2", "2", label="Path characters")
    
    # Save and render
    dfa.render("output/dfa", view=True)

# Example Usage
if __name__ == "__main__":
    visualize_dfa()
