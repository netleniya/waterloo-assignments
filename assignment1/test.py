import plotly.graph_objects as go
s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'


# def count_letters(dna_string):
#     letters = set(dna_string)
#     return {i: s.count(i) for i in letters}


# l_dict = count_letters(s)
# print(l_dict)

def allIn(first_corner=(0, 0), second_corner=(0, 0), *point_list):

    if not point_list:
        return False

    x1, y1 = first_corner
    x2, y2 = second_corner

    truth_table = []
    for point in point_list:
        p1, p2 = point
        if ((x1 <= p1 <= x2) and (y1 <= p2 <= y2)) and (x1 < x2):
            truth_table.append(True)
        elif ((x2 <= p1 <= x1) and (y2 <= p2 <= y1) or (y2 >= p2 >= y1)) and (x1 > x2):
            truth_table.append(True)
        else:
            truth_table.append(False)

    return all(truth_table)


# print(allIn((0, 0), (5, 5), *[(1, 1), (0, 0), (5, 5)]))
# print(allIn((0, 0), (5, 5), *[(1, 1), (0, 0), (5, 6)]))
# print(allIn((0, 0), (5, 5), *[(1, 1), (2, 2)]))

# print(allIn((0, 0), (5, 5), *[(6, 6), (0, 0), (5, 5)]))
# print(allIn((0, 0), (5, 5), *[]))
# print(allIn((0, 0), (5, 5), *[(1, 1)]))
# print(allIn((5, 0), (0, 5), *[(1, 0)]))


fig = go.Figure()

fig.add_shape(type="rect", x0=0, y0=0, x1=5, y1=5, line=dict(
    color='Red', width=2), fillcolor='rgba(255, 0, 0, 0.1)')

fig.add_trace(go.Scatter(
    x=[0, 1, 5, 5], y=[0, 1, 3, 6],
    text=["(0,0)", "(1,1)", "(5,3)", "(5,6)"],
    textposition="top right",
    mode='markers+text', marker=dict(color="Red", size=8),
    showlegend=False,
    name="(x1,y1) < (x2,y2)"))


fig.add_shape(type="rect", x0=0, y0=0, x1=-5, y1=-5,
              line=dict(color='Green', width=2), fillcolor='rgba(26, 150, 65, 0.1)')

fig.add_trace(go.Scatter(
    x=[-1, 2, -3, -5], y=[-1, -2, -6, -3],
    text=["(-1,-1)", "(2,-2)", "(-3,-6)", "(-5,-3)"],
    textposition="bottom left",
    mode='markers+text', marker=dict(color="Green", size=8),
    showlegend=False,
    name="(x1,y1) > (x2,y2)"))

fig.add_shape(type="rect", x0=-2, y0=2, x1=-6, y1=6,
              line=dict(color='#0D7AE6', width=2), fillcolor='rgba(13, 122, 230, 0.1)')

fig.add_trace(go.Scatter(
    x=[-2, -5, -4, -1], y=[2, 4, 6, 4],
    text=["(-2,2)", "(-5,4)", "(-4,6)", "(-1,4)"],
    textposition="top left",
    mode='markers+text', marker=dict(color="#0D7AE6", size=8),
    showlegend=False,
    name="(x1 > x2);(y1 < y2)"))

fig.add_shape(type="rect", x0=4, y0=-1, x1=8, y1=-8,
              line=dict(color='#FFCC00', width=2), fillcolor='rgba(255, 204, 0, 0.1)')

fig.add_trace(go.Scatter(
    x=[4, 5, 8, 9], y=[-1, -5, -5, -9],
    text=["(4,-1)", "(5,-5)", "(8,-5)", "(9,-9)"],
    textposition="bottom right",
    mode='markers+text', marker=dict(color="#FFCC00", size=8),
    showlegend=False,
    name="(x1 < x2);(y1 > y2)"))

fig.update_traces()

fig.update_xaxes(range=[-12, 12])
fig.update_yaxes(range=[-12, 12])

fig.update_layout(
    title="Question 3: is a data point within a rectangle",
    autosize=True,
    width=600,
    height=600,
    legend_title="rectangle:")
fig.show()
