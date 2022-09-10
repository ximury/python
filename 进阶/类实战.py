# 类实战
# 旧写法
class AddressBookOld:
    def __init__(self):
        self.persons = []

    def addPerson(self, person):
        self.persons.append(person)


addressBook = AddressBookOld()
zhangSan = {'name': '张三', 'address': '南京', 'phone': '12306'}
liSi = {'name': '李四', 'address': '北京', 'phone': '10086'}
addressBook.addPerson(zhangSan)
addressBook.addPerson(liSi)
print(addressBook.persons)


# 改善写法

class AddressBook:
    def __init__(self):
        self.persons = []

    def create_person(self):
        name = input('name: ')
        address = input('address: ')
        phone = input('phone: ')
        person = {'name': name, 'address': address, 'phone': phone}
        self.persons.append(person)

    def list_person(self):
        for person in self.persons:
            print('%s,%s,%s' % (person['name'], person['address'], person['phone']))

    def query_person(self):
        name = input('name: ')
        for person in self.persons:
            if person['name'] == name:
                print('%s,%s,%s' % (person['name'], person['address'], person['phone']))

    def delete_person(self):
        name = input('name: ')
        for person in self.persons:
            if person['name'] == name:
                self.persons.remove(person)
                break


def get_choice():
    print('1. create person')
    print('2. list all persons')
    print('3. query person')
    print('4. delete person')
    print('5. quit')
    choice = input('Enter a number(1-5):')
    return choice


if __name__ == '__main__':
    addressBook = AddressBook()
    while True:
        choice = get_choice()

        if choice == '1':
            addressBook.create_person()
        elif choice == '2':
            addressBook.list_person()
        elif choice == '3':
            addressBook.query_person()
        elif choice == '4':
            addressBook.delete_person()
        elif choice == '5':
            break
        else:
            print('Invalid choice')
