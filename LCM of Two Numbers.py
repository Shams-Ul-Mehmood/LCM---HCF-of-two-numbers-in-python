def lcm( firstValue , secondValue ):
    if( firstValue > secondValue ):
        greater = firstValue
    else:
        greater = secondValue
    while True:
        if( ( greater % firstValue == 0 ) and ( greater % secondValue == 0 ) ):
            break
        greater += 1
    return greater

first_Value = int( input("Please enter first-value : ") )
second_Value = int( input('Please enter second-value : ') )
print( "LCM of ",first_Value," and ",second_Value," is ",lcm( first_Value , second_Value ) )