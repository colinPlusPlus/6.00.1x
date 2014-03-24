def findPayment(loan, r, m):
	'''Assumes: loan and r are floats, m an int
	   Returns the monthly payment for a mortgage of size
	   loan at a monthly rate of r for m month '''
	return loan*((r*(1+r)**m)/((1+r)**m -1))

class Mortgage(object):
    '''Abstract class for building different kinds of mortgages'''
	
    def __init__(self, loan, annRate, months):
        '''Create a new mortgage'''
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payments = findPayment(loan, self.rate, months)
        self.legend = None #description of mortgage

    def makePayment(self):
        '''Make a payment'''
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)
    def getTotalPayment(self):
        '''Return the total amount paid so far'''
        return sum(self.paid)
    def __str__(self):
        return self.legend

class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' +str(r*100)+ "%"

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' +str(r*100)+'%, ' +str(pts)+ 'points'

		