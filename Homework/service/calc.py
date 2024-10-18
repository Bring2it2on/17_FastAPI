

def simple_calcultor(type:str,num1:int,num2:int):
    if type == "+":
        return num1+num2
    elif type == "-":
        return num1-num2
    elif type == "*":
        return num1*num2
    elif type == "%":
        return num1%num2
    else:
        raise Exception("연산기호를 정확히 입력해주세요!")
    
def slicing_calcultor(type:str,num1:int,num2:int):
    maxNum = max(num1,num2)
    minNum = min(num1,num2)
    if type == "+":
        return sum(range(minNum, maxNum+1))
    elif type == "*":
        product = 1
        for i in range(minNum, maxNum + 1):
            product *= i
        return product
    else:
        raise Exception("연산기호를 정확히 입력해주세요!")
    
def draw_picture(select:str,word:str,count:int):
    if select == "증가":
        result = ""
        for i in range(count):
            result += f"{word * (i + 1)}\n" 
        return result.strip()  # 마지막에 불필요한 줄바꿈 제거
    elif select == "감소":
        result = ""
        for i in range(count):
            result += f"{word * (count-i)}\n" 
        return result.strip()
