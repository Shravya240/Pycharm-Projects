quiz = {
        "Argentina" : {"answer" : "A" , "options" : ["A. Buenos Aires",  "B. Lagos" , "C. Abuja" ,  "D. Delta" ] },
        "Australia":  {"answer" : "B" , "options" : ["A. Buenos Aires",  "B. Canberra",  "C. Moscow",  "D. Berlin"]},
        "Canada" :    {"answer" : "A" , "options" : ["A. Ottawa" , "B. Madrid",  "C. Canberra" , "D. Berlin" ] }
}


def main():
    score = 0
    quesnum=0
    for question in quiz:     # Outer Loops
        quesnum = quesnum + 1
        print("Ques", quesnum, ". What is Capital of ", question, "?")
        # print("Show:" , quiz[question]["options"])

        for options in quiz[question]["options"]:  # Inner Loops
            print(options)

        ans = input("Enter (A, B, C, D): ")

        # print("Ans:" , ans)
        # print("Comp  ans :", quiz[question]["answer"])

        if (ans == quiz[question]["answer"]):
            score = score + 1
            print("Great Job!!!")
        else:
            print("Oops Wrong!!! Correct Answer is Option", quiz[question]["answer"])

        print("\nTotal Score you got", score, "out of", len(quiz))


main()