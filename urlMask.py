#!/usr/bin/python3
# Created by @p4nujr
import os
from time import sleep
import pyshorteners

os.system('clear')



def Main():
    print("------------------------------------------------------------")
    print("                [urlMask]                   ")
    print("   Hide your URL to social engineer targets ;)   ")
    print("                                                 by p4nujr   ")
    print("------------------------------------------------------------")
    print("\nPlease choose in which of these websites you want to hide your link: ")
    print("\n1)  Google")
    print("2)  Youtube")
    print("3)  Spotify")
    print("4)  Instagram")
    print("5)  Facebook")
    print("6)  Tik Tok")
    print("7)  Personalized")
    print("\n8)  Exit")
    Selector()


def Selector():
    option = int(input("\nSelect a option: "))
    if option == 1:
        google()
    elif option == 2:
        youtube()
    elif option == 3:
        spotify()
    elif option == 4:
        instagram()
    elif option == 5:
        facebook()
    elif option == 6:
        tiktok()
    elif option == 7:
        personalized()
    elif option == 8:
        os.system('clear')

        print("Goodbye...")
        sleep(1)
        os.system('clear')

        exit()
    else:
        os.system('clear')

        print("Not valid option...")
        sleep(1)
        os.system('clear')

        Main()


def google():
    os.system('clear')

    print("You have selected Google.")
    originalLink = str(input("\nURL to mask: "))

    print("\nPlease type between hyphens, words or phrases related to the masked url to trick the victim, e.g: login-google")
    postLink = str(input("\nPost LINK: "))

    s = pyshorteners.Shortener()
    linkShorted = s.isgd.short(originalLink)
    noHttps = linkShorted[8:]
    os.system('clear')

    print(f"\nYour link is: https://www.google.com-{postLink}@{noHttps}")

    Other()


def youtube():
    os.system('clear')

    print("You have selected Youtube.")
    originalLink = str(input("\nURL to mask: "))

    print("\nPlease type between hyphens, words or phrases related to the masked url to trick the victim, e.g: p4nujr-tutorial-how-to-hack")
    postLink = str(input("\nPost LINK: "))

    s = pyshorteners.Shortener()
    linkShorted = s.isgd.short(originalLink)
    noHttps = linkShorted[8:]
    os.system('clear')

    print(f"\nYour link is: https://www.youtube.com-{postLink}@{noHttps}")

    Other()


def spotify():
    os.system('clear')

    print("You have selected Spotify.")
    originalLink = str(input("\nURL to mask: "))

    print("\nPlease type between hyphens, words or phrases related to the masked url to trick the victim, e.g: podcast-p4nujr-how-to-hack")
    postLink = str(input("\nPost LINK: "))

    s = pyshorteners.Shortener()
    linkShorted = s.isgd.short(originalLink)
    noHttps = linkShorted[8:]
    os.system('clear')

    print(f"\nYour link is: https://www.spotify.com-{postLink}@{noHttps}")

    Other()


def instagram():
    os.system('clear')

    print("You have selected Instagram.")
    originalLink = str(input("\nURL to mask: "))

    print("\nPlease type between hyphens, words or phrases related to the masked url to trick the victim, e.g: new-reel-p4nujr")
    postLink = str(input("\nPost LINK: "))

    s = pyshorteners.Shortener()
    linkShorted = s.isgd.short(originalLink)
    noHttps = linkShorted[8:]
    os.system('clear')

    print(f"\nYour link is: https://www.instagram.com-{postLink}@{noHttps}")

    Other()


def facebook():
    os.system('clear')

    print("You have selected Facebook.")
    originalLink = str(input("\nURL to mask: "))

    print("\nPlease type between hyphens, words or phrases related to the masked url to trick the victim, e.g: new-photo-p4nujr-his-new-programm")
    postLink = str(input("\nPost LINK: "))

    s = pyshorteners.Shortener()
    linkShorted = s.isgd.short(originalLink)
    noHttps = linkShorted[8:]
    os.system('clear')

    print(f"\nYour link is: https://www.facebook.com-{postLink}@{noHttps}")

    Other()


def tiktok():
    os.system('clear')

    print("You have selected Tik Tok.")
    originalLink = str(input("\nURL to mask: "))

    print("\nPlease type between hyphens, words or phrases related to the masked url to trick the victim, e.g: view-new-tiktok-of-p4nujr")
    postLink = str(input("\nPost LINK: "))

    s = pyshorteners.Shortener()
    linkShorted = s.isgd.short(originalLink)
    noHttps = linkShorted[8:]
    os.system('clear')

    print(f"\nYour link is: https://www.tiktok.com-{postLink}@{noHttps}")

    Other()


def personalized():
    os.system('clear')

    print("You have selected Personalized.")
    domain = str(input("Example.com/es... input domain: "))
    originalLink = str(input("\nURL to mask: "))

    print("\nPlease type between hyphens, words or phrases related to the masked url to trick the victim, e.g: something-related-with-your-personalized-url")
    postLink = str(input("\nPost LINK: "))

    s = pyshorteners.Shortener()
    linkShorted = s.isgd.short(originalLink)
    noHttps = linkShorted[8:]
    os.system('clear')

    print(f"\nYour link is: https://www.{domain}-{postLink}@{noHttps}")

    Other()


def Other():
    print("\033[93m\nDo you want to create another link?")
    print("Yes 1) \nNo  2)")
    option = int(input("\nSelect a option: "))
    if option == 1:
        os.system('clear')

        Main()
    else:
        os.system('clear')

        exit()

# SYSCALL

Main()
