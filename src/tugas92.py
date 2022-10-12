kata1 = "Alur"
kata2 = "Ular"

kata1 = kata1.lower()
kata2 = kata2.lower()

if(len(kata1) == len(kata2)):

    sorted_str1 = sorted(kata1)
    sorted_str2 = sorted(kata2)

    if(sorted_str1 == sorted_str2):
        print(kata1 + " dan " + kata2 + " merupakan anagram.")
    else:
        print(kata1 + " and " + kata2 + " tidak anagram.")

else:
    print(kata1 + " and " + kata2 + " tidak anagram.")