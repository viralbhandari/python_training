planets=[['mercury','venus','earth'],['mars','jupiter','saturn'],['uranus','neptune','pluto']]
flatten_planets=[val for sublist in planets for val in sublist if len(planets)<6]
print(flatten_planets)
