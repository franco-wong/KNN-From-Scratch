from numpy import *
from seaborn import *

def CalculateSquaredError(initial_b, initial_m, points):
    points_length = len(points)
    sumOfError = 0

    for i in range(points_length):
        point_y = points[i][1]
        point_x = points[i][0]

        sumOfError += (point_y - ((initial_m * point_x) + initial_b)) ** 2

    return sumOfError / float(points_length)

def GradientDescent(eq_b, eq_m, learning_rate, points, iterations):
    b = eq_b
    m = eq_m

    for _ in range(iterations):
        [b, m] = GradientStep(b, m, learning_rate, array(points))
        
    return [b, m]

def GradientStep(eq_b, eq_m, learning_rate, points):
    points_length = len(points)

    gradient_b = 0
    gradient_m = 0

    for i in range(points_length):
        points_y = points[i][1]
        points_x = points[i][0]

        gradient_b += -(2/float(points_length)) * (points_y - ((eq_m * points_x) + eq_b))
        gradient_m += -(2/float(points_length)) * points_x * (points_y - ((eq_m * points_x) + eq_b))

    new_m = eq_m - (learning_rate * gradient_m)
    new_b = eq_b - (learning_rate * gradient_b)
    
    return [new_b, new_m]

def main():
    # read the data
    points = genfromtxt("data.csv", delimiter=",")
    # print("length of points is ",len(points))
    # initialize the hyperparameters
    learning_rate = 0.0001
    eq_b = 0
    eq_m = 0
    iterations = 1000

    # calculate the error for each point
    print("initial values: slope = {0}, y-intercept = {1}, error = {2}".format(eq_m, eq_b,CalculateSquaredError(eq_b, eq_m, points)))
    [eq_b, eq_m] = GradientDescent(eq_b, eq_m, learning_rate, points, iterations)
    print("end values: slope = {0}, y-intercept = {1}, error = {2}".format(eq_b, eq_m, CalculateSquaredError(eq_b, eq_m, points)))

    return

if __name__ == "__main__":
    main()
    pass