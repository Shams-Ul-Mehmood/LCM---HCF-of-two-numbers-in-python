def hcf( firstNumber , secondNumber ):
    if firstNumber > secondNumber:
        smaller = secondNumber
    else:
        smaller = firstNumber
    for value in range( 1 , smaller + 1 ):
        if firstNumber % value == 0 and secondNumber % value == 0:
            factor = value
    return factor

first_Number = int( input("Please enter first-number : ") )
second_Number = int( input("Please enter second-number : ") )
print( f"HCF of {first_Number} and {second_Number} is { hcf( first_Number , second_Number ) }" )