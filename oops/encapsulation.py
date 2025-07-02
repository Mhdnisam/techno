# # public
#
# class Public:
#     def access(self):
#         print("this public")
#
#
# obj = Public()
# obj.access()

# # protect
#
# class Protect:
#     _name = "nisam"
#
#     def show(self, salary):
#         self._salary = salary
#         print("my salary =", salary)
#         print(self._name)
#
# obj = Protect()
# obj.show(233333)

# private

class Private:
    __name = "saliha"

    def show(self):
        print(self.__name)


obj = Private()
obj.show()


