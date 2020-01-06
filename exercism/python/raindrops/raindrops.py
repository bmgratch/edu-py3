def convert(number):
    drop = ""
    if number % 3 == 0:
        drop += 'Pling'
    if number % 5 == 0:
        drop += 'Plang'
    if number % 7 == 0:
        drop += 'Plong'
    if drop == "":
        drop = str(number)
    return(drop)
