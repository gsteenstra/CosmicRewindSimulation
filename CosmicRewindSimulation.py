import random

class PreShow:
    def __init__(self):
        self.name = "Wonders of Xandar"
        self.completed = False

    def play(self):
        print("\n--- GUARDIANS OF THE GALAXY: COSMIC REWIND ---")
        print("Welcome to EPCOT!")
        print("You have arrived at the Wonders of Xandar.")
        print("You enter the Galaxarium and learn about Xandar.")
        print("Suddenly, a cosmic emergency occurs!")
        print("The Guardians of the Galaxy need your help!")
        print("Proceed to the loading area.")
        print("---------------------------------------------\n")

        self.completed = True

class RideVehicle:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.status = "Waiting"
        self.song = "None"

        self.ride_profiles = [
            ["BACKWARD LAUNCH", "PLANET FLYBY",
             "TURN LEFT", "SPEED UP", "SLOW DOWN"],

            ["BACKWARD LAUNCH", "ASTEROID FIELD",
             "TURN RIGHT", "TURN LEFT", "SLOW DOWN"],

            ["BACKWARD LAUNCH", "SPACE JUMP",
             "TURN RIGHT", "SPEED UP", "SLOW DOWN"]
        ]

        self.songs = [
            "September",
            "Disco Inferno",
            "Conga",
            "Everybody Wants to Rule the World",
            "One Way or Another",
            "I Ran"
        ]

    def load_riders(self):
        self.status = "Loading"
        print(self.name, "is loading passengers...")
        print("Passengers are seated.")
        print("Restraints have been checked.")
        print("The ride vehicle is ready!\n")
    def select_music(self):
        self.song = random.choice(self.songs)
        print("Now Playing:", self.song)
        print("---------------------------------\n")
    def run_ride(self):
        profile = random.choice(self.ride_profiles)

        self.status = "Running"

        print(self.name, "is beginning the adventure!")
        print("The Guardians are ready!\n")

        for action in profile:
            print(self.name + ":", action)
            if action == "BACKWARD LAUNCH":
                self.speed = 50
                print("The coaster launches backward into space!")
            elif action == "SPEED UP":
                self.speed = 60
                print("The coaster speeds through the galaxy!")
            elif action == "SLOW DOWN":
                self.speed = 0
                print("The coaster slows down.")
            elif action == "PLANET FLYBY":
                print("The vehicle races past a giant planet!")
            elif action == "ASTEROID FIELD":
                print("The Guardians fly through an asteroid field!")
            elif action == "SPACE JUMP":
                print("The vehicle travels through a cosmic portal!")
            elif action == "TURN LEFT":
                print("The ride vehicle rotates left!")
            elif action == "TURN RIGHT":
                print("The ride vehicle rotates right!")

            print()

        self.status = "Stopped"

        print("---------------------------------")
        print(self.name, "has returned to the station!")
        print("The adventure is complete!\n")

    def unload_riders(self):
        if self.status == "Stopped":
            print("Passengers may now exit", self.name)
            print("Thank you for saving the galaxy!\n")
        else:
            print("The vehicle must stop before unloading.")

    def display_status(self):
        print("--- FINAL RIDE STATUS ---")
        print("Vehicle:", self.name)
        print("Status:", self.status)
        print("Speed:", self.speed, "mph")
        print("Song:", self.song)
        print("-------------------------\n")

class CosmicRewind:
    def __init__(self):
        self.preshow = PreShow()

        self.vehicles = [
            RideVehicle("Vehicle A"),
            RideVehicle("Vehicle B"),
            RideVehicle("Vehicle C")
        ]

    def start_ride(self):
        print("Welcome to Guardians of the Galaxy: Cosmic Rewind!")
        print("You enter the Wonders of Xandar pavilion.\n")

        self.preshow.play()

        if self.preshow.completed:
            vehicle = random.choice(self.vehicles)

            print("Assigned to:", vehicle.name)
            print()

            vehicle.load_riders()
            vehicle.select_music()
            vehicle.run_ride()
            vehicle.unload_riders()
            vehicle.display_status()
        else:
            print("The pre-show must finish before the ride begins.")


ride = CosmicRewind()
ride.start_ride()