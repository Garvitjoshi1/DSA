a = "Garvit" == "Garvit"
print(a)
a = "Garvit" >= "Rarvit"
print(a)
a = "Garvit" >= "Gbrvit"
print(a)
# false in above both because it compares each alphabet ascii value.
a = "garvit" >= "Garvit"
print(a)
# True because small character have greater ascii values.
a = "gar" >= "garvit"
print(a)
# False because first element length is smaller
a = "Garvit" != "Garvit"
print(a)
# False because they are same.
