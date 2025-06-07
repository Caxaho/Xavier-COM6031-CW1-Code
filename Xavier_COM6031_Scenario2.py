class GenericPublisherInterface():
    def __init__(self):
        self._subscribers = []

    def AddSub(self, subscriber):
        self._subscribers.append(subscriber)

    def RemoveSub(self, subscriber):
        self._subscribers.remove(subscriber)

    def Notify(self, data):
        for subscriber in self._subscribers:
            subscriber.Update(data)

class GenericSubscriberInterface():
    def Update(self, data):
        pass

class InsuranceCompany(GenericPublisherInterface):
    def __init__(self, premium):
        super().__init__()
        self._premium = premium

    def GetPremium(self):
        return self._premium

    def SetPremium(self, new_premium):
        print(f'\nSetting Insurance Premium to: {new_premium}')
        self._premium = new_premium
        self.Notify(self._premium)

class Customer1(GenericSubscriberInterface):
    def Update(self, new_premium):
        if(new_premium > 100):
            print("Customer 1: This new insurance premium is unacceptable")
        else:
            print("Customer 1: This is an acceptable new insurance premium")

class Customer2(GenericSubscriberInterface):
    def Update(self, new_premium):
        if(new_premium > 150):
            print("Customer 2: This new insurance premium is unacceptable")
        else:
            print("Customer 2: This is an acceptable new insurance premium")

class Customer3(GenericSubscriberInterface):
    def Update(self, new_premium):
        if(new_premium > 200):
            print("Customer 3: This new insurance premium is unacceptable")
        else:
            print("Customer 3: This is an acceptable new insurance premium")

if __name__ == "__main__":
    evil_insurance = InsuranceCompany(80)
    c1 = Customer1()
    c2 = Customer2()
    c3 = Customer3()
    evil_insurance.AddSub(c1)
    evil_insurance.AddSub(c2)
    evil_insurance.AddSub(c3)
    print(f'Current Insurance: {evil_insurance.GetPremium()}')
    evil_insurance.SetPremium(90)
    evil_insurance.SetPremium(110)
    evil_insurance.SetPremium(160)
    evil_insurance.SetPremium(210)