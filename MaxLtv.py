loanPurpose         = ''
propertyType        = ''
fico                = ''
ltv                 = ''
loanAmt             = ''
dti                 = ''
reserves            = ''




def sponge_max_ltv(loanPurpose):
    # Purchase / RateTerm Refi
    if loanPurpose in('purchase', 'rateTerm', ''):
        max_ltv = 90
        
        # Check Property Types // Purch || rateTerm
        
        if propertyType in('sfr', 'pud', 'condo'):
            max_ltv = 90
            
            # Check FICO // SFR || PUD || Condo
            if fico >= 720:
                max_ltv = 90
            elif fico >= 700:
                max_ltv = 90
            elif fico >= 680:
                max_ltv = 90
            elif fico >= 660:
                max_ltv = 80
            elif fico >= 660:
                max_ltv = 80
            elif fico >= 640:
                max_ltv = 75
            elif fico >= 599:
                max_ltv = 65
            else:
                max_ltv = 0
                
        if propertyType == 'rural':
            max_ltv = 80
            
            # Check FICO // rural
            if fico >= 720:
                max_ltv = 80
            elif fico >= 700:
                max_ltv = 80
            elif fico >= 680:
                max_ltv = 80
            else:
                max_ltv = 0
                
        if propertyType == 'manufactured':
            max_ltv = 70
            
            # Check FICO // Manufactured
            if fico >= 720:
                max_ltv = 70
            elif fico >= 700:
                max_ltv = 70
            elif fico >= 680:
                max_ltv = 70
            else:
                max_ltv = 0
                
        if propertyType == 'twoToFour':
            max_ltv = 80
            
            # Check FICO // 2-4 Unit
            if fico >= 720:
                max_ltv = 80
            elif fico >= 700:
                max_ltv = 80
            elif fico >= 680:
                max_ltv = 80
            elif fico >= 660:
                max_ltv = 75
            else:
                max_ltv = 0
    elif loanPurpose == 'cashout':
        max_ltv = 80
        
        # Check Property Types // cashout
        
        if propertyType in('sfr', 'pud', 'condo'):
            max_ltv = 80
        if propertyType == 'rural':
            max_ltv = 80
        if propertyType == 'manufactured':
            max_ltv = 70
        if propertyType == 'twoToFour':
            max_ltv = 70
    else:
        max_ltv = "0"

        

    print(max_ltv)



sponge_max_ltv(loanPurpose)