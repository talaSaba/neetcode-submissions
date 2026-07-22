class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        i=0
        count=0
        while i<len(tokens):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
                #count+=1
                i+=1
            elif tokens[i]=="+" and len(stack)>=2:
                number1=stack.pop()
                number2=stack.pop()
                result=number1+number2
                stack.append(result)
                count+=1
                i+=1
            elif tokens[i]=="-" and len(stack)>=2:
                number1=stack.pop()
                number2=stack.pop()
                result=number2-number1
                stack.append(result)
                count+=1
                i+=1
            elif tokens[i]=="*" and len(stack)>=2:
                number1=stack.pop()
                number2=stack.pop()
                result=number1*number2
                stack.append(int(result))
                count+=1
                i+=1
            elif tokens[i]=="/" and len(stack)>=2:
                number1=stack.pop()
                number2=stack.pop()
                result=number2/number1
                stack.append(int(result))
                count+=1
                i+=1

        return stack[-1]


            
        
        