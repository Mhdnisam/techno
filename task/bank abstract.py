from abc import ABC, abstractmethod


class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass


class Canara(Bank):
    def __init__(self, B_name, Acc_no, name, age):
     print("Canara_branch =", B_name)
     print("account_no =", Acc_no)
     print("name =", name)
     print("age =", age)

    def interest(self):
        print("canara bank interset is 6.3%\n")


class Sbi(Bank):
    def __init__(self, B_name, Acc_no, name, age):
        print("Sbi_branch =", B_name)
        print("account_no =", Acc_no)
        print("name =", name)
        print("age =", age)

    def interest(self):
        print("sbi bank interset is 6.3%\n")


class Kscb(Bank):
    def __init__(self, B_name, Acc_no, name, age):
        print("Kscb_branch =", B_name)
        print("account_no =", Acc_no)
        print("name =", name)
        print("age =", age)

    def interest(self):
        print("kscb bank interset is 6.3%")


bank = Canara("kallachi", 10020, "nisam", 21)
bank.interest()
bank = Sbi("nadapuram", 17640, "saliha", 21)
bank.interest()
bank = Kscb("vanimel", 62123, "chikku", 20)
bank.interest()
