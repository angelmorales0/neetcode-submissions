class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op_num = 0
        for num_index in range (len(tokens)):
            if tokens[num_index].replace("-","").isnumeric():
                stack.append(tokens[num_index])
            else: #it must be an operation 
                if tokens[num_index] == "+":
                    op_num = int(stack[-2]) + int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(op_num)
                elif tokens[num_index] == "-":
                    op_num = int(stack[-2]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(op_num)
                elif tokens[num_index] == "*":
                    op_num = int(stack[-2]) * int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(op_num)
                elif tokens[num_index] == "/":
                    op_num = int(stack[-2] )/int( stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(op_num)
        return int(stack[0])
