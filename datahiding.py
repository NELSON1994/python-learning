class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print("the count is  : ", self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
# print(counter.__secretCount)
# will throw error of not a member of the class so nt accessible outside the class

print(counter.__JustCounter__secretCount)

# You need to name attributes with a double underscore prefix, and those attributes then are not be directly visible to outsiders.
