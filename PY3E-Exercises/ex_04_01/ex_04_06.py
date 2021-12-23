def computepay(h, r):
    #print ("In computepay", h, r)
    if h > 40:
        reg = h * r
        # I don't know what fuck this calculation MEANS
        overtime = (h - 40.0) * (r * 0.50)
        pay = reg + overtime
        return pay
        #always remeber of "else", after "if" and remeber putting the shit of ":" as well
    else:
        pay = fh * fr
        #print ("Returning", pay)
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
fh = float(hrs)
fr = float(rate)

xp = computepay(fh, fr)

print("Pay", xp)
