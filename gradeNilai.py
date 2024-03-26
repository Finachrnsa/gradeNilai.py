grade = int(input("Berapa Score anda?"))

if grade >=90 and grade <=100:
    print("A - With Compliments")
elif grade >=80 and grade <=89:
    print("b - Very Satisfy")
elif grade >=70 and grade <=79:
    print("c - Satisfying")
elif grade >=60 and grade <=69:
    print("d - Not Satisfactory")
elif grade >=0 and grade <=59:
    print("e - Not PASS")
else:
    print("Eror")