"""
Draw local and global tracks from event JSON using matplotlib
"""

import json
import matplotlib.pyplot as plt


if __name__ == "__main__":
    with open("../examples/event_0.json") as f:
        event = json.load(f)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for track in event[0]:
        x1 = track['fParamFirst']['fX']
        y1 = track['fParamFirst']['fY']
        z1 = track['fParamFirst']['fZ']
        x2 = track['fParamLast']['fX']
        y2 = track['fParamLast']['fY']
        z2 = track['fParamLast']['fZ']
        ax.plot([x1, x2], [y1, y2], 'b', zs=[z1, z2])

    for track in event[1]:
        x1 = track['fParamFirst']['fX']
        y1 = track['fParamFirst']['fY']
        z1 = track['fParamFirst']['fZ']
        x2 = track['fParamLast']['fX']
        y2 = track['fParamLast']['fY']
        z2 = track['fParamLast']['fZ']
        ax.plot([x1, x2], [y1, y2], 'g', zs=[z1, z2])

    plt.show()
