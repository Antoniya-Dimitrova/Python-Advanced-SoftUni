string_expression = input().split()

result = []

for el in string_expression:

    if el == "+":
        if result:
            sum_elements = sum(result)
            result.clear()
            result.append(sum_elements)

    elif el == "-":
        if len(result) > 1:
            for i in range(len(result)-1):
                diff_elements = result[i] - result[(i+1)]
                result[i+1] = diff_elements
            for _ in range(len(result) - 1):
                result.pop(0)

    elif el == "*":
        if len(result) > 1:
            multiple_elements = 1
            for j in result:
                multiple_elements *= j
            result.clear()
            result.append(multiple_elements)

    elif el == "/":
        if len(result) > 1:
            for k in range(len(result)-1):
                div_elements = result[k] // result[(k+1)]
                result[k+1] = div_elements
            for _ in range(len(result)-1):
                result.pop(0)

    else:
        result.append(int(el))

print(*result)