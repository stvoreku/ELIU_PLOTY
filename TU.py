import matplotlib
import matplotlib.pyplot as plt
import numpy as np
beta=6.7275*0.0001
Ut=1
Uds=[1, 2, 3, 4]
markers = ['o', 'v', 's', 'X', 'D']
def nnasyc(Ugs, Uds):
       return beta*((Ugs-Ut)*Uds-0.5*(Uds**2))*1000

def nasyc(Ugs):
       return beta*(0.5*(Ugs-Ut)**2)*1000
def gds(Ugs, Uds):
       return beta*(Ugs-Uds-Ut)
def gmNasyc(Ugs):
       return beta*(Ugs-Ut)
def gmnNasyc(Uds):
       return beta*Uds
fig, ax = plt.subplots()
plt.figure(1)
for i in range(0,4):
       diff = Uds[i] + Ut
       print(diff)

       Vt0 = np.arange(0.0, Ut, 0.01) #PONIZEJ PROGU
       V1 = np.arange(Ut, diff, 0.01) #OBSZAR NASYCENIA
       V2 = np.arange(diff, 5.01, 0.01) #OBSZAR NIENASYCENIA

       A_nasyc = nasyc(V1)
       A_nienasyc = nnasyc(V2, Uds[i])

       ax.plot(V2, nnasyc(V2, Uds[i]), "--")
       ax.plot(Vt0, Vt0*0, "r")

       end_point = (5, (np.amax(A_nienasyc)))
       print(end_point)
       plt.annotate("Uds =" + str(Uds[i]), end_point)
       if i == 3:
              ax.plot(V1, nasyc(V1), "red", marker=markers[3], markevery=10, markersize=5)

ax.set(xlabel='Napięcie [V]', ylabel='Prąd [mA]',
       title='Charakterystyki Przejściowe')
plt.annotate("Obszar podprogowy", (-0.25,0.5))
plt.annotate("Obszar nasycenia", (2.1,3))
plt.annotate("Obszar nienasycenia", (4.2,2.8))
ax.grid()


#teraz wyjściowe
colors = ["red", "blue", "green", "yellow"]
Ugs = [1,2,3,4]
fig2, ax2 = plt.subplots()
plt.figure(2)
for i in range(0,4):
       diff = Ugs[i] - Ut

       print(diff)

       V1 = np.arange(0.0, diff, 0.01) #OBSZAR NIENASYCENIA
       V2 = np.arange(diff, 5.01, 0.01) #OBSZAR NASYCENIA

       ax2.hlines(y=nasyc(Ugs[i]), xmin=diff, xmax=5, color= colors[i])
       A_nienasyc = nnasyc(Ugs[i], V1)
       ax2.plot(V1, A_nienasyc, "--", color=colors[i])

       end_point = (5, nasyc(Ugs[i]))
       print(end_point)
       plt.annotate("Ugs =" + str(Uds[i]), end_point)

ax2.set(xlabel='Napięcie [V]', ylabel='Prąd [mA]',
       title='Charakterystyki Wyjściowe')
ax2.grid()
plt.savefig("wyjsciowe2")


#gds (Ugs)
fig3, ax3 = plt.subplots()
plt.figure(3)
print("Gds (Ugs)")
for i in range(0,4):
       diff = Uds[i] + Ut
       print(diff)
       Vt0 = np.arange(0.0, diff, 0.01)  # OBSZAR NASYCENIA
       V2 = np.arange(diff, 5.01, 0.01)  # OBSZAR NIENASYCENIA
       print(Vt0, V2)
       A_nienasyc = gds(V2, Uds[i])

       ax3.plot(V2, gds(V2, Uds[i]), "--")
       ax3.plot(Vt0, Vt0 * 0, "r")

       end_point = (5, (np.amax(A_nienasyc)))
       print(end_point)
       plt.annotate("Uds =" + str(Uds[i]), end_point)
ax3.set(xlabel='Napięcie [V]', ylabel='Konduktancja wyjściowa')
ax3.grid()
plt.savefig("gdsUgs")
#gds (Uds)
fig4, ax4 = plt.subplots()
plt.figure(4)
for i in range(0,4):
       diff = Ugs[i] - Ut

       print(diff)

       V1 = np.arange(0.0, diff + 0.01, 0.01) #OBSZAR NIENASYCENIA
       V2 = np.arange(diff, 5.01, 0.01) #OBSZAR NASYCENIA

       ax4.hlines(y=0, xmin=diff, xmax=5, color= colors[i])
       A_nienasyc = gds(Ugs[i], V1)
       ax4.plot(V1, A_nienasyc, "--", color=colors[i])

       end_point = (0, np.amax(A_nienasyc))
       print(end_point)
       plt.annotate("Ugs =" + str(Uds[i]), end_point)

ax4.set(xlabel='Napięcie [V]', ylabel='Konduktancja wyjściowa')
ax4.grid()
plt.savefig("gdsUds")

fig5, ax5 = plt.subplots()
plt.figure(5)
print("Gm (Ugs)")
for i in range(0,4):
       diff = Uds[i] + Ut
       print(diff)
       Vt0 = np.arange(0.0, diff, 0.01)  # OBSZAR NASYCENIA
       V2 = np.arange(diff, 5.01, 0.01)  # OBSZAR NIENASYCENIA
       print(Vt0, V2)

       A_nasyc = gmNasyc(Vt0)

       ax5.hlines(y=gmnNasyc(Uds[i]), xmin=diff, xmax=5, color=colors[i])
       ax5.plot(Vt0, A_nasyc, "r--")

       end_point = (5, gmnNasyc(Ugs[i]))
       print(end_point)
       plt.annotate("Ugs =" + str(Uds[i]), end_point)

ax5.set(xlabel='Napięcie [V]', ylabel='Konduktancja przejściowa')
ax5.grid()
plt.savefig("Gm")
plt.show()


