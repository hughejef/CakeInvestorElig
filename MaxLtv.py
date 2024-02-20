loanPurpose         = ''
propertyType        = ''
fico                = ''
ltv                 = ''
loanAmt             = ''
dti                 = ''
reserves            = ''




def sponge_max_ltv_purpose(loanPurpose):
    if loanPurpose in('purchase', 'rateTerm', ''):
        max_ltv = 90
        if 
    elif loanPurpose == 'cashOut':
        max_ltv = 80
    else:
        max_ltv = 90

    print(max_ltv)



find_max_ltv(loanPurpose)