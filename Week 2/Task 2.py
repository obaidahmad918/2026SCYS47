sentence = input("Enter a sentence: ")
vowel_list = "aeiouAEIOU"
v_count = 0
c_count = 0
for ch in sentence:
    if ch in vowel_list:
        v_count += 1
    else:
        c_count += 1
print("Number of vowels in the sentence is: ", v_count)
print("Number of consonants in the sentence is: ", c_count)
