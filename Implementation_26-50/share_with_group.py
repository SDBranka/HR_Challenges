def kaprekarNumbers(p, q):
    answer = []
    
    # ######need to slice the list
    for i in range(p, q+1):
    #     # print(f"i: {i}")
        if i < 4:
            if i == 1:
                # print("is 1")
                answer.append(i)
        else:
    #     d = len(str(i))
            print(f"i: {i}")
            i_squared_str = str(i**2)
            a = int(i_squared_str[:len(i_squared_str)//2])
            # print(f"a: {a}")
            b = int(i_squared_str[len(i_squared_str)//2:])
            # print(f"b: {b}")
            if a + b == i:
                answer.append(i)

    #     n = len(i_squared_str)
        # # a works but b does not
        # a = int("".join(i_squared_str[:n-d]))
        # b = int("".join(i_squared_str[n-d:]))
        # a = int(i_squared_str[:n//2]) #why doesn't this work?
        # loop_multiplier = 1
        # a = 0
        # for i in range(n//2, 0, -1):
        #     if i_squared_str[i] != "0":
        #         a += int(i_squared_str[i]) * loop_multiplier
        #     loop_multiplier *= 10
        # # a = int(a)
        # b = int(i_squared_str[n//2:])
        

        # print(f"a: {a}")
        # print(f"a type: {type(a)}")
        # print(f"b: {b}")


    # print(f"x: {x}")
    # s = "string"
    # s1 = s[:len(s)//2]
    # s2 = s[len(s)//2:]
    # print(s1,s2)
    # a = int(i_squared_str[:len(i_squared_str)//2])
    # b = int(i_squared_str[len(i_squared_str)//2:])
    # print(f"a: {a}")
    # print(f"b: {b}")

    return answer


p = 1
q = 45
print(kaprekarNumbers(p, q))