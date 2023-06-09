import os
import time

# abstracting moving text
def moving(message, speed):
  for char in message:
    print(char, end='', flush = True)
    time.sleep(speed)

#create history file
def create_file():
  #checking if file exists
  if not os.path.exists("bookmarks.txt"):
    with open("bookmarks.txt", "w") as f:
      f.write("")

#add bookmark function
def add_bookmark():
  while True:
    # prompting user input for the bookmarks
    section = input("Enter a Section:")
    topic = input("Enter topic:")
    url = input("Enter Url:")
    note = input("Enter a note:")

    #append the new bookmark to the file
    with open("bookmarks.txt", "a") as f:
      f.write(f"{section.capitalize()}\t{topic.capitalize()}\t{url}\t{note}\n")
    print(f"Added {section}: {topic}")

  # asking if the user wants to add another bookmark
    m6 = "Do you want to add another bookmark?(y/n)\n"
    moving(m6,0.05)
    c = input("")
    if c.lower() != "y":
      break

#Display bookmarks
def display_bookmarks():
  with open("bookmarks.txt", "r") as f:
    bookmarks = f.read().splitlines()
  
  #checking if it has any bookmarks
  if len(bookmarks) == 0:
    print("You dont have any stored bookmarks")
  else:
    for bookmark in bookmarks:
      # identifying different parts of the bookmarks by the tabs
      section, topic, url, note = bookmark.split("\t")
      # printing them back to the user
      print(f"{section}: {topic} {url}\n")
      if note:
        print(f"Note: {note}\n\n")
      else:
        print("\n\n")

def disp_top():
  with open("bookmarks.txt", "r") as f:
    bookmarks = f.read().splitlines()
  # checks if any bookmarks exist                                                                                                                                                                                                                                                                                                                                                    
  if len(bookmarks) == 0:
    mes = "No bookmarks found."
    moving(mes, 0.075)
  # creates an arry for each bookmark and takes the second value(topic) and stores it in a set in the variable topics
  else:
    topics = set([bookmark.split("\t")[1] for bookmark in bookmarks])
    print("\nTopics:")
    for topic in sorted(topics):
      print(f"- {topic}")

#delete all bookmarks
def clear():
  while True:  
    # asking for confirmation
    m4 = "Are you sure you want to clear all bookmarks"
    moving(m4, 0.1)
    choice = input("(y/n)")
    if choice == "y":
      # replacing all the writing with ""
      with open("bookmarks.txt", "w") as f:
        f.write("")
        m5 = "All bookmarks Cleared\n"
        moving(m5, 0.05)
        break
    elif choice == "n":
      break
    else:
      print("Invalid choice, Try again\n")

def by_sec():
  with open("bookmarks.txt","r") as f:
    bookmarks = f.read().splitlines()

  if len(bookmarks) == 0:
    m2 = "Sorry no bookmarks stored."
    moving(m2, 0.05)
  else:
    sections = ["Health", "Arabic", "History", "Math", "Bio", "English", "Csp", "ST"]
    for i, section in enumerate(sections):
      #printing numbered sections 
      print(f"{i+1}. {section.capitalize()}")
    m3 = "Enter section number:"
    moving(m3, 0.2)
    choice = input("")
    # getting the bookmarks that start with the same section as the number selected
    sec_bkmrk = [bookmark for bookmark in bookmarks if bookmark.startswith(f"{sections[int(choice)-1]}\t")]
    if len(sec_bkmrk) > 0:
      print(f"\n{sections[int(choice)-1].capitalize()} bookmarks:")
      # printing loop
      for bookmark in sec_bkmrk:
        _, topic, url, note = bookmark.split("\t")
        print(f"{topic} - {url}")
        if note:
          print(f"  Note: {note}\n\n")
        else:
          print("\n\n")
    else:
      print("No bookmarks found for the selected section.")
  
def main():
  # creates file if not there
  create_file()

  while True:
    time.sleep(1)
    # prompts user to choose an application option 
    m1 = "\n\n1. Add Bookmark\n2. Diplay Bookmarks\n3. Clear Bookmarks\n4. Display by secton\n5. Display topic list\n6. Exit\n\nOption:"
    moving(m1, 0.025)

    choice = input("")

    #redirects the users choice to the appropriate function   
    if choice == "1":
      add_bookmark()
    if choice == "2":
      display_bookmarks()
    if choice == "3":
      clear()
    if choice == "4":
      by_sec()
    if choice == "5":
      disp_top()
    if choice == "6":
      break

if __name__ == "__main__":
  main()