import os

col_folder = "HPC_columnwise/"
col_add_folder = "HPC_col_add/"
result_folder = "HPC_result/"

def get_place_index(col_folder):
    index = []
    for root,dirs,files in os.walk(col_folder):
        for file in files:
            with open(root+file) as fr:
                for line in fr.readlines()[1:]:
                    index.append(line.split("\t")[0])
            return index

place_index = get_place_index(col_folder)
for index in range(len(place_index)):
    result_file = result_folder+place_index[index]+".txt"
    with open(result_file,'w') as res_file:
        res_file.write("Place\tP\tT\tL\tV\tx_N2\tx_O2\tx_Ar\ty_N2\ty_O2\ty_Ar\tLiqEtlp\tLiqRho\tLiqMass\tVapEtlp\tVapRho\tVapMass\n")
        for root,dirs,files in os.walk(col_folder):
            for file in files:
                with open(col_folder+file) as fr:
                    for line in fr.readlines()[index+1:index+2]:
                        line_split = line.split("\t")
                        for cell in line_split[0:-1]:
                            res_file.write(cell+"\t")
                        res_file.write(line_split[-1].replace("\n","\t"))
                with open(col_add_folder+file.replace(".txt","Add.txt")) as fr:
                    for line in fr.readlines()[index + 1:index+2]:
                        line_split = line.split("\t")
                        first_flag = True
                        for cell in line_split[1:]:
                            if first_flag:
                                first_flag=False
                                res_file.write(cell)
                            else:
                                res_file.write("\t"+cell)


