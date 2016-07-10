'''
Generate fake data based on fixed ability levels (1 dimension) and paramters to
test changes
'''

import numpy as np

def main():
    num_students = 50
    num_exercises = 10
    num_examples = 500

    mu, sigma = 0, 1
    abilities = np.random.normal(mu, sigma, num_students)
    bias = np.random.normal(0, 2, num_exercises)
    weight = 5*np.random.random(num_exercises)
    params = [(bias[i], weight[i]) for i in xrange(num_exercises)]

    with open ("fake_data_1_true_params.txt", 'w') as f:
        for a in abilities:
            f.write(str(a) + "\n")
        for b, w in zip(bias, weight):
            f.write(str(b) + "\t" + str(w) + "\n")

    with open("fake_data_1", 'w') as f:
        for i in xrange(num_students):
            for j in xrange(num_exercises):
                f.write("student_" + str(i))
                f.write(",")
                f.write("exercise_" + str(j))
                f.write(",")
                f.write("1") #Time taken, always 1
                f.write(",")

                p = 1 / (1 +  np.exp(-(bias[j] + weight[j]*abilities[i])))
                if np.random.random() < p:
                    f.write("True")
                else:
                    f.write("False")
                f.write("\n")

if __name__ == "__main__":
    main()
