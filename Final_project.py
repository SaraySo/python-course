''' basic hotel management.'''
#########################################
# Question 1 -  every Minibar has attributes
#########################################
class Minibar:
    def __init__(self, drinks, snacks):
        self.drinks = drinks
        self.snacks = snacks
        self.bill = float(0)
        self.drinks = {k.lower(): v for k, v in self.drinks.items()}
        self.drinks = {k.lower(): v for k, v in self.drinks.items()}

    def __repr__(self):
        return 'The minibar contains the drinks: ' + str([*self.drinks]) + '\nAnd the snacks: ' + str([*self.snacks]) + '\nThe bill for the minibar is: ' + str(self.bill)

    def eat_a_snack(self, snack):
        snack = snack.lower()
        if snack in self.snacks:
            self.bill += self.snacks.pop(snack)
        else:
            raise ValueError('The snack is not in the minibar')

    def drink_a_drink(self, drink):
        drink = drink.lower()
        if drink in self.drinks:
            self.bill += self.drinks.pop(drink)
        else:
            raise ValueError('The drink is not in the minibar')

#########################################
# Question 2  - every Room has attributes
#########################################
class RoomError(Exception):
    #A subclass of Exception that defines a new error type
    #DO NOT change this class
    pass

class Room:
    def __init__(self, minibar, floor, number, guests, clean_level, rank, satisfaction=1.0):
        if not isinstance(clean_level, int):
            raise TypeError('clean level must be type int!')
        if not isinstance(rank, int):
            raise TypeError('rank must be type int!')
        if not isinstance(satisfaction, float or int):
            raise TypeError('satisfaction must be either type int or type float!')
        if not clean_level>=1 and clean_level<=10:
            raise ValueError('clean level needs to be 1-10')
        if not rank>=1 and clean_level<=3:
            raise ValueError('rank needs to be 1-3')
        if not satisfaction>=1 and satisfaction<=5:
            raise ValueError('clean level needs to be 1-5')

        self.minibar = minibar
        self.floor = floor
        self.number = number
        self.guests = [guest.lower() for guest in guests] 
        self.clean_level = clean_level
        self.rank = rank
        self.satisfaction = float(satisfaction)

 
    def __repr__(self):
        if len(self.guests) == 0:
            guests_val = "empty"
        else:
            guests_val = ', '.join(self.guests)
        return str(self.minibar) + "\nfloor: " + str(self.floor) + "\nnumber: " + str(self.number)\
               + "\nguests: " + guests_val\
               + "\nclean_level: " + str(self.clean_level)\
               + "\nrank: " + str(self.rank)\
               + "\nsatisfaction: " + str(round(self.satisfaction,1))


    def is_occupied(self):
        if self.guests == []:
            return False
        else:
            return True

    def clean(self):
        self.clean_level = min(10, self.clean_level + self.rank)

    def better_than(self, other):
        if not isinstance(other, Room):
            raise TypeError('Other must be an instanse of Room')
        else:
            if (self.rank,self.floor,self.clean_level)>(other.rank,other.floor,other.clean_level):
                return True
            else:
                return False
        
    def check_in(self, guests):
        if(self.is_occupied()):
            raise RoomError('Cannot check-in new guests to an occupied room')
        else:
            for guest in guests:
                self.guests.append(guest.lower())
            self.satisfaction = 1.0


    def check_out(self):
        if (not self.is_occupied()):
            raise RoomError('Cannot check-out an empty room')
        else:
            del self.guests[:]
            
    def move_to(self, other):
        if(not self.is_occupied()):
            raise RoomError('Cannot move guests from an empty room')
        if(other.is_occupied()):
            raise RoomError("Cannot move guests into an occupied room")
        for guest in self.guests:
            other.guests.append(guest)
        if other.better_than(self):
            other.satisfaction = min(5.0, self.satisfaction+1.0)
        else:
            other.satisfaction = self.satisfaction
        self.check_out()
   
#########################################
# Question 3 - Hotel
#########################################
class Hotel:
    def __init__(self, name, rooms):
        self.name = name.lower()
        self.rooms = rooms
        
    def room_count(self):
        count = 0
        for room in self.rooms:
            if len(room.guests) > 0:
                count += 1
        return count
    
    def __repr__(self):
        return self.name + ' hotel has:\n' + str(len(self.rooms)) + ' rooms\n'+ str(self.room_count()) + ' occupied rooms'
                      
    def check_in(self, guests, rank):
        result = None
        for room in self.rooms:
            if room.rank == rank and room.guests == []:
                try:
                    room.check_in(guests)
                    result = room
                except RoomError:
                    pass
        return result

    def check_out(self, guest):
        guest_lower = guest.lower()
        result = None
        for room in self.rooms:
            for guest1 in room.guests:
                if guest1 == guest_lower:
                    try:
                        room.check_out()
                        result = room
                    except RoomError:
                        pass
        return result 

    def upgrade(self, guest):
        guest_lower = guest.lower()
        result = None
        for room_out in self.rooms:
            for guest1 in room_out.guests:
                if guest1 == guest_lower:
                    for room_in in self.rooms:
                        if room_in.better_than(room_out) == True and room_in.is_occupied() == False :
                            try:
                                room_out.move_to(room_in)
                                result = room_in
                            except RoomError:
                                pass
        return result
        
#########################################
# Question 3 supplement 
#########################################
def test_hotel():
    m = Minibar({'coke': 10, 'lemonade': 7}, {'bamba': 8, 'mars': 12})
    rooms = [Room(m, 15, 140, [], 5, 1), Room(m, 12, 101, ["Ronen", "Shir"], 6, 2),
             Room(m, 1, 2, ["Liat"], 7, 1), Room(m, 2, 23, [], 6, 3)]
    h = Hotel("Dan", rooms)
    test_sep = '\n------------------'
    print('PRINT h:\n', h, test_sep, sep="")
    print(m)
    print('PRINT h:\n', h, test_sep, sep="")
    print('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")
    print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
    print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
    print('CALL: h.check_in(["Alice", "Wonder"], 2)\n', h.check_in(["Alice", "Wonder"], 2), test_sep, sep="")
    print('CALL: h.check_in(["Alex"], 3)\n', h.check_in(["Alex"], 3), test_sep, sep="")
    print('PRINT h:\n', h, test_sep, sep="")
    print('CALL: h.check_in(["Oded", "Shani"], 3)\n', h.check_in(["Oded", "Shani"], 3), test_sep, sep="")
    print('CALL: h.check_in(["Oded", "Shani"], 1)\n', h.check_in(["Oded", "Shani"], 1), test_sep, sep="")
    print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print('PRINT h:\n', h, test_sep, sep="")


#########################
# main code 
# You can add more validation cases below
#########################
if __name__ == "__main__":
   ##test_hotel() ## After you are done implenting all classes and methods, you may comment-in the call to test_hotel() and compare the results with the 
    pass
#m = Minibar({'coke':10,'lemonade':7},{'bamba':8,'mars':12})
#r1 = Room(m,2,23,['Dana','Ron'],5,2)
#r_better = Room(m,6,57,[],4,3)
#print (r_better.better_than(r1))
#r_better.check_in(["Amir"])
#r_better.clean()
#print(r_better.clean_level)


#print(r1.is_occupied())

#r1.check_out() ## note: None is returned, and so nothing is printed
#print(r1.is_occupied())

#r_better.move_to(r1)
#print(r1.satisfaction)

#print(r1.guests)

#r1.move_to(r_better)
#print(r1.is_occupied())

#print(r_better.satisfaction)

#print(r_better.guests)
