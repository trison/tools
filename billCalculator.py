from __future__ import division

def divideByFour(num):
	return num / 4

print "Welcome to Trison's Bill Calculator 5000"

hydro = float((input("Enter the Hydro amount: $")))
internet = float((input("Enter the Shaw amount: $")))

topFloor = float(hydro) * (2/3)
bottomFloor = float(hydro) * (1/3)

print "\nThe top floor's 2/3 is $%.3f" % topFloor
print "The bottom floor's 1/3 is $%.3f" % bottomFloor

print "\nOur breakdown:"
print "The Shaw bill is $%.3f" % internet

hydroEach = divideByFour(hydro)
internetEach = divideByFour(internet)

print "\nThe hydro each is $%.3f" % hydroEach
print "The internet each is $%.3f" % internetEach

totalEach = hydroEach + internetEach
print "\nThe total each is $%.3f" % totalEach
