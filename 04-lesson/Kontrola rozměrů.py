diameters = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]

current_id =1
spatny = 0
for diametr in diameters:
    pochyb = round(diametr - 25, 2) 
    
    if pochyb > 0.05 :
        print(f"{current_id}: {diametr} mm VELKÝ")
        spatny = spatny +1
    elif pochyb< -0.05 :
        print(f"{current_id}: {diametr} mm MALÝ")
        spatny = spatny +1
    else:
        print(f"{current_id}: {diametr} mm OK")
    current_id +=1

print(f"Zmetků: {spatny} z {len(diameters)} ({spatny/len(diameters)*100} %)")


