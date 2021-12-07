inp = "16,1,2,0,4,2,7,1,2,14"
print(min(sum([int((abs(bip - x)*(abs(bip - x)+1))/2) for x in [int(x) for x in inp.split(",")]]) for bip in range(len([int(x) for x in inp.split(",")]))))

# excuse the distasteful solution, i am in finals
