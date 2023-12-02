file_path = input("path to log.txt: ")

def count_elements_in_file(file_path, delimiter=','):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            elements_list = file_content.split(delimiter)
            list = []
            for string in elements_list:
                if string[-1] == ' ':
                    continue
                number = int(string[-1])
                if "klakk" in string:
                   list.append([True, number])
                else:
                   list.append([False, number])
            return list
        
    except FileNotFoundError:
        print("The specified file was not found.")
        return []

list = count_elements_in_file(file_path)

dict = {}
amount = 0

def fill_list():
    for i in range(1,8):
        dict.update({i : 0})

for i, sublist in enumerate(list):
    klakk, number = sublist
    if number in dict and not klakk:
        dict.pop(number)
    if number not in dict and klakk:
        dict.update({number : 0})
    if not dict:
        amount += 1
        fill_list()

print(amount)
        
         
        
        
        
        

