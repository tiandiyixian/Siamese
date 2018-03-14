from matplotlib import pyplot as plt
import numpy as np
import matplotlib

# Index time plot

methods = [22, 50, 178, 423, 1723, 6601, 28030, 111190, 442403, 1771183, 4870113]
nicad_methods = [22, 50, 178, 423, 1723, 6601, 28030, 111190]
iclones_methods = [22, 50, 178, 1723, 6601, 28030]
jplag_methods = [22, 50, 178, 423, 1723, 6601, 28030]
simian_methods = [22, 50, 178, 423, 1723, 6601, 28030]
deckard_methods = [22, 50, 178, 423, 1723, 6601, 28030, 111190]

siamese = [4.13, 2.95, 4.62, 8.4, 11.94,
           36.22, 172.90, 614.90, 2077.04, 9089,
           23606]
scc = [(0.58 + 2.03), (0.88 + 0.68), (2.68 + 0.98), (3.81 + 1.37), (9.18 + 2.15),
       (28.40 + 4.96), (110.09 + 16.78), (432.52 + 60.96), (1694.23 + 219.8), (6786 + 870.08),
       (18606 + 2348.9)]
nicad = [0.34, 0.66, 2.21, 7.89, 26.50,
         84.25, 574.91, 6992]
iclones = [0.59, 0.67, 3.06, 4.82, 14.97, 166.95]
jpag = [0.37, 0.91, 0.89, 1.02, 3.83, 57.92, 890.08]
simian = [0.25, 0.30, 0.47, 2.14, 25.90, 401.93, 6506]
deckard = [1.57, 3.59, 8.26, 18.05, 119.77, 1152.13, 462.07, 124528.96]

# # seconds
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(methods, siamese, c="b", marker="s", label="Siamese")
# ax.plot(methods, scc, c="r", marker="x", label="SourcererCC")
# ax.plot(methods, nicad, c="g", marker="o", label="NiCad")
# plt.yscale('log', basey=10)
# plt.xscale('log', basex=10)
# plt.xlabel("No. of methods")
# plt.ylabel("Indexing time (s)")
# plt.ylim(ymax=100000)
# plt.legend(loc=2)
# plt.show()
#
# fig = ax.get_figure()
# fig.savefig('index.pdf', bbox_inches='tight')

# minutes
siamese_m = [x / 60 for x in siamese]
scc_m = [x / 60 for x in scc]
nicad_m = [x / 60 for x in nicad]
iclones_m = [x / 60 for x in iclones]
jplag_m = [x / 60 for x in jpag]
simian_m = [x / 60 for x in simian]
deckard_m = [x / 60 for x in deckard]

fig = plt.figure()
# ax = fig.add_subplot(111)
plt.plot(methods, siamese_m, c="b", marker="s", label="Siamese")
plt.plot(methods, scc_m, c="r", marker="x", label="SourcererCC")
plt.plot(nicad_methods, nicad_m, c="g", marker="o", label="NiCad")
plt.plot(iclones_methods, iclones_m, c="c", marker="v", label="iClones")
plt.plot(jplag_methods, jplag_m, c="m", marker="^", label="JPlag")
plt.plot(simian_methods, simian_m, c="y", marker="<", label="Simian")
plt.plot(deckard_methods, deckard_m, c="k", marker=">", label="Deckard")
plt.yscale('log', basey=10)
plt.xscale('log', basex=10)
plt.xlabel("No. of methods")
plt.ylabel("Indexing time (m)")
plt.ylim(ymax=1000)
plt.legend(loc=2)
# plt.show()
# fig = ax.get_figure()
plt.savefig('../index_m.pdf', bbox_inches='tight')


# # Query time plot
#
# methods = [22, 50, 178, 423, 1723, 6601, 28030, 111190, 442403, 1771183, 4870113]
# # siamese = [1.539, 1.5405, 1.5526, 1.5244, 1.5818, 1.6382, 1.71, 1.8626, 1.9711, 2.3409, 3.30]
# siamese = [1.7092, 1.6788, 1.8617, 1.7484, 1.7917, 1.8277, 1.7641, 2.0179, 2.2878, 2.7482, 2.9614]
# scc = [1.3006, 1.3773, 1.3937, 1.3412, 1.4536, 1.4913, 2.0718, 3.3621, 9.2613, 28.3169, 60.9813]
# scc_m = [x + 0.2354 for x in scc] # add avg tokenisation time
#
# print(scc_m)
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(methods, siamese, c="b", marker="s", label="Siamese")
# ax.plot(methods, scc_m, c="r", marker="x", label="SourcererCC")
# plt.yscale('log', basey=10)
# plt.xscale('log', basex=10)
# plt.ylim(ymax=100)
# plt.xlabel("No. of methods in the index")
# plt.ylabel("Average query response time (s)")
# plt.legend(loc=2)
# plt.show()
#
# fig = ax.get_figure()
# fig.savefig('query.pdf', bbox_inches='tight')