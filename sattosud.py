import fileinput


# def convert_grid_to_val(i,j,num):
#     return (81*(i-1))+(9*(j-1))+(num-1)+1

def convert_val_to_grid(num):
    num = abs(int(num))
    i = int(num / 81)
    j = int(num / 9)
    val = num % 9
    return (i,j,val)

sat = ""
for line in fileinput.input():
    sat += line
sat = sat.split(" ")

sud = ""
for clause in sat:
    try:
        c = int(clause)
        if c >= 0:
            sud += str(convert_val_to_grid(int(clause))[2])
    except ValueError:
        pass

print(sud)