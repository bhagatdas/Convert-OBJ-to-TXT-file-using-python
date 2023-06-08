import os

folder_path = os.path.realpath(os.path.dirname(__file__))
files = list(os.listdir(folder_path))

input_data = ''

for i in range(len(files)):
    if  files[i][-4:] == '.obj':
        input_data = files[i]
        break
if input_data == '':
    print('Please add .obj file!!!')
    quit()


# set the path to the input OBJ file
input_path = os.path.join(folder_path,input_data)

# set the path to the output TXT file
output_path = os.path.join(folder_path,input_data[:-4]+'.txt')

# convert the OBJ file to TXT format and save to system
with open(input_path, "r") as obj_file:
    with open(output_path, "w") as txt_file:
        for line in obj_file:
            if line.startswith("v "):  # check for vertex lines
                vertex = line.split()[1:]
                txt_file.write(" ".join(vertex) + "\n")  # write vertex coordinates to txt file

print(f"Conversion complete. The output file has been saved to {output_path}.")


