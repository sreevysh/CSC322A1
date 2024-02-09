from pprint import pp

test_sud = "163805070008040065005007008450082039301000040700000000839050000604200590000093081"

def convert_grid_to_val(i,j,num):
    return (81*(i-1))+(9*(j-1))+(num-1)+1

sat = ""

# print(len(test_sud))


for i in range(1,10):
    for j in range(1,10):
        if test_sud[((i-1)*9)+j-1] != "0":
            # print(test_sud[((i-1)*9)+j-1])
            sat += str(convert_grid_to_val(i,j,int(test_sud[((i-1)*9)+j-1]))) + " 0\n"


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

for j in range(1,10):
    for k in range(1,10):
        for i in range(1,9):
            for l in range(i+1,10):
                sat += str(-1*convert_grid_to_val(i,j,k))+" "+str(-1*convert_grid_to_val(l,j,k))+" 0\n"

for k in range(1,10):
    for a in range(0,3):
        for b in range(0,3):
            for u in range(1,4):
                for v in range(1,3):
                    for w in range(v+1,4):
                        sat += str(-1*convert_grid_to_val(((3*a)+u),((3*b)+v),k))+" "+str(-1*convert_grid_to_val(((3*a)+u),((3*b)+w),k))+" 0\n"

for k in range(1,10):
    for a in range(0,3):
        for b in range(0,3):
            for u in range(1,3):
                for v in range(1,4):
                    for w in range(u+1,4):
                        for t in range(1,4):
                            sat += str(-1*convert_grid_to_val(((3*a)+u),((3*b)+v),k))+" "+str(-1*convert_grid_to_val(((3*a)+w),((3*b)+t),k))+" 0\n"



pp(sat)
