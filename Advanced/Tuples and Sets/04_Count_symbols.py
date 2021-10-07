text = input()

chars = {}

for chr in text:
    if chr not in chars:
        chars[chr] = 1
    else:
        chars[chr] += 1
chars_sorted = sorted(chars.items(), key=lambda x: x[0])

for key, value in chars_sorted:
    print(f"{key}: {value} time/s")