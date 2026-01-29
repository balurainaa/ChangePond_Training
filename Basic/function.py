def gsal(bsal):
    return bsal+allowance(bsal)
def nsal(bsal):
    return gsal(bsal)-detuction(bsal)
def allowance(bsal):
    hra=bsal*0.3
    ta=bsal*0.2
    da=bsal*0.1
    return hra+ta+da
def detuction(bsal):
    pf=bsal*0.12
    if bsal>10000:
        ptax=200
    else:
        ptax=0
    ins=350
    return pf+ptax+ins
bsal=int(input("Enter the basic salary: "))
print("salary slip")
print("Basic salary:",bsal)
print("Allowance amount:",allowance(bsal))
print("detuction amount:",detuction(bsal))
print("Gross salary Annualy:",12*gsal(bsal))
print("Net salary Annualy:",12*nsal(bsal))
