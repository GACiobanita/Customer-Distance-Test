from implementation.organizer import Organizer
from implementation.user_inviter import UserInviter

def main():
    organizer=Organizer()
    user_inviter=UserInviter()

    print("This program will return a list of Customers, including name, id")
    print("and coordinatesthat are within 100 kilometers of the Dublin office.")

    organizer.acquire_filepath()
    organizer.read_from_filepath()

    user_inviter.create_customer_data(organizer.fileData)
    user_inviter.display_customer_data()

if __name__ == "__main__":
    main()