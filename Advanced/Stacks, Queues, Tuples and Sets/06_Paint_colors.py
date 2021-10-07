colors = ["red", "blue", "yellow", "orange", "green", "purple"]
text = [i for i in input().split()]

found_colors = []
while text:
    if len(text) > 1:
        left = text[0]
        right = text[-1]
        if left + right in colors:
            found_colors.append(left + right)
            text.pop()
            text.pop(0)
        elif right + left in colors:
            found_colors.append(right + left)
            text.pop()
            text.pop(0)
        else:
            left = left[:-1]
            right = right[: -1]
            text.pop()
            text.pop(0)

            index = int(len(text) // 2)
            if right:
                text.insert(index, right)
            if left:
                text.insert(index, left)

            if len(text) == 1:
                if text[0] in found_colors and text[0] not in colors:
                    colors.append(text[0])

    else:
        if text[0] in colors:
            found_colors.append(text[0])
        text.pop()
        break

for color in found_colors:
    if color == "orange":
        if "red" not in found_colors or "yellow" not in found_colors:
            found_colors.remove(color)
        elif color == "green":
            if "blue" not in found_colors or "yellow" not in found_colors:
                found_colors.remove(color)
        elif color == "purple":
            if "red" not in found_colors or "blue" not in found_colors:
                found_colors.remove(color)
print(found_colors)
