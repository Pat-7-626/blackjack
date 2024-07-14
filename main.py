num = int(input())
count = 0
ace = False
ten = False
for i in range(num):
    text = list(str(input()))
    text.pop()
    text = "".join(text)
    if text.isnumeric():
        if text == "10":
            ten = True
        count += int(text)
    elif text in ["J", "Q", "K"]:
        ten = True
        count += 10
    elif text == "A":
        ace = True
        if count+11 > 21:
            count += 1
        else: count += 11
print("Blackjack") if ace is True and ten is True \
    else print("Bust") if count > 21 \
    else print(f"{count} points")