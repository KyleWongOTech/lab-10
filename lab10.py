# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first): Go through each element in the array, because we
    #know that every element is either an intger or a operator we add all intgers to a secondary
    #list. if the next option is an operator we do that operator with the integers in the list
    #
    #   ...
    temp:list[int] = []
    temp1 = 0
    temp2 = 0
    value= 0
    for i in range(len(tokens)):
        if tokens[i] not in "+-/*":
            temp.append(int(tokens[i]))
        else:
            match tokens[i]:
                case '+':
                    temp1=temp.pop(-1)
                    temp2=temp.pop(-1)
                    value = temp2+temp1
                    temp.append(value)
                case '-':
                    temp1=temp.pop(-1)
                    temp2=temp.pop(-1)
                    value = temp2-temp1
                    temp.append(value)
                case '*':
                    temp1=temp.pop(-1)
                    temp2=temp.pop(-1)
                    value = temp2*temp1
                    temp.append(value)
                case '/':
                    temp1=temp.pop(-1)
                    temp2=temp.pop(-1)
                    value = int(temp2/temp1)
                    temp.append(value)


    return int(value)


def decode_string(s):
    # Outline: you serach through the string and 
    #   ...
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    stack = []
    num:int
    myStr:str

    for temp in s:
        if temp!=']':
            stack.append(temp)

        else:
            myStr=""
            while stack and stack[-1]!='[':
                myStr=stack.pop()+myStr
            stack.pop()
            num=int(stack.pop())
            stack.append(myStr*num)

    myStr=""
    for char in stack:
        myStr += char

    return myStr





    pass


def daily_temperatures(temps):
    # Outline: create a stack of the numbers that have not been added yet, then
    #you peek at the top of the stack and if its less then next number you add the
    #length of the list to a new list containting the days waiting, if its not then
    #you loop through all elements of the list ahaed of your current index
    #if any of them are greater you return the length of the stack + the index you
    #searched through minus the originial index of your loop
    #   ...

    stacks = []
    my_list = []

    for i in range(len(temps)):
        if stacks:
            if stacks[-1]<temps[i]:
                my_list.append(len(stacks))
                stacks.pop()
            else:
                for j in range(i,len(temps)):
                    if stacks[-1]<temps[j]:
                        my_list.append(len(stacks)+j-i)
                        stacks.pop()
                        break

        stacks.append(temps[i])


    while stacks:
        my_list.append(0)
        stacks.pop()

    return my_list


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    print( decode_string("3[a]2[bc]") ) # "aaabcbc"
    pass


if __name__ == "__main__":
    main()
