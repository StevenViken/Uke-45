from matplotlib import pyplot

# Liste med dyr
x = ["katt", "hund","fugl","andre dyr","ingen dyr"]
# Input av hvor mange av hvert dyr du skal ha
y = [int(input("katter: ")), int(input("hunder: ")),int(input("fugler: ")),int(input("andre dyr: ")),int(input("ingen dyr: "))]
# Lager diagrammet
pyplot.bar(x,y)
# Hviser diagrammet
pyplot.show()