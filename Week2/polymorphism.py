class Building:
    strAddress = "Daejeon"
    def openDoor(self):
        print("Door Opended")
        
class Hotel:
    def openDoor(self):
        print("Bellboy opens a door")
        
    def checkIn(self, days = 1):
        print("Someone checks in for", days, "days")
        
lotteHotel = Hotel()
lotteHotel.openDoor()
lotteHotel.checkIn()
lotteHotel.checkIn(2)