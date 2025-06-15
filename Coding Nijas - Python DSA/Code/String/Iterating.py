s = "Hello World"
count = 0
# for letter in s:
#     if letter == "l":
#         count = count+1
# print(count)
# other form of code
for i in range(len(s)):
    if s[i] == "l":
        count += 1
print(count)
# to check if string present or not:-
if "Hel" not in s:
    print("Hello")
else:
    print("Not")

# if "Hel" in s:
#     print("Hello")
# else:
#     print("Not")
