b = 80  # pris for en billett barn(6-12 år)
u = 100 # pris for en billett ungdom(13-17 år)
veldigBraTilbud = 110 # pris for en billett ung voksen(18-25 år)
v = 120 # pris for en billett voksen
g = 0   # under 6 år er gratis
alder = int(input("Tast inn alder: "))
# Sjekker hva alderen er og setter riktig pris
if alder <= 5:
  pris = g
elif alder > 5 and alder < 13: 
  pris = b
elif alder > 12 and alder < 18:
  pris = u
elif alder > 17 and alder < 26:
    pris = veldigBraTilbud
else:
  pris = v
print("Prisen blir", pris, "kroner. ")
