file_path = 'knowit_2023_kalender\Klikk klikk klakk\log.txt'

dict = {}
amount = 0

def fill_list():
    for i in range(1,8):
        dict.update({i : 0})

try:
    with open(file_path, 'r') as file:
        
        file_content = file.read()
        elements_list = file_content.split(',')
            
        for string in elements_list:
            
            if string[-1] == ' ':
                continue
            number = int(string[-1])
            
            if not dict:
                amount += 1
                fill_list()
            if "klakk" in string and number not in dict:
                dict.update({number : 0})
            if "klikk" in string and number in dict:
                 dict.pop(number)
        
except FileNotFoundError:
    print("The specified file was not found.")
    
print(amount)
        
         
        
        
        
        

