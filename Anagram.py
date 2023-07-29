a="listen"
b="silent"
sorted_a=sorted(a)
sorted_b=sorted(b)
is_anagram=sorted_a==sorted_b
if is_anagram:
    print("yes,its anagram")
else:
    print("its,not anagram")