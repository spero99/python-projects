#p17095/input arabic number output latin number

selected_num =int(input("select your number from 1-3999:"))
xiliada=selected_num //1000
ekatontada=selected_num % 1000 // 100
dekada =selected_num % 100 //10
monada =selected_num % 10
#confirm the input number is corrrect

if  selected_num<1 :
    print ("learn to read ,number must be from 1-3999")
elif selected_num>3999:
    print ("learn to read ,number must be from 1-3999")
else:
    #change the first digit
    if xiliada>1:
        lat_xiliada= 'M'*xiliada
    else:
        lat_xiliada=''

    #second digit
    if ekatontada==9:
        lat_ekatontada='CM'
    elif ekatontada >=5 and ekatontada<9:
        help1=ekatontada-5
        lat_ekatontada='D'+ help1*'C'
    elif ekatontada==4:
        lat_ekatontada='CD'
    else:
        lat_ekatontada= 'C'*ekatontada

    #third digit
    if dekada==9 :
        lat_dekada='XC'
    elif dekada >= 5and monada<9:
        help2=dekada-5
        lat_dekada='L'+help2*'X'
    elif dekada==4:
        lat_dekada='XL'
    else:
        lat_dekada='X'*dekada



    #fourth digit
    if monada==9:
        lat_monada='IX'
    elif monada>=5 and monada<9:
        help3=monada -5
        lat_monada='V'+ 'I'*help3
    elif monada==4:
        lat_monada='IV'
    else:
        lat_monada='I'*monada
    #result

    print ("the latin numeral for your number is:" + lat_xiliada+lat_ekatontada+lat_dekada+lat_monada )
