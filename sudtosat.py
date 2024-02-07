from pprint import pp

test_sud = "163805070008040065005007008450082039301000040700000000839050000604200590000093081"

def convert_grid_to_val(i,j,num):
    return (81*(i-1))+(9*(j-1))+(num-1)+1

sat = ""

for i in range(1,10):
    for j in range(1,10):
        literal = ""
        for num in range(1,10):
            literal += str(convert_grid_to_val(i,j,num)) + " "
        literal += "0"
        sat += literal + "\n"

for i in range(1,10):
    for k in range(1,10):
        for j in range(1,8):
            for l in range(i+1,10):
                sat += str(-1*convert_grid_to_val(i,j,k))+" "+str(-1*convert_grid_to_val(i,l,k))+" 0\n"

pp(sat)
