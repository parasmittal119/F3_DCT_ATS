file_path = "AC001_Single_Socket (1).bin"

with open(file_path,'rb') as f:
    file_data = f.read()

print(file_data)