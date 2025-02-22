def convert_exercise_points(ep: int):
    work = 0
    
    if ep > 0 and ep < 20:
        work = 1
    elif ep > 19 and ep < 30:
        work = 2
    elif ep > 29 and ep < 40:
        work = 3
    elif ep > 39 and ep < 50:
        work = 4
    elif ep > 49 and ep < 60:
        work = 5
    elif ep > 59 and ep < 70:
        work = 6
    elif ep > 69 and ep < 80:
        work = 7
    elif ep > 79 and ep < 90:
        work = 8
    elif ep > 89 and ep < 100:
        work = 9
    elif ep == 100:
        work = 10
    return work
def print_out_work():
    average, passperc, grades = get_all_inputs()
    start = 5
    print("Statistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {passperc:.1f}")
    print("Grade distribution:")
    for blah in range(len(grades)):
        stars = "*" * grades[blah]
        print(f"{"":<5}{start}: {stars}")
        start -= 1

    

def grade(z, q):
    l1 = [0, 0, 0, 0, 0, 0]
    totes = z + q
    
    if totes > 27:
        l1[0] += 1
    elif totes > 23 and totes < 28:
        l1[1] += 1
    elif totes > 20 and totes < 24:
        l1[2] += 1
    elif totes > 17 and totes < 21:
        l1[3] += 1
    elif totes > 14 and totes < 18:
        l1[4] += 1
    elif totes < 14:
        l1[5] += 1
    return l1

def get_all_inputs():
    p = 0
    total = 0
    number_of_inputs = 0
    thouw = [0, 0, 0, 0, 0, 0]
    while True:
        inputs = input("Exam points and exercise points: ")
        if inputs == '':
            break
        number_of_inputs += 1
        x, y = inputs.split()
        a = int(x)
        b = int(y)
        cep = convert_exercise_points(b)
        total += (a + cep)
        g = grade(a, cep)
        if a + cep > 14:
            p += 1
        average = total / number_of_inputs
        pass_perc = p / number_of_inputs * 100
        thouw = [thouw[i] + g[i] for i in range(len(thouw))]
    
    l_of_ia = [average, pass_perc, thouw]
    return l_of_ia
    

def main():
    print_out_work()



main()