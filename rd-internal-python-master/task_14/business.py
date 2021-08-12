
# Implement all methods where `NotImplementedError` is raised


class Company(object):
    """ Represents a company """

    def __init__(self, name, address=None):
        self.name = name
        self.address = address
        self.employees = []
        self.boss = None
        self.__money = 1000

    def set_boss(self, boss):
        # make sure that person is an instance of `Boss` class
        raise NotImplementedError()

    def add_employee(self, employee):
        # make sure employee is an instance of Engineer or Manager
        # make sure he is not employed already
        raise NotImplementedError()

    def dismiss_employee(self, employee):
        """
        Dismisses an employee. Employee must be a company member.
        Boss cannot be dismissed
        Company should notify employee that he/she was dismissed
        """
        raise NotImplementedError()

    def notify_im_leaving(self, employee):
        """ En employee should call this method when leaving a company """
        raise NotImplementedError()

    def show_money(self):
        """ Displays amount of money that company has"""
        raise NotImplementedError()

    def ask_for_payment(self, employee):
        """ An employee should call this method after doing work  """
        # make sure a person is actually employed
        # make sure a company is not a bankrupt
        # return 10 money to Engineer or 12 to Manager
        raise NotImplementedError()

    def make_a_party(self):
        """ Party time! All employees get 5 money """
        # make sure a company is not a bankrupt before and after the party
        raise NotImplementedError()

    def go_bankrupt(self):
        """
        Declare bankruptcy. Company money are drop to 0
        All employees become unemployed.
        """
        raise NotImplementedError()

    @property
    def is_bankrupt(self):
        """ returns True or False """
        return self.__money <= 0

    def __repr__(self):
        return 'Company (%s)' % self.name


class Person(object):
    """ Represents any person """

    def __init__(self, name, age, sex=None, address=None):
        self.name = name
        self.age = age
        self.sex = sex if sex is not None else '<not specified>'
        self.address = address

    def __repr__(self):
        return '%s, %s years old' % (self.name, self.age)


class Boss(Person):

    def __init__(self, name, age, sex=None, address=None):
        super(Boss, self).__init__(name, age, sex, address)
        self.company = None

    def notify_promoted(self, company):
        """ Company should call this method when hiring this boss """
        raise NotImplementedError()

    def __repr__(self):
        if self.company is None:
            return '%s, unemployed' % self.name
        return '%s. Boss at %s' % (self.name, self.company)


class Employee(Person):

    def __init__(self, name, age, sex=None, address=None):
        super(Employee, self).__init__(name, age, sex, address)
        self.company = None

    def join_company(self, company):
        # make sure that this person is not employed already
        raise NotImplementedError()

    def become_unemployed(self):
        """ Leave current company """
        raise NotImplementedError()

    def notify_dismissed(self):
        """ Company should call this method when dismissing an employee """
        raise NotImplementedError()

    @property
    def is_employed(self):
        """ returns True or False """
        return self.company is not None

    def __repr__(self):
        if self.is_employed:
            return '%s works at %s' % (self.name, self.company)
        return '%s, unemployed'


class Engineer(Employee):

    def __init__(self, name, age, sex=None, address=None):
        super(Engineer, self).__init__(name, age, sex, address)
        self.__money = 0

    def do_tasks(self):
        """ Do some work and receive payment from company """
        # make sure this person is employed
        raise NotImplementedError()

    def notify_rewarded(self, company, reward):
        """ Company should call this method when having a party """
        # make sure person is employed to the same company
        raise NotImplementedError()

    def show_money(self):
        """ Shows how much money person has earned """
        raise NotImplementedError()


class Manager(Employee):

    def __init__(self, name, age, sex=None, address=None):
        super(Manager, self).__init__(name, age, sex, address)
        self.__money = 0

    def write_reports(self):
        """ Do some work and receive payment from company """
        # make sure this person is employed
        raise NotImplementedError()

    def notify_rewarded(self, company, reward):
        """ Company should call this method when having a party """
        # make sure person is employed to the same company
        raise NotImplementedError()

    def show_money(self):
        """ Shows how much money person has earned """
        raise NotImplementedError()


def check_yourself():
    """ Now let's operate on objects """

    # create first company
    fruits_company = Company('Fruits', address='Ocean street, 1')
    steve = Boss('Steve', 44)
    fruits_company.set_boss(steve)
    print(fruits_company)

    # add some employees
    alex = Engineer('Alex', 55)
    alex.join_company(fruits_company)
    alex.do_tasks()
    alex.show_money()

    # add second company
    doors_company = Company('Windows and doors', 'Mountain ave. 10')
    print(doors_company)

    # Alex wants to work for doors
    alex.join_company(doors_company)
    # ups, already haired
    alex.become_unemployed()
    alex.join_company(doors_company)
    alex.do_tasks()

    # Bill also wants to work for doors
    bill = Engineer('Bill', 20)
    bill.join_company(doors_company)
    bill.do_tasks()

    # Jane is a very good manager. She wants to work for fruits
    jane = Manager('Jane', 30)
    jane.join_company(fruits_company)
    # Jane works pretty hard
    jane.write_reports()
    jane.write_reports()

    # Bill wants Jane to be his manager, he leaves doors and joins fruits
    bill.become_unemployed()
    bill.join_company(fruits_company)

    # doors becomes a bankrupt
    doors_company.go_bankrupt()

    # alex becomes unemployed and goes to fruits
    alex.join_company(fruits_company)

    # fruits company has a celebration party
    fruits_company.make_a_party()

    # results
    fruits_company.show_money()
    doors_company.show_money()
    alex.show_money()
    bill.show_money()
    jane.show_money()


if __name__ == '__main__':
    check_yourself()

