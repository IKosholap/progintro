milimetrs = int(input("Delka [mm]:"))
sentimiters = milimetrs/10
metrs = sentimiters / 100
inches = milimetrs /25.4

print(f"{milimetrs} mm = {sentimiters} sm = {metrs:.3f} m = {inches:.3f} in")