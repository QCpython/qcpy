import matplotlib.pyplot as plt

# ScalerMappable is needed for creating the color bar on the State Vector
# visualization


def graph(_text, _background, num_qubits):
    plt.clf()
    plt.close()
    # sets up bar graph and colors that map to a qubits phase angle
    fig, ax = plt.subplots(figsize=(num_qubits + 3, num_qubits + 3))
    # sets up tick labels
    plt.setp(ax.get_xticklabels(), rotation=75, ha="right", color=_text)
    plt.setp(ax.get_yticklabels(), color=_text)
    # cleans outline of bargraph so it's open to the top and right
    ax.spines["bottom"].set_color(_text)
    ax.spines["top"].set_color(_background)
    ax.spines["right"].set_color(_background)
    ax.spines["left"].set_color(_text)
    # sets up tick parameters
    ax.tick_params(axis="x", colors=_text)
    ax.tick_params(axis="y", colors=_text)
    # sets backgorund color
    ax.set_facecolor(_background)
    fig.patch.set_facecolor(_background)
    return ax
