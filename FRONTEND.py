from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import font
import datetime
from datetime import datetime
from datetime import timedelta
from datetime import time
from BACKEND import *

global pageGeometry
global bannerHeight
global bannerWidth
global optionButtonWidth
global buttonWidth
global confirmPageGeometry
global fontSize
global buttonFontSize
global Password

pageGeometry = '1280x720'
bannerHeight = 2
optionButtonWidth = 12
bannerWidth = 60
buttonWidth = 20

confirmPageGeometry = '500x500'
reportGeometry = '1000x500'
fontSize = ("Helvetica", 30)
buttonFontSize = ("Helvatica", 20)

Password = "password"  # SET AS YOUR OWN PASSWORD

# Main Page


def mainToMembership():
    mainPage.destroy()
    membershipPageFunction()


def mainToBooks():
    mainPage.destroy()
    bookPageFunction()


def mainToLoans():
    mainPage.destroy()
    loansPageFunction()


def mainToReservations():
    mainPage.destroy()
    reservationsPageFunction()


def mainToFines():
    mainPage.destroy()
    finesPageFunction()


def mainToReports():
    mainPage.destroy()
    reportsFunction()


def weGoMain():
    buttonToMainPage.destroy()
    mainPageFunction()


global buttonToMainPage
buttonToMainPage = Tk()
buttonToMainPage.geometry(pageGeometry)
buttonToMainPage.title("Click this button to access ALS Main Page")
buttonToMainPage_label = Label(buttonToMainPage, text="Click this button to access ALS Main Page",
                               font=fontSize)
buttonToMainPage_label.place(relx=0.5, rely=0.3, anchor=CENTER)

buttonToMainPage_btn = Button(buttonToMainPage, command=weGoMain,
                              text="Open ALS", font=fontSize)
buttonToMainPage_btn.place(relx=0.5, rely=0.5, anchor=CENTER)


def mainPageFunction():
    global mainPage
    mainPage = Tk()
    mainPage.geometry(pageGeometry)
    mainPage.title("ALS Main Page")
    mainPage_label = Label(mainPage, text="(ALS)",
                           font=fontSize)
    mainPage_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    # 6 labels
    membership_label = Label(mainPage, text="Membership", font=fontSize)
    membership_label.place(relx=0.25, rely=0.5, anchor=CENTER)
    books_label = Label(mainPage, text="Books", font=fontSize)
    books_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    loans_label = Label(mainPage, text="Loans", font=fontSize)
    loans_label.place(relx=0.75, rely=0.5, anchor=CENTER)
    reservations_label = Label(
        mainPage, text="Reservations", font=fontSize)
    reservations_label.place(relx=0.25, rely=0.9, anchor=CENTER)
    fines_label = Label(mainPage, text="Fines", font=fontSize)
    fines_label.place(relx=0.5, rely=0.9, anchor=CENTER)
    reports_label = Label(mainPage, text="Reports", font=fontSize)
    reports_label.place(relx=0.75, rely=0.9, anchor=CENTER)
    # 6 buttons
    membership_btn = Button(mainPage, command=mainToMembership,
                            text="MEMBERSHIP BUTTON", font=fontSize)
    membership_btn.place(relx=0.25, rely=0.35, anchor=CENTER)
    books_btn = Button(mainPage, command=mainToBooks,
                       text="BOOKS BUTTON", font=fontSize)
    books_btn.place(relx=0.5, rely=0.35, anchor=CENTER)
    loans_btn = Button(mainPage, command=mainToLoans,
                       text="LOANS BUTTON", font=fontSize)
    loans_btn.place(relx=0.75, rely=0.35, anchor=CENTER)
    reservations_btn = Button(
        mainPage, command=mainToReservations, text="RESERVATIONS BUTTON", font=fontSize)
    reservations_btn.place(relx=0.25, rely=0.8, anchor=CENTER)
    fines_btn = Button(mainPage, command=mainToFines,
                       text="FINES BUTTON", font=fontSize)
    fines_btn.place(relx=0.5, rely=0.8, anchor=CENTER)
    reports_btn = Button(mainPage, command=mainToReports,
                         text="REPORTS BUTTON", font=fontSize)
    reports_btn.place(relx=0.75, rely=0.8, anchor=CENTER)

######################################################
# Membership Page


def membershipToCreation():
    membershipPage.destroy()
    membershipCreationPageFunction()


def membershipToDeletion():
    membershipPage.destroy()
    membershipDeletionPageFunction()


def membershipToUpdate():
    membershipPage.destroy()
    membershipUpdatePageFunction()


def membershipToMainMenu():
    membershipPage.destroy()
    mainPageFunction()


def membershipPageFunction():
    global membershipPage
    membershipPage = Tk()
    membershipPage.geometry(pageGeometry)
    membershipPage.title("Membership")
    membershipPage_topBanner = Label(
        membershipPage, text="Select one of the Options below:", font=fontSize)
    membershipPage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    creation_btn = Button(membershipPage, height=bannerHeight, width=optionButtonWidth,
                          command=membershipToCreation, text="1. Creation", font=fontSize)
    creation_btn.place(relx=0.5, rely=0.35, anchor=CENTER)
    membershipCreation_label = Label(
        membershipPage, text="Membership Creation", font=fontSize)
    membershipCreation_label.place(relx=0.8, rely=0.35, anchor=CENTER)

    deletion_btn = Button(membershipPage, height=bannerHeight, width=optionButtonWidth,
                          command=membershipToDeletion, text="2. Deletion", font=fontSize)
    deletion_btn.place(relx=0.5, rely=0.55, anchor=CENTER)
    membershipDeletion_label = Label(
        membershipPage, text="Membership Deletion", font=fontSize)
    membershipDeletion_label.place(relx=0.8, rely=0.55, anchor=CENTER)

    update_btn = Button(membershipPage, height=bannerHeight, width=optionButtonWidth,
                        command=membershipToUpdate, text="3. Update", font=fontSize)
    update_btn.place(relx=0.5, rely=0.75, anchor=CENTER)
    membershipUpdate_label = Label(
        membershipPage, text="Membership Update", font=fontSize)
    membershipUpdate_label.place(relx=0.8, rely=0.75, anchor=CENTER)

    backToMain_btn = Button(membershipPage, height=bannerHeight, width=bannerWidth,
                            command=membershipToMainMenu, text="Back To Main Menu", font=fontSize)
    backToMain_btn.place(relx=0.5, rely=0.9, anchor=CENTER)


def membershipCreationToMainPage():
    membershipCreationPage.destroy()
    mainPageFunction()


def membershipCreationPageFunction():
    global membershipCreationPage
    membershipCreationPage = Tk()
    membershipCreationPage.geometry(pageGeometry)
    membershipCreationPage.title("Membership Creation")
    membershipCreationPage_topBanner = Label(
        membershipCreationPage, text="To Create Member, Please Enter Requested Information Below:", font=fontSize)
    membershipCreationPage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    membershipID_label = Label(
        membershipCreationPage, text="Membership ID", font=fontSize)
    membershipID_label.place(relx=0.2, rely=0.25, anchor=CENTER)
    membershipID = StringVar()
    membershipID_entry = Entry(
        membershipCreationPage, textvariable=membershipID)
    membershipID_entry.place(relx=0.4, rely=0.25, anchor=CENTER)

    name_label = Label(
        membershipCreationPage, text="Name", font=fontSize)
    name_label.place(relx=0.2, rely=0.35, anchor=CENTER)
    name = StringVar()
    name_entry = Entry(
        membershipCreationPage, textvariable=name)
    name_entry.place(relx=0.4, rely=0.35, anchor=CENTER)

    faculty_label = Label(
        membershipCreationPage, text="Faculty", font=fontSize)
    faculty_label.place(relx=0.2, rely=0.45, anchor=CENTER)
    faculty = StringVar()
    faculty_entry = Entry(
        membershipCreationPage, textvariable=faculty)
    faculty_entry.place(relx=0.4, rely=0.45, anchor=CENTER)

    phonenumber_label = Label(
        membershipCreationPage, text="Phone Number", font=fontSize)
    phonenumber_label.place(relx=0.2, rely=0.55, anchor=CENTER)
    phonenumber = StringVar()
    phonenumber_entry = Entry(
        membershipCreationPage, textvariable=phonenumber)
    phonenumber_entry.place(relx=0.4, rely=0.55, anchor=CENTER)

    email_label = Label(
        membershipCreationPage, text="Email Address", font=fontSize)
    email_label.place(relx=0.2, rely=0.65, anchor=CENTER)
    email = StringVar()
    email_entry = Entry(
        membershipCreationPage, textvariable=email)
    email_entry.place(relx=0.4, rely=0.65, anchor=CENTER)

    def createMember():
        MembershipID = membershipID_entry.get()
        Name = name_entry.get()
        Faculty = faculty_entry.get()
        PhoneNumber = phonenumber_entry.get()
        EmailAddress = email_entry.get()

        if createMembership(MembershipID, Name, Faculty, PhoneNumber, EmailAddress):
            # Success
            global membershipCreationSuccess
            membershipCreationSuccess = Tk()
            membershipCreationSuccess.geometry(confirmPageGeometry)
            membershipCreationSuccess.title("Membership Creation Success")
            membershipCreationSuccess_label = Label(
                membershipCreationSuccess, text="Success!", font=fontSize)
            membershipCreationSuccess_label.place(
                relx=0.5, rely=0.3, anchor=CENTER)
            membershipCreationSuccessnote_label = Label(
                membershipCreationSuccess, text="ALS Membership created", font=fontSize)
            membershipCreationSuccessnote_label.place(
                relx=0.5, rely=0.5, anchor=CENTER)
            backToCreateFunction_btn = Button(membershipCreationSuccess, height=bannerHeight, width=buttonWidth,
                                              command=backToCreateFunctionSuccess, text="Back to\nCreate Function", font=buttonFontSize)
            backToCreateFunction_btn.place(relx=0.5, rely=0.8, anchor=CENTER)
        else:
            # Error
            global membershipCreationError
            membershipCreationError = Tk()
            membershipCreationError.geometry(confirmPageGeometry)
            membershipCreationError.title("Membership Creation Error")
            membershipCreationError_label = Label(
                membershipCreationError, text="Error!", font=fontSize)
            membershipCreationError_label.place(
                relx=0.5, rely=0.3, anchor=CENTER)
            membershipCreationErrornote_label = Label(
                membershipCreationError, text="Member already exist; Missing or\n Incomplete fields.", font=buttonFontSize)
            membershipCreationErrornote_label.place(
                relx=0.5, rely=0.5, anchor=CENTER)
            backToCreateFunction_btn = Button(membershipCreationError, height=bannerHeight, width=buttonWidth,
                                              command=backToCreateFunctionError, text="Back to\nCreate Function", font=buttonFontSize)
            backToCreateFunction_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    createMember_btn = Button(membershipCreationPage, height=bannerHeight, width=buttonWidth,
                              command=createMember, text="Create Member", font=fontSize)
    createMember_btn.place(relx=0.3, rely=0.8, anchor=CENTER)
    backToMainMenu_btn = Button(membershipCreationPage, height=bannerHeight, width=buttonWidth,
                                command=membershipCreationToMainPage, text="Back To Main Menu", font=fontSize)
    backToMainMenu_btn.place(relx=0.7, rely=0.8, anchor=CENTER)


def backToCreateFunctionSuccess():
    membershipCreationSuccess.destroy()


def backToCreateFunctionError():
    membershipCreationError.destroy()


def membershipDeletionToMenuPage():
    membershipDeletionPage.destroy()
    membershipPageFunction()


def membershipDeletionPageFunction():
    global membershipDeletionPage
    membershipDeletionPage = Tk()
    membershipDeletionPage.geometry(pageGeometry)
    membershipDeletionPage.title("Membership Deletion")
    membershipDeletionPage_topBanner = Label(
        membershipDeletionPage, text="To Delete Member, Please Enter Requested Information Below:", font=fontSize)
    membershipDeletionPage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)
    membershipID_label = Label(
        membershipDeletionPage, text="Membership ID", font=fontSize)
    membershipID_label.place(relx=0.2, rely=0.5, anchor=CENTER)
    membershipID = StringVar()
    global deletemembershipID_entry
    deletemembershipID_entry = Entry(
        membershipDeletionPage, textvariable=membershipID)
    deletemembershipID_entry.place(relx=0.4, rely=0.5, anchor=CENTER)

    deleteMember_btn = Button(membershipDeletionPage, height=bannerHeight, width=buttonWidth,
                              command=deleteMember, text="Delete Member", font=fontSize)
    deleteMember_btn.place(relx=0.3, rely=0.8, anchor=CENTER)
    backToMembershipMenu_btn = Button(membershipDeletionPage, height=bannerHeight, width=buttonWidth,
                                      command=membershipDeletionToMenuPage, text="Back To\nMembership Menu", font=fontSize)
    backToMembershipMenu_btn.place(relx=0.7, rely=0.8, anchor=CENTER)


def backToDeleteFunctionSuccess():
    membershipDeletionSuccess.destroy()


def backToDeleteFunctionError():
    membershipDeletionError.destroy()


def deleteMember():
    # SUCCESS
    global membershipDeletionSuccess
    membershipDeletionSuccess = Tk()
    membershipDeletionSuccess.geometry(confirmPageGeometry)
    membershipDeletionSuccess.title("Membership Deletion Success")
    membershipDeletionSuccess_label = Label(
        membershipDeletionSuccess, text="Please Confirm Details to\nBe Correct", font=fontSize)
    membershipDeletionSuccess_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    MembershipID = deletemembershipID_entry.get()
    Name = showName(MembershipID)
    Faculty = showFaculty(MembershipID)
    PhoneNumber = showPhoneNumber(MembershipID)
    EmailAddress = showEmailAddress(MembershipID)

    membershipID_label = Label(
        membershipDeletionSuccess, text="Member ID : {}".format(MembershipID), font=buttonFontSize)
    membershipID_label.place(relx=0.1, rely=0.3)

    name_label = Label(
        membershipDeletionSuccess, text="Name : {}".format(Name), font=buttonFontSize)
    name_label.place(relx=0.1, rely=0.4)

    faculty_label = Label(
        membershipDeletionSuccess, text="Faculty : {}".format(Faculty), font=buttonFontSize)
    faculty_label.place(relx=0.1, rely=0.5)

    phoneNumber_label = Label(
        membershipDeletionSuccess, text="Phone Number : {}".format(PhoneNumber), font=buttonFontSize)
    phoneNumber_label.place(relx=0.1, rely=0.6)

    emailAddress_label = Label(
        membershipDeletionSuccess, text="Email Address : {}".format(EmailAddress), font=buttonFontSize)
    emailAddress_label.place(relx=0.1, rely=0.7)

    confirmDeletion_btn = Button(membershipDeletionSuccess, height=bannerHeight,
                                 width=optionButtonWidth, command=memberdeleted, text="Confirm\nDeletion", font=buttonFontSize)
    confirmDeletion_btn.place(relx=0.25, rely=0.9, anchor=CENTER)
    backToDeleteFunction_btn = Button(membershipDeletionSuccess, height=bannerHeight, width=optionButtonWidth,
                                      command=backToDeleteFunctionSuccess, text="Back to\nDelete Function", font=buttonFontSize)
    backToDeleteFunction_btn.place(relx=0.75, rely=0.9, anchor=CENTER)


def memberdeleted():
    membershipID = deletemembershipID_entry.get()

    if deleteMembership(membershipID):
        membershipDeletionSuccess.destroy()
        pass
    else:
        # ERROR
        global membershipDeletionError
        membershipDeletionError = Tk()
        membershipDeletionError.geometry(confirmPageGeometry)
        membershipDeletionError.title("Membership Deletion Error")
        membershipDeletionError_label = Label(
            membershipDeletionError, text="Error!", font=fontSize)
        membershipDeletionError_label.place(
            relx=0.5, rely=0.3, anchor=CENTER)
        membershipDeletionErrornote_label = Label(
            membershipDeletionError, text="No member\nMember has loans,\nreservations or outstanding fines.", font=fontSize)
        membershipDeletionErrornote_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToDeleteFunction_btn = Button(membershipDeletionError, height=bannerHeight, width=buttonWidth,
                                          command=backToDeleteFunctionError, text="Back to\nDelete Function", font=buttonFontSize)
        backToDeleteFunction_btn.place(relx=0.5, rely=0.8, anchor=CENTER)


def membershipUpdateToMenuPage():
    membershipUpdatePage.destroy()
    membershipPageFunction()


def membershipUpdateInfoToMenuPage():
    membershipUpdateIDPage.destroy()


def membershipUpdatePageFunction():
    global membershipUpdatePage
    membershipUpdatePage = Tk()
    membershipUpdatePage.geometry(pageGeometry)
    membershipUpdatePage.title("Membership Update")
    membershipUpdatePage_topBanner = Label(
        membershipUpdatePage, text="To Update a Member, Please Enter Membership ID Below:", font=fontSize)
    membershipUpdatePage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)
    membershipID_label = Label(
        membershipUpdatePage, text="Membership ID", font=fontSize)
    membershipID_label.place(relx=0.2, rely=0.5, anchor=CENTER)
    membershipID = StringVar()
    global updateMembershipID_entry
    updateMembershipID_entry = Entry(
        membershipUpdatePage, textvariable=membershipID)
    updateMembershipID_entry.place(relx=0.4, rely=0.5, anchor=CENTER)

    updateMember_btn = Button(membershipUpdatePage, height=bannerHeight, width=buttonWidth,
                              command=updateMemberID, text="Update Member", font=fontSize)
    updateMember_btn.place(relx=0.3, rely=0.8, anchor=CENTER)
    backToMembershipMenu_btn = Button(membershipUpdatePage, height=bannerHeight, width=buttonWidth,
                                      command=membershipUpdateToMenuPage, text="Back To\nMembership Menu", font=fontSize)
    backToMembershipMenu_btn.place(relx=0.7, rely=0.8, anchor=CENTER)


def updateMemberID():
    global membershipUpdateIDPage
    membershipUpdateIDPage = Tk()
    membershipUpdateIDPage.geometry(pageGeometry)
    membershipUpdateIDPage.title("Membership Update")
    membershipUpdateIDPage_topBanner = Label(
        membershipUpdateIDPage, text="Please Enter Requested Information Below:", font=fontSize)
    membershipUpdateIDPage_topBanner.place(
        relx=0.5, rely=0.1, anchor=CENTER)

    membershipID_label = Label(
        membershipUpdateIDPage, text="Membership ID", font=fontSize)
    membershipID_label.place(relx=0.2, rely=0.25, anchor=CENTER)
    membershipID = updateMembershipID_entry.get()
    membershipID_label = Label(
        membershipUpdateIDPage, text="{}".format(membershipID), font=fontSize)
    membershipID_label.place(relx=0.4, rely=0.25, anchor=CENTER)

    name_label = Label(
        membershipUpdateIDPage, text="Name", font=fontSize)
    name_label.place(relx=0.2, rely=0.35, anchor=CENTER)
    name = StringVar()
    global updateName_entry
    updateName_entry = Entry(
        membershipUpdateIDPage, textvariable=name)
    updateName_entry.place(relx=0.4, rely=0.35, anchor=CENTER)

    faculty_label = Label(
        membershipUpdateIDPage, text="Faculty", font=fontSize)
    faculty_label.place(relx=0.2, rely=0.45, anchor=CENTER)
    faculty = StringVar()
    global updateFaculty_entry
    updateFaculty_entry = Entry(
        membershipUpdateIDPage, textvariable=faculty)
    updateFaculty_entry.place(relx=0.4, rely=0.45, anchor=CENTER)

    phonenumber_label = Label(
        membershipUpdateIDPage, text="Phone Number", font=fontSize)
    phonenumber_label.place(relx=0.2, rely=0.55, anchor=CENTER)
    phonenumber = float()
    global updatePhonenumber_entry
    updatePhonenumber_entry = Entry(
        membershipUpdateIDPage, textvariable=phonenumber)
    updatePhonenumber_entry.place(relx=0.4, rely=0.55, anchor=CENTER)

    email_label = Label(
        membershipUpdateIDPage, text="Email Address", font=fontSize)
    email_label.place(relx=0.2, rely=0.65, anchor=CENTER)
    email = StringVar()
    global updateEmail_entry
    updateEmail_entry = Entry(
        membershipUpdateIDPage, textvariable=email)
    updateEmail_entry.place(relx=0.4, rely=0.65, anchor=CENTER)

    updateMember_btn = Button(membershipUpdateIDPage, height=bannerHeight, width=buttonWidth,
                              command=updateMemberConfirmpage, text="Update Member", font=fontSize)
    updateMember_btn.place(relx=0.3, rely=0.8, anchor=CENTER)
    backToMembershipMenu_btn = Button(membershipUpdateIDPage, height=bannerHeight, width=buttonWidth,
                                      command=membershipUpdateInfoToMenuPage, text="Back To\nMembership Menu", font=fontSize)
    backToMembershipMenu_btn.place(relx=0.7, rely=0.8, anchor=CENTER)


def updateMemberConfirmpage():
    MembershipID = updateMembershipID_entry.get()
    Name = updateName_entry.get()
    Faculty = updateFaculty_entry.get()
    PhoneNumber = updatePhonenumber_entry.get()
    EmailAddress = updateEmail_entry.get()
    global membershipUpdateConfirm
    membershipUpdateConfirm = Tk()
    membershipUpdateConfirm.geometry(confirmPageGeometry)
    membershipUpdateConfirm.title("Membership Update Confirm")
    membershipUpdateConfirm_label = Label(
        membershipUpdateConfirm, text="Please Confirm Updated\n Details to Be Correct", font=fontSize)
    membershipUpdateConfirm_label.place(
        relx=0.5, rely=0.1, anchor=CENTER)

    membershipID_label = Label(
        membershipUpdateConfirm, text="Member ID : {}".format(MembershipID), font=buttonFontSize)
    membershipID_label.place(relx=0.1, rely=0.3)

    name_label = Label(
        membershipUpdateConfirm, text="Name : {}".format(Name), font=buttonFontSize)
    name_label.place(relx=0.1, rely=0.4)

    faculty_label = Label(
        membershipUpdateConfirm, text="Faculty : {}".format(Faculty), font=buttonFontSize)
    faculty_label.place(relx=0.1, rely=0.5)

    phoneNumber_label = Label(
        membershipUpdateConfirm, text="Phone Number : {}".format(PhoneNumber), font=buttonFontSize)
    phoneNumber_label.place(relx=0.1, rely=0.6)

    emailAddress_label = Label(
        membershipUpdateConfirm, text="Email Address : {}".format(EmailAddress), font=buttonFontSize)
    emailAddress_label.place(relx=0.1, rely=0.7)

    confirmUpdate_btn = Button(membershipUpdateConfirm, height=bannerHeight, width=optionButtonWidth,
                               command=membershipUpdateInfoConfirm, text="Confirm\nUpdate", font=buttonFontSize)
    confirmUpdate_btn.place(relx=0.25, rely=0.9, anchor=CENTER)
    backToUpdateFunction_btn = Button(membershipUpdateConfirm, height=bannerHeight, width=optionButtonWidth,
                                      command=updateConfirmToUpdateFunction, text="Back to\nUpdate Function", font=buttonFontSize)
    backToUpdateFunction_btn.place(relx=0.75, rely=0.9, anchor=CENTER)


def updateConfirmToUpdateFunction():
    membershipUpdateIDPage.destroy()
    membershipUpdateConfirm.destroy()


def membershipUpdateInfoConfirm():
    membershipUpdateConfirm.destroy()
    MembershipID = updateMembershipID_entry.get()
    Name = updateName_entry.get()
    Faculty = updateFaculty_entry.get()
    PhoneNumber = updatePhonenumber_entry.get()
    EmailAddress = updateEmail_entry.get()

    if updateMembership(MembershipID, Name, Faculty, PhoneNumber, EmailAddress):
        global membershipUpdateSuccess
        membershipUpdateSuccess = Tk()
        membershipUpdateSuccess.geometry(confirmPageGeometry)
        membershipUpdateSuccess.title("Membership Update Success")
        membershipUpdateSuccess_label = Label(
            membershipUpdateSuccess, text="Success!", font=fontSize)
        membershipUpdateSuccess_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        membershipUpdateSuccessnote_label = Label(
            membershipUpdateSuccess, text="ALS Membership Updated.", font=fontSize)
        membershipUpdateSuccessnote_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        createAnotherMember_btn = Button(membershipUpdateSuccess, height=bannerHeight, width=optionButtonWidth,
                                         command=toMemberCreation, text="Create Another\nMember", font=buttonFontSize)
        createAnotherMember_btn.place(relx=0.25, rely=0.8, anchor=CENTER)
        backToUpdateFunction_btn = Button(membershipUpdateSuccess, height=bannerHeight, width=optionButtonWidth,
                                          command=backToUpdateFunctionSuccess, text="Back to\nUpdate Function", font=buttonFontSize)
        backToUpdateFunction_btn.place(relx=0.75, rely=0.8, anchor=CENTER)

    else:
        global membershipUpdateError
        membershipUpdateError = Tk()
        membershipUpdateError.geometry(confirmPageGeometry)
        membershipUpdateError.title("Membership Update Error")
        membershipUpdateError_label = Label(
            membershipUpdateError, text="Error!", font=fontSize)
        membershipUpdateError_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        membershipUpdateErrornote_label = Label(
            membershipUpdateError, text="Member does not exist; or\n Missing or\nIncomplete fields.", font=buttonFontSize)
        membershipUpdateErrornote_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToDeleteFunction_btn = Button(membershipUpdateError, height=bannerHeight, width=buttonWidth,
                                          command=backToUpdateFunctionError, text="Back to\nUpdate Function", font=buttonFontSize)
        backToDeleteFunction_btn.place(relx=0.5, rely=0.8, anchor=CENTER)


def toMemberCreation():
    membershipUpdatePage.destroy()
    membershipUpdateIDPage.destroy()
    membershipUpdateSuccess.destroy()
    membershipCreationPageFunction()


def backToUpdateFunctionSuccess():
    membershipUpdateIDPage.destroy()
    membershipUpdateSuccess.destroy()


def backToUpdateFunctionError():
    membershipUpdateIDPage.destroy()
    membershipUpdateError.destroy()


##########################################
# BookPage


def bookToAcquisition():
    bookPage.destroy()
    bookAcquisitionPageFunction()


def bookToWithdrawal():
    bookPage.destroy()
    bookWithdrawalPageFunction()


def bookToMainPage():
    bookPage.destroy()
    mainPageFunction()


def bookPageFunction():
    global bookPage
    bookPage = Tk()
    bookPage.geometry(pageGeometry)
    bookPage.title("Book")
    bookPage_topBanner = Label(
        bookPage, text="Select one of the Options below:", font=fontSize)
    bookPage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    acquisition_btn = Button(bookPage, height=bannerHeight, width=optionButtonWidth,
                             command=bookToAcquisition, text="4.Acquisition", font=fontSize)
    acquisition_btn.place(relx=0.5, rely=0.4, anchor=CENTER)
    membershipCreation_label = Label(
        bookPage, text="Book Acquisition", font=fontSize)
    membershipCreation_label.place(relx=0.8, rely=0.4, anchor=CENTER)

    withdrawal_btn = Button(bookPage, height=bannerHeight, width=optionButtonWidth,
                            command=bookToWithdrawal, text="5.Withdrawal", font=fontSize)
    withdrawal_btn.place(relx=0.5, rely=0.6, anchor=CENTER)
    bookWithdrawal_label = Label(
        bookPage, text="Book Withdrawal", font=fontSize)
    bookWithdrawal_label.place(relx=0.8, rely=0.6, anchor=CENTER)

    backToMain_btn = Button(bookPage, height=bannerHeight, width=bannerWidth,
                            command=bookToMainPage, text="Back To Main Menu", font=fontSize)
    backToMain_btn.place(relx=0.5, rely=0.9, anchor=CENTER)


def acquisitionToBooksMenu():
    acquisitionPage.destroy()
    bookPageFunction()


def bookAcquisitionPageFunction():
    global acquisitionPage
    acquisitionPage = Tk()
    acquisitionPage.geometry(pageGeometry)
    acquisitionPage.title("Book Acquisition")
    acquisitionPage_topBanner = Label(
        acquisitionPage, text="For New Book Acquisition, Please Enter Required Information Below:", font=fontSize)
    acquisitionPage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    accessionNumber_label = Label(
        acquisitionPage, text="Accession Number", font=fontSize)
    accessionNumber_label.place(relx=0.2, rely=0.25, anchor=CENTER)
    accessionNumber = StringVar()
    accessionNumber_entry = Entry(
        acquisitionPage, textvariable=accessionNumber)
    accessionNumber_entry.place(relx=0.4, rely=0.25, anchor=CENTER)

    title_label = Label(
        acquisitionPage, text="Title", font=fontSize)
    title_label.place(relx=0.2, rely=0.35, anchor=CENTER)
    title = StringVar()
    title_entry = Entry(
        acquisitionPage, textvariable=title)
    title_entry.place(relx=0.4, rely=0.35, anchor=CENTER)

    authors_label = Label(
        acquisitionPage, text="Authors", font=fontSize)
    authors_label.place(relx=0.2, rely=0.45, anchor=CENTER)
    authors = StringVar()
    authors_entry = Entry(
        acquisitionPage, textvariable=authors)
    authors_entry.place(relx=0.4, rely=0.45, anchor=CENTER)

    ISBN_label = Label(
        acquisitionPage, text="ISBN", font=fontSize)
    ISBN_label.place(relx=0.2, rely=0.55, anchor=CENTER)
    ISBN = float()
    ISBN_entry = Entry(
        acquisitionPage, textvariable=ISBN)
    ISBN_entry.place(relx=0.4, rely=0.55, anchor=CENTER)

    publisher_label = Label(
        acquisitionPage, text="Publisher", font=fontSize)
    publisher_label.place(relx=0.2, rely=0.65, anchor=CENTER)
    publisher = StringVar()
    publisher_entry = Entry(
        acquisitionPage, textvariable=publisher)
    publisher_entry.place(relx=0.4, rely=0.65, anchor=CENTER)

    publicationYear_label = Label(
        acquisitionPage, text="Publication Year", font=fontSize)
    publicationYear_label.place(relx=0.2, rely=0.75, anchor=CENTER)
    publicationYear = StringVar()
    publicationYear_entry = Entry(
        acquisitionPage, textvariable=publicationYear)
    publicationYear_entry.place(relx=0.4, rely=0.75, anchor=CENTER)

    def bookAcquisitionConfirmPage():
        accessionNumber = accessionNumber_entry.get()
        title = title_entry.get()
        authors = authors_entry.get()
        ISBN = ISBN_entry.get()
        publisher = publisher_entry.get()
        publicationYear = publicationYear_entry.get()

        if bookAcquisition(accessionNumber, title, authors, ISBN, publisher, publicationYear):
            # SUCCESS
            global bookAcquisitionSuccess
            bookAcquisitionSuccess = Tk()
            bookAcquisitionSuccess.geometry(confirmPageGeometry)
            bookAcquisitionSuccess.title("Book Acquisition Success")
            bookAcquisitionSuccess_label = Label(
                bookAcquisitionSuccess, text="Success!", font=fontSize)
            bookAcquisitionSuccess_label.place(
                relx=0.5, rely=0.3, anchor=CENTER)
            bookAcquisitionSuccessNote_label = Label(
                bookAcquisitionSuccess, text="ALS Membership Updated.", font=fontSize)
            bookAcquisitionSuccessNote_label.place(
                relx=0.5, rely=0.5, anchor=CENTER)
            backToAcquisition_btn = Button(bookAcquisitionSuccess, height=bannerHeight, width=buttonWidth,
                                           command=backToAcquisitionSuccess, text="Back to\nAcquisition Function", font=buttonFontSize)
            backToAcquisition_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

        else:
            # ERROR
            global bookAcquisitionError
            bookAcquisitionError = Tk()
            bookAcquisitionError.geometry(confirmPageGeometry)
            bookAcquisitionError.title("Book Acquisition Error")
            bookAcquisitionError_label = Label(
                bookAcquisitionError, text="Error!", font=fontSize)
            bookAcquisitionError_label.place(relx=0.5, rely=0.3, anchor=CENTER)
            bookAcquisitionErrorNote_label = Label(
                bookAcquisitionError, text="Book already added;\nDuplicate, Missing or\nIncomplete fields.", font=fontSize)
            bookAcquisitionErrorNote_label.place(
                relx=0.5, rely=0.5, anchor=CENTER)
            backToAcquisition_btn = Button(bookAcquisitionError, height=bannerHeight, width=buttonWidth,
                                           command=backToAcquisitionError, text="Back to\nAcquisition Function", font=buttonFontSize)
            backToAcquisition_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    addNewBook_btn = Button(acquisitionPage, height=bannerHeight, width=buttonWidth,
                            command=bookAcquisitionConfirmPage, text="Add New Book", font=fontSize)
    addNewBook_btn.place(relx=0.3, rely=0.9, anchor=CENTER)
    backToBooksMenu_btn = Button(acquisitionPage, height=bannerHeight, width=buttonWidth,
                                 command=acquisitionToBooksMenu, text="Back To Books Menu", font=fontSize)
    backToBooksMenu_btn.place(relx=0.7, rely=0.9, anchor=CENTER)


def backToAcquisitionSuccess():
    bookAcquisitionSuccess.destroy()


def backToAcquisitionError():
    bookAcquisitionError.destroy()


def withdrawToBooksMenu():
    bookWithdrawalPage.destroy()
    bookPageFunction()


def bookWithdrawalPageFunction():
    global bookWithdrawalPage
    bookWithdrawalPage = Tk()
    bookWithdrawalPage.geometry(pageGeometry)
    bookWithdrawalPage.title("Book Withdrawal")
    bookWithdrawalPage_topBanner = Label(
        bookWithdrawalPage, text="To Remove Outdated Books From System, Please Enter Required Information:", font=fontSize)
    bookWithdrawalPage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)
    bookWithdrawalPage_label = Label(
        bookWithdrawalPage, text="Accession Number", font=fontSize)
    bookWithdrawalPage_label.place(relx=0.2, rely=0.5, anchor=CENTER)
    accessionNumber = StringVar()
    global withdrawalAccessionNumber_entry
    withdrawalAccessionNumber_entry = Entry(
        bookWithdrawalPage, textvariable=accessionNumber)
    withdrawalAccessionNumber_entry.place(relx=0.4, rely=0.5, anchor=CENTER)

    withdrawBook_btn = Button(bookWithdrawalPage, height=bannerHeight, width=buttonWidth,
                              command=bookWithdrawConfirmFunction, text="Withdraw Book", font=fontSize)
    withdrawBook_btn.place(relx=0.3, rely=0.8, anchor=CENTER)
    backToBooksMenu_btn = Button(bookWithdrawalPage, height=bannerHeight, width=buttonWidth,
                                 command=withdrawToBooksMenu, text="Back To\nMembership Menu", font=fontSize)
    backToBooksMenu_btn.place(relx=0.7, rely=0.8, anchor=CENTER)


def backToWithdrawalSuccess():
    bookWithdrawSuccess.destroy()


def backToWithdrawalErrorLoan():
    bookWithdrawErrorLoan.destroy()


def backToWithdrawalErrorReserve():
    bookWithdrawErrorReserve.destroy()


def backToWithdrawalErrorNoBook():
    bookWithdrawErrorNoBook.destroy()


def bookWithdrawConfirmFunction():
    global bookWithdrawSuccess
    bookWithdrawSuccess = Tk()
    bookWithdrawSuccess.geometry(confirmPageGeometry)
    bookWithdrawSuccess.title("Book Withdraw Success")
    bookWithdrawSuccess_label = Label(
        bookWithdrawSuccess, text="Please Confirm Details to\nBe Correct", font=fontSize)
    bookWithdrawSuccess_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    AccessionNumber = withdrawalAccessionNumber_entry.get()
    Title = showTitle(AccessionNumber)
    Authors = showAuthors(AccessionNumber)
    ISBN = showISBN(AccessionNumber)
    Publisher = showPublisher(AccessionNumber)
    PublicationYear = showYear(AccessionNumber)

    accessionNumber_label = Label(
        bookWithdrawSuccess, text="Accession Number : {}".format(AccessionNumber), font=buttonFontSize)
    accessionNumber_label.place(relx=0.1, rely=0.2)

    title_lable = Label(
        bookWithdrawSuccess, text="Title : {}".format(Title), font=buttonFontSize)
    title_lable.place(relx=0.1, rely=0.3)

    authors_label = Label(
        bookWithdrawSuccess, text="Authors : {}".format(Authors), font=buttonFontSize)
    authors_label.place(relx=0.1, rely=0.4)

    ISBN_label = Label(
        bookWithdrawSuccess, text="ISBN : {}".format(ISBN), font=buttonFontSize)
    ISBN_label.place(relx=0.1, rely=0.5)

    publisher_label = Label(
        bookWithdrawSuccess, text="Publisher : {}".format(Publisher), font=buttonFontSize)
    publisher_label.place(relx=0.1, rely=0.6)

    publicationYear_label = Label(
        bookWithdrawSuccess, text="Publication Year : {}".format(PublicationYear), font=buttonFontSize)
    publicationYear_label.place(relx=0.1, rely=0.7)

    bookWithdrawalConfirm_btn = Button(bookWithdrawSuccess, height=bannerHeight, width=optionButtonWidth,
                                       command=bookWithdrawalConfirm, text="Confirm\nWithdrawal", font=buttonFontSize)
    bookWithdrawalConfirm_btn.place(relx=0.25, rely=0.9, anchor=CENTER)
    backToWithdrawalFunction_btn = Button(bookWithdrawSuccess, height=bannerHeight, width=optionButtonWidth,
                                          command=backToWithdrawalSuccess, text="Back to\nWithdrawal Function", font=buttonFontSize)
    backToWithdrawalFunction_btn.place(relx=0.75, rely=0.9, anchor=CENTER)


def bookWithdrawalConfirm():
    accessionNumber = withdrawalAccessionNumber_entry.get()

    if bookWithLoan(accessionNumber):
        # ERROR Loan
        global bookWithdrawErrorLoan
        bookWithdrawErrorLoan = Tk()
        bookWithdrawErrorLoan.geometry(confirmPageGeometry)
        bookWithdrawErrorLoan.title("Book Withdraw Error - Loan")
        bookWithdrawErrorLoan_label = Label(
            bookWithdrawErrorLoan, text="Error!", font=fontSize)
        bookWithdrawErrorLoan_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        bookWithdrawErrorLoanNote_label = Label(
            bookWithdrawErrorLoan, text="Book is currently on Loan.", font=fontSize)
        bookWithdrawErrorLoanNote_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToAcquisition_btn = Button(bookWithdrawErrorLoan, height=bannerHeight, width=buttonWidth,
                                       command=backToWithdrawalErrorLoan, text="Back to\nWithdrawal Function", font=buttonFontSize)
        backToAcquisition_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    elif bookWithReserve(accessionNumber):
        # ERROR Reserved
        global bookWithdrawErrorReserve
        bookWithdrawErrorReserve = Tk()
        bookWithdrawErrorReserve.geometry(confirmPageGeometry)
        bookWithdrawErrorReserve.title("Book Withdraw Error - Reserve")
        bookWithdrawErrorReserve_label = Label(
            bookWithdrawErrorReserve, text="Error!", font=fontSize)
        bookWithdrawErrorReserve_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        bookWithdrawErrorReserveNote_label = Label(
            bookWithdrawErrorReserve, text="Book is currently Reserved.", font=fontSize)
        bookWithdrawErrorReserveNote_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToAcquisition_btn = Button(bookWithdrawErrorReserve, height=bannerHeight, width=buttonWidth,
                                       command=backToWithdrawalErrorReserve, text="Back to\nWithdrawal\nFunction", font=buttonFontSize)
        backToAcquisition_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    elif successWithdrawal(accessionNumber):
        bookWithdrawSuccess.destroy()

    else:
        backToWithdrawalSuccess()
        global bookWithdrawErrorNoBook
        bookWithdrawErrorNoBook = Tk()
        bookWithdrawErrorNoBook.geometry(confirmPageGeometry)
        bookWithdrawErrorNoBook.title("Book Withdraw Error - No Book")
        bookWithdrawErrorNoBook_label = Label(
            bookWithdrawErrorNoBook, text="Error!", font=fontSize)
        bookWithdrawErrorNoBook_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        bookWithdrawErrorNoBookNote_label = Label(
            bookWithdrawErrorNoBook, text="Book does not exist", font=fontSize)
        bookWithdrawErrorNoBookNote_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToAcquisition_btn = Button(bookWithdrawErrorNoBook, height=bannerHeight, width=buttonWidth,
                                       command=backToWithdrawalErrorNoBook, text="Back to\nWithdrawal Function", font=buttonFontSize)
        backToAcquisition_btn.place(relx=0.5, rely=0.8, anchor=CENTER)


##########################################
# Loans page
def loansToBorrow():
    loansPage.destroy()
    borrowPageFunction()


def loansToReturn():
    loansPage.destroy()
    returnPageFunction()


def loansToMainPage():
    loansPage.destroy()
    mainPageFunction()


def loansPageFunction():
    global loansPage
    loansPage = Tk()
    loansPage.geometry(pageGeometry)
    loansPage.title("Loans")
    loansPage_topBanner = Label(
        loansPage, text="Select one of the Options below:", font=fontSize)
    loansPage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    borrow_btn = Button(loansPage, height=bannerHeight, width=optionButtonWidth,
                        command=loansToBorrow, text="6.Borrow", font=fontSize)
    borrow_btn.place(relx=0.5, rely=0.4, anchor=CENTER)
    bookBorrow_label = Label(
        loansPage, text="Book Borrowing", font=fontSize)
    bookBorrow_label.place(relx=0.8, rely=0.4, anchor=CENTER)

    return_btn = Button(loansPage, height=bannerHeight, width=optionButtonWidth,
                        command=loansToReturn, text="7.Return", font=fontSize)
    return_btn.place(relx=0.5, rely=0.6, anchor=CENTER)
    bookReturn_label = Label(
        loansPage, text="Book Returning", font=fontSize)
    bookReturn_label.place(relx=0.8, rely=0.6, anchor=CENTER)

    backToMain_btn = Button(loansPage, height=bannerHeight, width=bannerWidth,
                            command=loansToMainPage, text="Back To Main Menu", font=fontSize)
    backToMain_btn.place(relx=0.5, rely=0.9, anchor=CENTER)


def borrowToLoansMenu():
    borrowPage.destroy()
    loansPageFunction()


def borrowPageFunction():
    global borrowPage
    borrowPage = Tk()
    borrowPage.geometry(pageGeometry)
    borrowPage.title("Borrow Book")
    borrowPage_topBanner = Label(
        borrowPage, text="To Borrow a Book, Please Enter Information Below:", font=fontSize)
    borrowPage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    accessionNumber_label = Label(
        borrowPage, text="Accession Number", font=fontSize)
    accessionNumber_label.place(relx=0.2, rely=0.25, anchor=CENTER)
    accessionNumber = StringVar()
    global borrowAccessionNumber_entry
    borrowAccessionNumber_entry = Entry(
        borrowPage, textvariable=accessionNumber)
    borrowAccessionNumber_entry.place(relx=0.4, rely=0.25, anchor=CENTER)

    membershipID_label = Label(
        borrowPage, text="Membership ID", font=fontSize)
    membershipID_label.place(relx=0.2, rely=0.35, anchor=CENTER)
    membershipID = StringVar()
    global borrowMembershipID_entry
    borrowMembershipID_entry = Entry(
        borrowPage, textvariable=membershipID)
    borrowMembershipID_entry.place(relx=0.4, rely=0.35, anchor=CENTER)

    borrowBook_btn = Button(borrowPage, height=bannerHeight, width=buttonWidth,
                            command=borrowBookConfirmFunction, text="Borrow Book", font=fontSize)
    borrowBook_btn.place(relx=0.3, rely=0.8, anchor=CENTER)
    backToLoansMenu_btn = Button(borrowPage, height=bannerHeight, width=buttonWidth,
                                 command=borrowToLoansMenu, text="Back To Loans Menu", font=fontSize)
    backToLoansMenu_btn.place(relx=0.7, rely=0.8, anchor=CENTER)


def confirmBorrow():
    bookBorrowSuccess.destroy()


def backToBorrowConfirm():
    bookBorrowSuccess.destroy()


def backToBorrowSuccess():
    bookBorrowSuccess.destroy()


def backToBorrowErrorLoan():
    bookBorrowErrorLoan.destroy()


def backToBorrowErrorQuota():
    bookBorrowErrorQuota.destroy()


def backToBorrowErrorFine():
    bookBorrowErrorFine.destroy()


def backToBorrowErrorReservedEarlier():
    bookBorrowErrorReservedEarlier.destroy()


def borrowBookConfirmFunction():
    global bookBorrowSuccess
    bookBorrowSuccess = Tk()
    bookBorrowSuccess.geometry(confirmPageGeometry)
    bookBorrowSuccess.title("Book Borrow Success")
    bookBorrowSuccess_label = Label(
        bookBorrowSuccess, text="Confirm Loan Details to\nBe Correct", font=fontSize)
    bookBorrowSuccess_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    AccessionNumber = borrowAccessionNumber_entry.get()
    Title = showTitle(AccessionNumber)
    borrowDate = datetime.now()
    BorrowDate = borrowDate.strftime("%Y-%m-%d")
    MembershipID = borrowMembershipID_entry.get()
    MemberName = showName(MembershipID)
    dueDate = datetime.now() + timedelta(days=14)
    DueDate = dueDate.strftime("%Y-%m-%d")

    accessionNumber_label = Label(
        bookBorrowSuccess, text="Member ID : {}".format(AccessionNumber), font=buttonFontSize)
    accessionNumber_label.place(relx=0.1, rely=0.2)

    title_label = Label(
        bookBorrowSuccess, text="Book Title : {}".format(Title), font=buttonFontSize)
    title_label.place(relx=0.1, rely=0.3)

    borrowDate_label = Label(
        bookBorrowSuccess, text="Borrow Date : {}".format(BorrowDate), font=buttonFontSize)
    borrowDate_label.place(relx=0.1, rely=0.4)

    membershipID_label = Label(
        bookBorrowSuccess, text="Membership ID : {}".format(MembershipID), font=buttonFontSize)
    membershipID_label.place(relx=0.1, rely=0.5)

    memberName_label = Label(
        bookBorrowSuccess, text="Member Name : {}".format(MemberName), font=buttonFontSize)
    memberName_label.place(relx=0.1, rely=0.6)

    dueDate_label = Label(
        bookBorrowSuccess, text="Due Date : {}".format(DueDate), font=buttonFontSize)
    dueDate_label.place(relx=0.1, rely=0.7)

    confirmBorrow_btn = Button(bookBorrowSuccess, height=bannerHeight, width=optionButtonWidth,
                               command=confirmBorrow, text="Confirm\nLoan", font=buttonFontSize)
    confirmBorrow_btn.place(relx=0.25, rely=0.9, anchor=CENTER)
    backToBorrow_btn = Button(bookBorrowSuccess, height=bannerHeight, width=optionButtonWidth,
                              command=backToBorrowConfirm, text="Back to\nBorrow Function", font=buttonFontSize)
    backToBorrow_btn.place(relx=0.75, rely=0.9, anchor=CENTER)


def confirmBorrow():
    membershipID = borrowMembershipID_entry.get()
    accessionNumber = borrowAccessionNumber_entry.get()

    if LoanedBook(membershipID, accessionNumber):
        backToBorrowSuccess()
        loanUntilDate = showLoanDate(accessionNumber)
        # ERROR Loan
        global bookBorrowErrorLoan
        bookBorrowErrorLoan = Tk()
        bookBorrowErrorLoan.geometry(confirmPageGeometry)
        bookBorrowErrorLoan.title("Book Borrow Error - Loan")
        bookBorrowErrorLoan_label = Label(
            bookBorrowErrorLoan, text="Error!", font=fontSize)
        bookBorrowErrorLoan_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        bookBorrowErrorLoanNote_label = Label(
            bookBorrowErrorLoan, text="Book is currently on Loan until:\n{}".format(loanUntilDate), font=fontSize)
        bookBorrowErrorLoanNote_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToBorrow_btn = Button(bookBorrowErrorLoan, height=bannerHeight, width=buttonWidth,
                                  command=backToBorrowErrorLoan, text="Back to\nBorrow Function", font=buttonFontSize)
        backToBorrow_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    elif MemQuotaExceeded(membershipID, accessionNumber):
        backToBorrowSuccess()
        # ERROR quota
        global bookBorrowErrorQuota
        bookBorrowErrorQuota = Tk()
        bookBorrowErrorQuota.geometry(confirmPageGeometry)
        bookBorrowErrorQuota.title("Book Borrow Error - Quota")
        bookBorrowErrorQuota_label = Label(
            bookBorrowErrorQuota, text="Error!", font=fontSize)
        bookBorrowErrorQuota_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        bookBorrowErrorQuotaNote_label = Label(
            bookBorrowErrorQuota, text="Member loan quota exceeded", font=fontSize)
        bookBorrowErrorQuotaNote_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToBorrow_btn = Button(bookBorrowErrorQuota, height=bannerHeight, width=buttonWidth,
                                  command=backToBorrowErrorQuota, text="Back to\nBorrow Function", font=buttonFontSize)
        backToBorrow_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    elif memFined(membershipID, accessionNumber):
        backToBorrowSuccess()
        # ERROR fine
        global bookBorrowErrorFine
        bookBorrowErrorFine = Tk()
        bookBorrowErrorFine.geometry(confirmPageGeometry)
        bookBorrowErrorFine.title("Book Borrow Error - Fine")
        bookBorrowErrorFine_label = Label(
            bookBorrowErrorFine, text="Error!", font=fontSize)
        bookBorrowErrorFine_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        bookBorrowErrorFineNote_label = Label(
            bookBorrowErrorFine, text="Member has outstanding fines", font=fontSize)
        bookBorrowErrorFineNote_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToBorrow_btn = Button(bookBorrowErrorFine, height=bannerHeight, width=buttonWidth,
                                  command=backToBorrowErrorFine, text="Back to\nBorrow Function", font=buttonFontSize)
        backToBorrow_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    elif bookOnReservation(membershipID, accessionNumber):
        backToBorrowSuccess()
        global bookBorrowErrorReservedEarlier
        bookBorrowErrorReservedEarlier = Tk()
        bookBorrowErrorReservedEarlier.geometry(confirmPageGeometry)
        bookBorrowErrorReservedEarlier.title(
            "Book Borrow Error - Reserved earlier")
        bookBorrowErrorReservedEarlier_label = Label(
            bookBorrowErrorReservedEarlier, text="Error!", font=fontSize)
        bookBorrowErrorReservedEarlier_label.place(
            relx=0.5, rely=0.3, anchor=CENTER)
        bookBorrowErrorReservedEarlierNote_label = Label(
            bookBorrowErrorReservedEarlier, text="Another Member reserved earlier", font=fontSize)
        bookBorrowErrorReservedEarlierNote_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToBorrow_btn = Button(bookBorrowErrorReservedEarlier, height=bannerHeight, width=buttonWidth,
                                  command=backToBorrowErrorReservedEarlier, text="Back to\nBorrow Function", font=buttonFontSize)
        backToBorrow_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    else:
        successBorrow(membershipID, accessionNumber)
        backToBorrowSuccess()


def backToReturnConfirm():
    bookReturnSuccess.destroy()


def backToReturn():
    bookReturnError.destroy()


def returnToLoansMenu():
    returnPage.destroy()
    loansPageFunction()


def returnPageFunction():
    global returnPage
    returnPage = Tk()
    returnPage.geometry(pageGeometry)
    returnPage.title("Return Book")
    returnPage_topBanner = Label(
        returnPage, text="To Return a Book, Please Enter Information Below:", font=fontSize)
    returnPage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    accessionNumber_label = Label(
        returnPage, text="Accession Number", font=fontSize)
    accessionNumber_label.place(relx=0.2, rely=0.25, anchor=CENTER)
    accessionNumber = StringVar()
    global returnAccessionNumber_entry
    returnAccessionNumber_entry = Entry(
        returnPage, textvariable=accessionNumber)
    returnAccessionNumber_entry.place(relx=0.4, rely=0.25, anchor=CENTER)

    returnDate_label = Label(
        returnPage, text="Return Date", font=fontSize)
    returnDate_label.place(relx=0.2, rely=0.35, anchor=CENTER)
    global returnDateStr
    returnDateStr = datetime.now()
    returnDateStr_label = Label(returnPage, text=returnDateStr.strftime(
        "%Y-%m-%d"), font=fontSize)
    returnDateStr_label.place(relx=0.4, rely=0.35, anchor=CENTER)

    returnBook_btn = Button(returnPage, height=bannerHeight, width=buttonWidth,
                            command=returnBookConfirmFunction, text="Return Book", font=fontSize)
    returnBook_btn.place(relx=0.3, rely=0.8, anchor=CENTER)
    backToLoansMenu_btn = Button(returnPage, height=bannerHeight, width=buttonWidth,
                                 command=returnToLoansMenu, text="Back To Loans Menu", font=fontSize)
    backToLoansMenu_btn.place(relx=0.7, rely=0.8, anchor=CENTER)


def returnBookConfirmFunction():
    global bookReturnSuccess
    bookReturnSuccess = Tk()
    bookReturnSuccess.geometry(confirmPageGeometry)
    bookReturnSuccess.title("Book Return Success")
    bookReturnSuccess_label = Label(
        bookReturnSuccess, text="Confirm Return Details\nTo Be Correct", font=fontSize)
    bookReturnSuccess_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    AccessionNumber = returnAccessionNumber_entry.get()
    Title = showTitle(AccessionNumber)
    MembershipID = showLoanedMembershipID(AccessionNumber)
    MemberName = showLoanedMemberName(AccessionNumber)
    returnDateStr = datetime.now()
    ReturnBookDate = returnDateStr.strftime("%Y-%m-%d")
    Fine = showFine(AccessionNumber)

    accessionNumber_label = Label(
        bookReturnSuccess, text="Member ID : {}".format(AccessionNumber), font=buttonFontSize)
    accessionNumber_label.place(relx=0.1, rely=0.2)

    title_label = Label(
        bookReturnSuccess, text="Book Title : {}".format(Title), font=buttonFontSize)
    title_label.place(relx=0.1, rely=0.3)

    membershipID_label = Label(
        bookReturnSuccess, text="Membership ID : {}".format(MembershipID), font=buttonFontSize)
    membershipID_label.place(relx=0.1, rely=0.4)

    memberName_label = Label(
        bookReturnSuccess, text="Member Name : {}".format(MemberName), font=buttonFontSize)
    memberName_label.place(relx=0.1, rely=0.5)

    returnDate_label = Label(
        bookReturnSuccess, text="Due Date : {}".format(ReturnBookDate), font=buttonFontSize)
    returnDate_label.place(relx=0.1, rely=0.6)

    fine_label = Label(
        bookReturnSuccess, text="Fine : ${}".format(Fine), font=buttonFontSize)
    fine_label.place(relx=0.1, rely=0.7)

    confirmReturn_btn = Button(bookReturnSuccess, height=bannerHeight, width=optionButtonWidth,
                               command=confirmReturn, text="Confirm\nReturn", font=buttonFontSize)
    confirmReturn_btn.place(relx=0.25, rely=0.8, anchor=CENTER)
    backToReturn_btn = Button(bookReturnSuccess, height=bannerHeight, width=optionButtonWidth,
                              command=backToReturnConfirm, text="Back to\nReturn Function", font=buttonFontSize)
    backToReturn_btn.place(relx=0.75, rely=0.8, anchor=CENTER)


def confirmReturn():
    bookReturnSuccess.destroy()
    AccessionNumber = returnAccessionNumber_entry.get()
    if returnBook(AccessionNumber):
        pass
    else:
        # ERROR Loan
        global bookReturnError
        bookReturnError = Tk()
        bookReturnError.geometry(confirmPageGeometry)
        bookReturnError.title("Book Return Error")
        bookReturnError_label = Label(
            bookReturnError, text="Error!", font=fontSize)
        bookReturnError_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        bookReturnErrorNote_label = Label(
            bookReturnError, text="Book was not on Loan \nor \nBook is returned successfully\nbut has fines", font=fontSize)
        bookReturnErrorNote_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToReturn_btn = Button(bookReturnError, height=bannerHeight, width=buttonWidth,
                                  command=backToReturn, text="Back to\nReturn Function", font=buttonFontSize)
        backToReturn_btn.place(relx=0.5, rely=0.8, anchor=CENTER)


######################################################
# Reservation Page


def reserveToReserveBook():
    reservationPage.destroy()
    reserveABook()


def reserveToCancelReservation():
    reservationPage.destroy()
    reserveCancel()


def reserveToMainMenu():
    reservationPage.destroy()
    mainPageFunction()


def reservationsPageFunction():
    global reservationPage
    reservationPage = Tk()
    reservationPage.geometry(pageGeometry)
    reservationPage.title("Reservation")
    reservationPage_topBanner = Label(
        reservationPage, text="Select one of the Options below:", font=fontSize)
    reservationPage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    reserveBook_btn = Button(reservationPage, height=bannerHeight, width=optionButtonWidth,
                             command=reserveToReserveBook, text="8. Reserve a \nBook", font=fontSize)
    reserveBook_btn.place(relx=0.5, rely=0.4, anchor=CENTER)
    reserveBook_label = Label(
        reservationPage, text="Book Reservation", font=fontSize)
    reserveBook_label.place(relx=0.8, rely=0.4, anchor=CENTER)

    reservationCancel_btn = Button(reservationPage, height=bannerHeight, width=optionButtonWidth,
                                   command=reserveToCancelReservation, text="9. Cancel\nReservation", font=fontSize)
    reservationCancel_btn.place(relx=0.5, rely=0.6, anchor=CENTER)
    reservationCancel_label = Label(
        reservationPage, text="Reservation Cancellation", font=fontSize)
    reservationCancel_label.place(relx=0.8, rely=0.6, anchor=CENTER)

    backToMain_btn = Button(reservationPage, height=bannerHeight, width=bannerWidth,
                            command=reserveToMainMenu, text="Back To Main Menu", font=fontSize)
    backToMain_btn.place(relx=0.5, rely=0.9, anchor=CENTER)


def reserveBookToMain():
    reserveABooks.destroy()
    reservationsPageFunction()


def reserveABook():
    global reserveABooks
    reserveABooks = Tk()
    reserveABooks.geometry(pageGeometry)
    reserveABooks.title("Reserve Book")
    reserveABooks_topBanner = Label(
        reserveABooks, text="To Reserve a Book, Please Enter Information Below:", font=fontSize)
    reserveABooks_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    accessNumm_label = Label(
        reserveABooks, text="Accession Number", font=fontSize)
    accessNumm_label.place(relx=0.2, rely=0.3, anchor=CENTER)
    accessNumm = StringVar()
    global accessNumm_entry
    accessNumm_entry = Entry(
        reserveABooks, textvariable=accessNumm)
    accessNumm_entry.place(relx=0.4, rely=0.3, anchor=CENTER)

    memIDNum_label = Label(
        reserveABooks, text="Membership ID", font=fontSize)
    memIDNum_label.place(relx=0.2, rely=0.4, anchor=CENTER)
    memIDNum = StringVar()
    global memIDNum_entry
    memIDNum_entry = Entry(
        reserveABooks, textvariable=memIDNum)
    memIDNum_entry.place(relx=0.4, rely=0.4, anchor=CENTER)

    reserveDateNum_label = Label(
        reserveABooks, text="Reserve Date", font=fontSize)
    reserveDateNum_label.place(relx=0.2, rely=0.5, anchor=CENTER)
    global reserveDatestr
    reserveDatestr = datetime.now()
    reserveDatestr_label = Label(
        reserveABooks, text=reserveDatestr.strftime("%Y-%m-%d"), font=fontSize)
    reserveDatestr_label.place(relx=0.4, rely=0.5, anchor=CENTER)

    reserveBooksNum_btn = Button(reserveABooks, height=bannerHeight, width=buttonWidth,
                                 command=confirmResv, text="Reserve Book", font=fontSize)
    reserveBooksNum_btn.place(relx=0.3, rely=0.8, anchor=CENTER)

    backToReserveMenu_btn = Button(reserveABooks, height=bannerHeight, width=buttonWidth,
                                   command=reserveBookToMain, text="Back To\nReservations Menu", font=fontSize)
    backToReserveMenu_btn.place(relx=0.7, rely=0.8, anchor=CENTER)


def backToReserveMenu():
    reportConfirmReservationDetail.destroy()


def callmem2BookAlrdy():
    reportConfirmReservationDetail.destroy()
    mem2BooksAlrdy()


def confirmResv():
    AccessNumber = accessNumm_entry.get()
    BookTitle = showTitle(AccessNumber)
    reserveDatestrr = datetime.now()
    ReserveDatestrr = reserveDatestrr.strftime("%Y-%m-%d")
    MEMIDNUM = memIDNum_entry.get()
    MemName = showName(MEMIDNUM)

    global reportConfirmReservationDetail
    reportConfirmReservationDetail = Tk()
    reportConfirmReservationDetail.geometry(confirmPageGeometry)
    reportConfirmReservationDetail.title(
        "Confirm Reservation Details To Be Correct")
    reportConfirmReservationDetail_label = Label(
        reportConfirmReservationDetail, text="Confirm Reservation\nDetails To Be Correct", font=fontSize)
    reportConfirmReservationDetail_label.place(
        relx=0.5, rely=0.1, anchor=CENTER)

    AccessNumber_label = Label(
        reportConfirmReservationDetail, text="Accession Number: {}".format(AccessNumber), font=buttonFontSize)
    AccessNumber_label.place(relx=0.1, rely=0.2)

    BookTitle_label = Label(
        reportConfirmReservationDetail, text="Book Title: {}".format(BookTitle), font=buttonFontSize)
    BookTitle_label.place(relx=0.1, rely=0.3)

    MEMIDNUM_label = Label(
        reportConfirmReservationDetail, text="Membership ID: {}".format(MEMIDNUM), font=buttonFontSize)
    MEMIDNUM_label.place(relx=0.1, rely=0.4)

    MemName_label = Label(
        reportConfirmReservationDetail, text="Member Name: {}".format(MemName), font=buttonFontSize)
    MemName_label.place(relx=0.1, rely=0.5)

    ReserveDatestrr_label = Label(
        reportConfirmReservationDetail, text="Reserve Date: {}".format(ReserveDatestrr), font=buttonFontSize)
    ReserveDatestrr_label.place(relx=0.1, rely=0.6)

    checkConfirmReservation_btn = Button(reportConfirmReservationDetail, height=bannerHeight, width=optionButtonWidth,
                                         command=callmem2BookAlrdy, text="Confirm\nReservation", font=buttonFontSize)
    checkConfirmReservation_btn.place(relx=0.25, rely=0.9, anchor=CENTER)

    backToReserveFunction_btn = Button(reportConfirmReservationDetail, height=bannerHeight, width=optionButtonWidth,
                                       command=backToReserveMenu, text="Back to\nReserve Function", font=buttonFontSize)
    backToReserveFunction_btn.place(relx=0.75, rely=0.9, anchor=CENTER)


def backToReserveMenu2():
    memAlrdyHas2Bk.destroy()


def backtoReserveMenu55():
    memStillHasFineToPay.destroy()


def backtoReserveMenu66():
    youCanBorrow.destroy()


def letGoToBook():
    youCanBorrow.destroy()
    reserveABooks.destroy()
    borrowPageFunction()


def mem2BooksAlrdy():
    newAccessNumber = accessNumm_entry.get()
    newBookTitle = showTitle(newAccessNumber)
    newreserveDatestrr = datetime.now()
    newReserveDatestrr = newreserveDatestrr.strftime("%y-%m-%d")
    newMEMIDNUM = memIDNum_entry.get()
    newMemName = showName(newMEMIDNUM)
    Fineagari = agari(newMEMIDNUM)

    # Error Quota
    if twoBooksReserved(newMEMIDNUM):
        global memAlrdyHas2Bk
        memAlrdyHas2Bk = Tk()
        memAlrdyHas2Bk.geometry(confirmPageGeometry)
        memAlrdyHas2Bk.title("Reserve Error - Quota")
        memAlrdyHas2Bk_label = Label(
            memAlrdyHas2Bk, text="Error!", font=fontSize)
        memAlrdyHas2Bk_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        memAlrdyHas2Bk_label = Label(
            memAlrdyHas2Bk, text="Member currently has \n 2 Books on Reservation", font=fontSize)
        memAlrdyHas2Bk_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToReservemenuu_btn = Button(memAlrdyHas2Bk, height=bannerHeight, width=buttonWidth,
                                        command=backToReserveMenu2, text="Back to\nReserve Function", font=buttonFontSize)
        backToReservemenuu_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    # Error Fine
    elif outstandingFine(newMEMIDNUM):
        global memStillHasFineToPay
        memStillHasFineToPay = Tk()
        memStillHasFineToPay.geometry(confirmPageGeometry)
        memStillHasFineToPay.title("Reserve Error - Fine")
        memStillHasFineToPay_label = Label(
            memStillHasFineToPay, text="Error!", font=fontSize)
        memStillHasFineToPay_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        # SHOW FUNCTION
        memStillHasFineToPay_label = Label(
            memStillHasFineToPay, text="Member has Oustanding Fine of:\n${}".format(Fineagari), font=fontSize)
        memStillHasFineToPay_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToReservemenuu_btn = Button(memStillHasFineToPay, height=bannerHeight, width=buttonWidth,
                                        command=backtoReserveMenu55, text="Back to\nReserve Function", font=buttonFontSize)
        backToReservemenuu_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    # Error Not on Loan
    elif notOnLoan(newAccessNumber):
        global youCanBorrow
        youCanBorrow = Tk()
        youCanBorrow.geometry(confirmPageGeometry)
        youCanBorrow.title("Reserve Error - Can Borrow")
        youCanBorrowError_label = Label(
            youCanBorrow, text="Error!", font=fontSize)
        youCanBorrowError_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        youCanBorrow_label = Label(
            youCanBorrow, text="The book is currenly not on loan. \n You may borrow it", font=fontSize)
        youCanBorrow_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        weGoBook_btn = Button(youCanBorrow, height=bannerHeight, width=optionButtonWidth,
                              command=letGoToBook, text="Borrow Book", font=buttonFontSize)
        weGoBook_btn.place(relx=0.25, rely=0.8, anchor=CENTER)

        weGoReserve_btn = Button(youCanBorrow, height=bannerHeight, width=optionButtonWidth,
                                 command=backtoReserveMenu66, text="Back to\nReserve Function", font=buttonFontSize)
        weGoReserve_btn.place(relx=0.75, rely=0.8, anchor=CENTER)

    elif successReserve(newAccessNumber, newMEMIDNUM, newReserveDatestrr):
        pass


def reserveCancelToMain():
    reserveCancels.destroy()
    reservationsPageFunction()


def reserveCancel():
    global reserveCancels
    reserveCancels = Tk()
    reserveCancels.geometry(pageGeometry)
    reserveCancels.title("Cancel Book")
    reserveCancels_topBanner = Label(
        reserveCancels, text="To Cancel a Reservation, Please Enter Information Below:", font=fontSize)
    reserveCancels_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    accessNummm_label = Label(
        reserveCancels, text="Accession Number", font=fontSize)
    accessNummm_label.place(relx=0.2, rely=0.25, anchor=CENTER)
    accessNummm = StringVar()
    global accessNummm_entry
    accessNummm_entry = Entry(
        reserveCancels, textvariable=accessNummm)
    accessNummm_entry.place(relx=0.4, rely=0.25, anchor=CENTER)

    memIDNumm_label = Label(
        reserveCancels, text="Membership ID", font=fontSize)
    memIDNumm_label.place(relx=0.2, rely=0.35, anchor=CENTER)
    memIDNumm = StringVar()
    global memIDNumm_entry
    memIDNumm_entry = Entry(
        reserveCancels, textvariable=memIDNumm)
    memIDNumm_entry.place(relx=0.4, rely=0.35, anchor=CENTER)

    cancelDateNum_label = Label(
        reserveCancels, text="Cancel Date", font=fontSize)
    cancelDateNum_label.place(relx=0.2, rely=0.45, anchor=CENTER)
    cancelDateNum = StringVar()
    global cancelDateNumstr
    cancelDateNumstr = datetime.now()
    cancelDateNumstr_label = Label(
        reserveCancels, text=cancelDateNumstr.strftime("%Y-%m-%d"), font=fontSize)
    cancelDateNumstr_label.place(relx=0.4, rely=0.45, anchor=CENTER)

    cancelBooksNumn_btn = Button(reserveCancels, height=bannerHeight, width=buttonWidth,
                                 command=confirmCancell, text="Cancel Reservation", font=fontSize)
    cancelBooksNumn_btn.place(relx=0.3, rely=0.8, anchor=CENTER)

    backToReserveMenu_btn = Button(reserveCancels, height=bannerHeight, width=buttonWidth,
                                   command=reserveCancelToMain, text="Back To\nReservations Menu", font=fontSize)
    backToReserveMenu_btn.place(relx=0.7, rely=0.8, anchor=CENTER)


def backToCancelFuncMenu():
    reportConfirmCancellationDetail.destroy()


def callmem2CancelAlrdy():
    reportConfirmCancellationDetail.destroy()
    memHasNoCancel()


def confirmCancell():
    CancelAccessNumber = accessNummm_entry.get()
    CancelBookTitle = showTitle(CancelAccessNumber)
    CancelreserveDatestrr = datetime.now()
    CancelReserveDatestrr = CancelreserveDatestrr.strftime("%y-%m-%d")
    CancelMemIDNum = memIDNumm_entry.get()
    CancelMemName = showName(CancelMemIDNum)

    global reportConfirmCancellationDetail
    reportConfirmCancellationDetail = Tk()
    reportConfirmCancellationDetail.geometry(confirmPageGeometry)
    reportConfirmCancellationDetail.title(
        "Confirm Cancellation Details To Be Correct")
    reportConfirmCancellationDetail_label = Label(
        reportConfirmCancellationDetail, text="Confirm Cancellation\nDetails To Be Correct", font=fontSize)
    reportConfirmCancellationDetail_label.place(
        relx=0.5, rely=0.1, anchor=CENTER)

    CancelAccessNumber_label = Label(
        reportConfirmCancellationDetail, text="Accession Number : {}".format(CancelAccessNumber), font=buttonFontSize)
    CancelAccessNumber_label.place(relx=0.1, rely=0.2)

    CancelBookTitle_label = Label(
        reportConfirmCancellationDetail, text="Book Title : {}".format(CancelBookTitle), font=buttonFontSize)
    CancelBookTitle_label.place(relx=0.1, rely=0.3)

    CancelMemIDNum_label = Label(
        reportConfirmCancellationDetail, text="Membership ID : {}".format(CancelMemIDNum), font=buttonFontSize)
    CancelMemIDNum_label.place(relx=0.1, rely=0.4)

    CancelMemName_label = Label(
        reportConfirmCancellationDetail, text="Member Name : {}".format(CancelMemName), font=buttonFontSize)
    CancelMemName_label.place(relx=0.1, rely=0.5)

    CancelReserveDatestrr_label = Label(
        reportConfirmCancellationDetail, text="Reserve Date: {}".format(CancelReserveDatestrr), font=buttonFontSize)
    CancelReserveDatestrr_label.place(relx=0.1, rely=0.6)

    checkConfirmCancellation_btn = Button(reportConfirmCancellationDetail, height=bannerHeight, width=optionButtonWidth,
                                          command=callmem2CancelAlrdy, text="Confirm\nCancellation", font=buttonFontSize)
    checkConfirmCancellation_btn.place(relx=0.25, rely=0.8, anchor=CENTER)

    backToReserveFunction_btn = Button(reportConfirmCancellationDetail, height=bannerHeight, width=optionButtonWidth+2,
                                       command=backToCancelFuncMenu, text="Back to\nCancellation Function", font=buttonFontSize)
    backToReserveFunction_btn.place(relx=0.75, rely=0.8, anchor=CENTER)


def backToCancelMenu2():
    memHasNoCancelErrorr.destroy()


def memHasNoCancel():
    newCancelAccessNumber = accessNummm_entry.get()
    newCancelBookTitle = showTitle(newCancelAccessNumber)
    newCancelreserveDatestrr = datetime.now()
    newCancelReserveDatestrr = newCancelreserveDatestrr.strftime("%y-%m-%d")
    newCancelMemIDNum = memIDNumm_entry.get()
    newCancelMemName = showName(newCancelMemIDNum)

    # Error No reservation
    if noReservation(newCancelMemIDNum):
        global memHasNoCancelErrorr
        memHasNoCancelErrorr = Tk()
        memHasNoCancelErrorr.geometry(confirmPageGeometry)
        memHasNoCancelErrorr.title("Cancel Reservation - No Reservation")
        memHasNoCancelErrorr_label = Label(
            memHasNoCancelErrorr, text="Error!", font=fontSize)
        memHasNoCancelErrorr_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        memHasNoCancelErrorr_label = Label(
            memHasNoCancelErrorr, text="Member has no such reservation.", font=fontSize)
        memHasNoCancelErrorr_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToCancelmenuu_btn = Button(memHasNoCancelErrorr, height=bannerHeight, width=buttonWidth,
                                       command=backToCancelMenu2, text="Back to\nCancellation Function", font=buttonFontSize)
        backToCancelmenuu_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    elif successCancel(newCancelAccessNumber, newCancelMemIDNum, newCancelReserveDatestrr):
        pass


######################################################
# Fines Page


def finesToPayment():
    finesPage.destroy()
    finesPayByMem()


def finesToMainMenu():
    finesPage.destroy()
    mainPageFunction()


def finesPageFunction():
    global finesPage
    finesPage = Tk()
    finesPage.geometry(pageGeometry)
    finesPage.title("Reservation")
    finesPage_topBanner = Label(
        finesPage, text="Select one of the Options below:", font=fontSize)
    finesPage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    finesPayment_btn = Button(finesPage, height=bannerHeight, width=optionButtonWidth,
                              command=finesToPayment, text="10. Payment", font=fontSize)
    finesPayment_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
    finesPayment_label = Label(
        finesPage, text="Fine Payment", font=fontSize)
    finesPayment_label.place(relx=0.8, rely=0.5, anchor=CENTER)

    finesToMain_btn = Button(finesPage, height=bannerHeight, width=bannerWidth,
                             command=finesToMainMenu, text="Back To Main Menu", font=fontSize)
    finesToMain_btn.place(relx=0.5, rely=0.9, anchor=CENTER)


def finesPayToMain():
    finesMemInfo.destroy()
    finesPageFunction()


def finesPayByMem():
    global finesMemInfo
    finesMemInfo = Tk()
    finesMemInfo.geometry(pageGeometry)
    finesMemInfo.title("Fines Payment")
    finesMemInfo_topBanner = Label(
        finesMemInfo, text="To Pay a Fine, Please Enter Information Below:", font=fontSize)
    finesMemInfo_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    memberIDNum_label = Label(
        finesMemInfo, text="Membership ID", font=fontSize)
    memberIDNum_label.place(relx=0.2, rely=0.3, anchor=CENTER)
    memberIDNum = StringVar()
    global memberIDNum_entry
    memberIDNum_entry = Entry(
        finesMemInfo, textvariable=memberIDNum)
    memberIDNum_entry.place(relx=0.4, rely=0.3, anchor=CENTER)

    memPayDate_label = Label(
        finesMemInfo, text="Payment Date", font=fontSize)
    memPayDate_label.place(relx=0.2, rely=0.4, anchor=CENTER)
    global memPayDateStr
    memPayDateStr = datetime.now()
    memPayDateStr_label = Label(finesMemInfo, text=memPayDateStr.strftime(
        "%Y-%m-%d"), font=fontSize)
    memPayDateStr_label.place(relx=0.4, rely=0.4, anchor=CENTER)

    memPayAmount_label = Label(
        finesMemInfo, text="Payment Amount", font=fontSize)
    memPayAmount_label.place(relx=0.2, rely=0.5, anchor=CENTER)
    memPayAmount = StringVar()
    global memPayAmount_entry
    memPayAmount_entry = Entry(
        finesMemInfo, textvariable=memPayAmount)
    memPayAmount_entry.place(relx=0.4, rely=0.5, anchor=CENTER)

    reserveBooksNum_btn = Button(finesMemInfo, height=bannerHeight, width=buttonWidth,
                                 command=confirmFinee, text="Pay Fine", font=fontSize)
    reserveBooksNum_btn.place(relx=0.3, rely=0.8, anchor=CENTER)

    backToReserveMenu_btn = Button(finesMemInfo, height=bannerHeight, width=buttonWidth,
                                   command=finesPayToMain, text="Back To \nFines Menu", font=fontSize)
    backToReserveMenu_btn.place(relx=0.7, rely=0.8, anchor=CENTER)


def backToFineMenu():
    confirmFineDetailCorrect.destroy()


def callmem2PayFineAlrdy():
    confirmFineDetailCorrect.destroy()
    memErrorFine()


def confirmFinee():
    MembershipID = memberIDNum_entry.get()
    fineMemPayDateStr = datetime.now()
    FineMemPayDateStr = fineMemPayDateStr.strftime("%Y-%m-%d")
    PaymentAmount = memPayAmount_entry.get()
    global confirmFineDetailCorrect
    confirmFineDetailCorrect = Tk()
    confirmFineDetailCorrect.geometry(confirmPageGeometry)
    confirmFineDetailCorrect.title("Confirm Reservation Details To Be Correct")
    confirmFineDetailCorrect_label = Label(
        confirmFineDetailCorrect, text="Please Confirm Details To\nBe Correct", font=fontSize)
    confirmFineDetailCorrect_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    membershipID_label = Label(
        confirmFineDetailCorrect, text="Membership ID: \n{}".format(MembershipID), font=buttonFontSize)
    membershipID_label.place(relx=0.7, rely=0.3)
    paymentDate_label = Label(
        confirmFineDetailCorrect, text="Payment Date: \n{}".format(FineMemPayDateStr), font=buttonFontSize)
    paymentDate_label.place(relx=0.7, rely=0.6)
    paymentAmount_label = Label(
        confirmFineDetailCorrect, text="Payment Due: \n${}".format(PaymentAmount), font=buttonFontSize)
    paymentAmount_label.place(relx=0.1, rely=0.3)
    extractFeeOnly_label = Label(
        confirmFineDetailCorrect, text="Extract Fee Only", font=buttonFontSize)
    extractFeeOnly_label.place(relx=0.3, rely=0.6, anchor=CENTER)

    checkConfirmPayFine_btn = Button(confirmFineDetailCorrect, height=bannerHeight, width=optionButtonWidth,
                                     command=callmem2PayFineAlrdy, text="Confirm\nPayment", font=buttonFontSize)
    checkConfirmPayFine_btn.place(relx=0.25, rely=0.8, anchor=CENTER)

    backToFinesFunction_btn = Button(confirmFineDetailCorrect, height=bannerHeight, width=optionButtonWidth,
                                     command=backToFineMenu, text="Back to\nReserve Function", font=buttonFontSize)
    backToFinesFunction_btn.place(relx=0.75, rely=0.8, anchor=CENTER)


def backToFineMenu2():
    memHasNoFine.destroy()


def backToFineMenu3():
    memIncorrectFinePaymentAmount.destroy()


def memErrorFine():
    memIDFine = memberIDNum_entry.get()
    PaymentDate = datetime.now()
    newNewPaymentDate = PaymentDate.strftime("%y-%m-%d")
    paymentAmountMemFine = int(memPayAmount_entry.get())

    # Error No fine
    if nofine(memIDFine):
        global memHasNoFine
        memHasNoFine = Tk()
        memHasNoFine.geometry(confirmPageGeometry)
        memHasNoFine.title("Fine Error - No Fine")
        memHasNoFine_label = Label(
            memHasNoFine, text="Error!", font=fontSize)
        memHasNoFine_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        memHasNoFine_label = Label(
            memHasNoFine, text="Member has no fine.", font=fontSize)
        memHasNoFine_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToFinesMenuu_btn = Button(memHasNoFine, height=bannerHeight, width=buttonWidth,
                                      command=backToFineMenu2, text="Back to\nPayment Function", font=buttonFontSize)
        backToFinesMenuu_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    # Error Incorrect amount
    elif incorrectAmount(memIDFine, paymentAmountMemFine):
        global memIncorrectFinePaymentAmount
        memIncorrectFinePaymentAmount = Tk()
        memIncorrectFinePaymentAmount.geometry(confirmPageGeometry)
        memIncorrectFinePaymentAmount.title("Fine Error - Incorrect amount")
        memIncorrectFinePaymentAmount_label = Label(
            memIncorrectFinePaymentAmount, text="Error!", font=fontSize)
        memIncorrectFinePaymentAmount_label.place(
            relx=0.5, rely=0.1, anchor=CENTER)
        memIncorrectFinePaymentAmount_label = Label(
            memIncorrectFinePaymentAmount, text="Incorrect fine payment amount.", font=fontSize)
        memIncorrectFinePaymentAmount_label.place(
            relx=0.5, rely=0.5, anchor=CENTER)
        backToFinesMenuu_btn = Button(memIncorrectFinePaymentAmount, height=bannerHeight, width=buttonWidth,
                                      command=backToFineMenu3, text="Back to\nPayment Function", font=buttonFontSize)
        backToFinesMenuu_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    elif successPayment(memIDFine, newNewPaymentDate, paymentAmountMemFine):
        insertPayment(memIDFine, newNewPaymentDate, paymentAmountMemFine)


def reportsToBookSearch():
    reportsPage.destroy()
    reportsPageFunction()


def reportsToBooksOnLoan():
    reportsPage.destroy()
    booksOnLoanReport()


def reportsToBooksOnReservation():
    reportsPage.destroy()
    booksOnReservationReport()


def reportsToBooksOnOustandingFines():
    reportsPage.destroy()
    oustandingFeesReports()


def reportsToBooksOnLoanToMember():
    reportsPage.destroy()
    reportsBooksOnLoanToMember()


def reportsToMainMenu():
    reportsPage.destroy()
    mainPageFunction()


def reportsFunction():
    global reportsPage
    reportsPage = Tk()
    reportsPage.geometry(pageGeometry)
    reportsPage.title("Reports")
    reportsPage_topBanner = Label(
        reportsPage, text="Select one of the Options below:", font=fontSize)
    reportsPage_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)
    bookSearch_btn = Button(reportsPage, height=bannerHeight, width=optionButtonWidth+2,
                            command=reportsToBookSearch, text="11. Books\nSearch", font=fontSize)
    bookSearch_btn.place(relx=0.3, rely=0.3, anchor=CENTER)
    booksSearch_label = Label(
        reportsPage, text="A member can perform a search on the\ncollection of books.", font=fontSize)
    booksSearch_label.place(relx=0.7, rely=0.3, anchor=CENTER)

    bookOnLoan_btn = Button(reportsPage, height=bannerHeight, width=optionButtonWidth+2,
                            command=reportsToBooksOnLoan, text="12. Books on\nLoan", font=fontSize)
    bookOnLoan_btn.place(relx=0.3, rely=0.4, anchor=CENTER)
    bookOnLoan_label = Label(
        reportsPage, text="This function displays all the books currently on\nloan to members.", font=fontSize)
    bookOnLoan_label.place(relx=0.7, rely=0.4, anchor=CENTER)

    bookOnReservation_btn = Button(reportsPage, height=bannerHeight, width=optionButtonWidth+2,
                                   command=reportsToBooksOnReservation, text="13. Books on\nReservation", font=fontSize)
    bookOnReservation_btn.place(relx=0.3, rely=0.5, anchor=CENTER)
    bookOnReservation_label = Label(
        reportsPage, text="This function displays all the books that\nmembers have reserved.", font=fontSize)
    bookOnReservation_label.place(relx=0.7, rely=0.5, anchor=CENTER)

    bookOnOutstanding_btn = Button(reportsPage, height=bannerHeight, width=optionButtonWidth+2,
                                   command=reportsToBooksOnOustandingFines, text="14. Outstanding\nFines", font=fontSize)
    bookOnOutstanding_btn.place(relx=0.3, rely=0.6, anchor=CENTER)
    bookOnOutstanding_label = Label(
        reportsPage, text="This function displays all the books that\nmembers have reserved.", font=fontSize)
    bookOnOutstanding_label.place(relx=0.7, rely=0.6, anchor=CENTER)

    bookOnLoanMem_btn = Button(reportsPage, height=bannerHeight, width=optionButtonWidth+2,
                               command=reportsToBooksOnLoanToMember, text="15. Books on\nLoan to Member", font=fontSize)
    bookOnLoanMem_btn.place(relx=0.3, rely=0.7, anchor=CENTER)
    bookOnLoanMem_label = Label(
        reportsPage, text="This function displays all the books a member\nidentified by the membership id has borrowed", font=fontSize)
    bookOnLoanMem_label.place(relx=0.7, rely=0.7, anchor=CENTER)

    backToMain_btn = Button(reportsPage, height=bannerHeight, width=bannerWidth,
                            command=reportsToMainMenu, text="Back To Main Menu", font=fontSize)
    backToMain_btn.place(relx=0.5, rely=0.9, anchor=CENTER)


def reportsSearchToReports():
    reportBookSearch.destroy()
    reportsFunction()


def reportsPageFunction():
    global reportBookSearch
    reportBookSearch = Tk()
    reportBookSearch.geometry(pageGeometry)
    reportBookSearch.title("Report Book Search")
    reportBookSearch_topBanner = Label(
        reportBookSearch, text="Search based on one of the categories below:", font=fontSize)
    reportBookSearch_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    titleBook_label = Label(
        reportBookSearch, text="Title", font=fontSize)
    titleBook_label.place(relx=0.2, rely=0.3, anchor=CENTER)
    titleBook = StringVar()
    global titleBook_entry
    titleBook_entry = Entry(
        reportBookSearch, textvariable=titleBook)
    titleBook_entry.place(relx=0.4, rely=0.3, anchor=CENTER)

    authorBook_label = Label(
        reportBookSearch, text="Authors", font=fontSize)
    authorBook_label.place(relx=0.2, rely=0.4, anchor=CENTER)
    authorBook = StringVar()
    global authorBook_entry
    authorBook_entry = Entry(
        reportBookSearch, textvariable=authorBook)
    authorBook_entry.place(relx=0.4, rely=0.4, anchor=CENTER)

    ISBNBook_label = Label(
        reportBookSearch, text="ISBN", font=fontSize)
    ISBNBook_label.place(relx=0.2, rely=0.5, anchor=CENTER)
    ISBNBook = StringVar()
    global ISBNBook_entry
    ISBNBook_entry = Entry(
        reportBookSearch, textvariable=ISBNBook)
    ISBNBook_entry.place(relx=0.4, rely=0.5, anchor=CENTER)

    publisherBook_label = Label(
        reportBookSearch, text="Publisher", font=fontSize)
    publisherBook_label.place(relx=0.2, rely=0.6, anchor=CENTER)
    publisherBook = StringVar()
    global publisherBook_entry
    publisherBook_entry = Entry(
        reportBookSearch, textvariable=publisherBook)
    publisherBook_entry.place(relx=0.4, rely=0.6, anchor=CENTER)

    publicationyrBook_label = Label(
        reportBookSearch, text="Publication Year", font=fontSize)
    publicationyrBook_label.place(relx=0.2, rely=0.7, anchor=CENTER)
    publicationyrBook = StringVar()
    global publicationyrBook_entry
    publicationyrBook_entry = Entry(
        reportBookSearch, textvariable=publicationyrBook)
    publicationyrBook_entry.place(relx=0.4, rely=0.7, anchor=CENTER)

    reportSearchBook_btn = Button(reportBookSearch, height=bannerHeight, width=buttonWidth,
                                  command=confirmDetail, text="Search Book", font=fontSize)
    reportSearchBook_btn.place(relx=0.3, rely=0.8, anchor=CENTER)

    backToReportsMenu_btn = Button(reportBookSearch, height=bannerHeight, width=buttonWidth,
                                   command=reportsSearchToReports, text="Back To \nReports Menu", font=fontSize)
    backToReportsMenu_btn.place(relx=0.7, rely=0.8, anchor=CENTER)


def backToReportsMenu():
    reportConfirmDetail.destroy()


def confirmDetail():
    titleName = titleBook_entry.get()
    authorName = authorBook_entry.get()
    ISBNName = ISBNBook_entry.get()
    publisherBookName = publisherBook_entry.get()
    publicationyrBookName = publicationyrBook_entry.get()

    global reportConfirmDetail
    reportConfirmDetail = Tk()
    reportConfirmDetail.geometry(reportGeometry)
    reportConfirmDetail.title("Book Search Result")
    reportConfirmDetail_label = Label(
        reportConfirmDetail, text="Book Search Result", font=fontSize)
    reportConfirmDetail_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    reportConfirmDetail_label.pack()

    connect = mysql.connector.connect(
        host='localhost', user='root', password=Password, database='ALS')
    connnne = connect.cursor()
    query = f"SELECT * FROM ALS.Book WHERE Title LIKE '% {titleName} %' OR Title LIKE '{titleName} %' OR Title LIKE '% {titleName}' "\
        f"OR Authors LIKE '% {authorName} %' OR Authors LIKE '{authorName} %' OR Authors LIKE '% {authorName}' "\
        f"OR ISBN = '{ISBNName}' "\
        f"AND Publisher LIKE '%{publisherBookName}%' OR Publisher LIKE '{publisherBookName} %' OR Publisher LIKE '% {publisherBookName}' "\
        f"OR PublicationYear = '{publicationyrBookName}'"
    connnne.execute(query.format(titleName, titleName, titleName,
                    authorName, ISBNName, publisherBookName, publicationyrBookName))
    tree8 = ttk.Treeview(reportConfirmDetail)
    tree8['show'] = 'headings'

    tree8["columns"] = ("AccessionNumber", "Title",
                        "Authors", "ISBN", "Publisher", "Year")

    tree8.column("AccessionNumber", width=150, minwidth=150, anchor=tk.CENTER)
    tree8.column("Title", width=250, minwidth=250, anchor=tk.CENTER)
    tree8.column("Authors", width=150, minwidth=150, anchor=tk.CENTER)
    tree8.column("ISBN", width=150, minwidth=150, anchor=tk.CENTER)
    tree8.column("Publisher", width=150, minwidth=150, anchor=tk.CENTER)
    tree8.column("Year", width=50, minwidth=50, anchor=tk.CENTER)

    tree8.heading("AccessionNumber", text="Accession Number", anchor=tk.CENTER)
    tree8.heading("Title", text="Title", anchor=tk.CENTER)
    tree8.heading("Authors", text="Authors", anchor=tk.CENTER)
    tree8.heading("ISBN", text="ISBN", anchor=tk.CENTER)
    tree8.heading("Publisher", text="Publisher", anchor=tk.CENTER)
    tree8.heading("Year", text="Year", anchor=tk.CENTER)

    i = 0
    for ro in connnne:
        tree8.insert('', i, text="", values=(
            ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]))
        i = i + 1

    tree8.pack()

    backToConfirmFunction_btn = tk.Button(reportConfirmDetail, height=bannerHeight, width=buttonWidth,
                                          command=backToReportsMenu, text="Back to\nSearch Function", font=buttonFontSize)
    backToConfirmFunction_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    reportConfirmDetail.mainloop()


def reportsLoanToReports():
    booksOnLoan.destroy()
    reportsFunction()


def booksOnLoanReport():
    global booksOnLoan
    booksOnLoan = tk.Tk()
    booksOnLoan.geometry(pageGeometry)
    booksOnLoan.title("Books on Loan Report")
    booksOnLoan_topBanner = Label(
        booksOnLoan, text="Books on Loan Report", font=fontSize)
    booksOnLoan_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)
    booksOnLoan_topBanner.pack()

    connect = mysql.connector.connect(
        host='localhost', user='root', password=Password, database='ALS')
    conn = connect.cursor()
    conn.execute("SELECT * FROM ALS.Book inner join ALS.BookLoan ON ALS.Book.AccessionNumber=ALS.BookLoan.AccessionNumber ORDER BY ALS.BookLoan.AccessionNumber")
    tree = ttk.Treeview(booksOnLoan)
    tree['show'] = 'headings'

    tree["columns"] = ("AccessionNumber", "Title",
                       "Authors", "ISBN", "Publisher", "Year")

    tree.column("AccessionNumber", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("Title", width=250, minwidth=250, anchor=tk.CENTER)
    tree.column("Authors", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("ISBN", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("Publisher", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("Year", width=50, minwidth=50, anchor=tk.CENTER)

    tree.heading("AccessionNumber", text="Accession Number", anchor=tk.CENTER)
    tree.heading("Title", text="Title", anchor=tk.CENTER)
    tree.heading("Authors", text="Authors", anchor=tk.CENTER)
    tree.heading("ISBN", text="ISBN", anchor=tk.CENTER)
    tree.heading("Publisher", text="Publisher", anchor=tk.CENTER)
    tree.heading("Year", text="Year", anchor=tk.CENTER)

    i = 0
    for ro in conn:
        tree.insert('', i, text="", values=(
            ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]))
        i = i + 1

    tree.pack()

    backToReportsMenu2_btn = tk.Button(booksOnLoan, height=bannerHeight, width=buttonWidth,
                                       command=reportsLoanToReports, text="Back To Reports Menu", font=fontSize)
    backToReportsMenu2_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    booksOnLoan.mainloop()


def reportsReservationToReports():
    booksOnReservation.destroy()
    reportsFunction()


def booksOnReservationReport():
    global booksOnReservation
    booksOnReservation = Tk()
    booksOnReservation.geometry(pageGeometry)
    booksOnReservation.title("Books on Reservation Report")
    booksOnReservation_topBanner = Label(
        booksOnReservation, text="Books on Reservation Report", font=fontSize)
    booksOnReservation_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)
    booksOnReservation_topBanner.pack()

    connectReserve = mysql.connector.connect(
        host='localhost', user='root', password=Password, database='ALS')
    connn = connectReserve.cursor()
    connn.execute("SELECT ALS.Book.AccessionNumber,ALS.Book.Title, ALS.Member.MembershipID,ALS.Member.Name FROM ALS.Book,ALS.Member, ALS.ReservedBook WHERE ALS.Book.AccessionNumber = ALS.ReservedBook.AccessionNumber AND ALS.Member.MembershipID = ALS.ReservedBook.MembershipID")
    tree2 = ttk.Treeview(booksOnReservation)
    tree2['show'] = 'headings'

    tree2["columns"] = ("AccessionNumber", "Title", "MembershipID", "Name")

    tree2.column("AccessionNumber", width=150, minwidth=150, anchor=tk.CENTER)
    tree2.column("Title", width=250, minwidth=250, anchor=tk.CENTER)
    tree2.column("MembershipID", width=100, minwidth=100, anchor=tk.CENTER)
    tree2.column("Name", width=150, minwidth=150, anchor=tk.CENTER)

    tree2.heading("AccessionNumber", text="Accession Number", anchor=tk.CENTER)
    tree2.heading("Title", text="Title", anchor=tk.CENTER)
    tree2.heading("MembershipID", text="MembershipID", anchor=tk.CENTER)
    tree2.heading("Name", text="Name", anchor=tk.CENTER)

    i = 0
    for ro in connn:
        tree2.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3]))
        i = i + 1

    tree2.pack()

    backToReportsMenu2_btn = tk.Button(booksOnReservation, height=bannerHeight, width=buttonWidth,
                                       command=reportsReservationToReports, text="Back To Reports Menu", font=fontSize)
    backToReportsMenu2_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    booksOnReservation.mainloop()


def reportsOustandingFees():
    memWithOutstandingFees.destroy()
    reportsFunction()


def oustandingFeesReports():
    global memWithOutstandingFees
    memWithOutstandingFees = Tk()
    memWithOutstandingFees.geometry(pageGeometry)
    memWithOutstandingFees.title("Members With Outstanding Fines")
    memWithOutstandingFees_topBanner = Label(
        memWithOutstandingFees, text="Members With Outstanding Fines", font=fontSize)
    memWithOutstandingFees_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)
    memWithOutstandingFees_topBanner.pack()

    connectReserve = mysql.connector.connect(
        host='localhost', user='root', password=Password, database='ALS')
    connnn = connectReserve.cursor()
    connnn.execute(
        "SELECT * FROM ALS.Member inner join ALS.MemFine ON ALS.Member.MembershipID = ALS.MemFine.MembershipID ORDER BY ALS.MemFine.MembershipID")
    tree3 = ttk.Treeview(memWithOutstandingFees)
    tree3['show'] = 'headings'

    tree3["columns"] = ("MembershipID", "Name", "Faculty",
                        "PhoneNumber", "EmailAddress")

    tree3.column("MembershipID", width=150, minwidth=150, anchor=tk.CENTER)
    tree3.column("Name", width=150, minwidth=150, anchor=tk.CENTER)
    tree3.column("Faculty", width=100, minwidth=100, anchor=tk.CENTER)
    tree3.column("PhoneNumber", width=150, minwidth=150, anchor=tk.CENTER)
    tree3.column("EmailAddress", width=150, minwidth=150, anchor=tk.CENTER)

    tree3.heading("MembershipID", text="Membership ID", anchor=tk.CENTER)
    tree3.heading("Name", text="Name", anchor=tk.CENTER)
    tree3.heading("Faculty", text="Faculty", anchor=tk.CENTER)
    tree3.heading("PhoneNumber", text="PhoneNumber", anchor=tk.CENTER)
    tree3.heading("EmailAddress", text="EmailAddress", anchor=tk.CENTER)

    tree3.place(x=0, y=0)

    i = 0
    for ro in connnn:
        tree3.insert('', i, text="", values=(
            ro[0], ro[1], ro[2], ro[3], ro[4]))
        i = i + 1

    tree3.pack()

    backToReportsMenu3_btn = Button(memWithOutstandingFees, height=bannerHeight, width=buttonWidth,
                                    command=reportsOustandingFees, text="Back To Reports Menu", font=fontSize)
    backToReportsMenu3_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    memWithOutstandingFees.mainloop()


def reportsLoanToMember():
    booksOnLoanToMember.destroy()
    reportsFunction()


def reportsreportsreports():
    searchMemOnLoanToMem()
    booksOnLoanToMember.destroy()


def reportsBooksOnLoanToMember():
    global booksOnLoanToMember
    booksOnLoanToMember = Tk()
    booksOnLoanToMember.geometry(pageGeometry)
    booksOnLoanToMember.title("Books On Loan to Member")
    booksOnLoanToMember_topBanner = Label(
        booksOnLoanToMember, text="Books On Loan to Member", font=fontSize)
    booksOnLoanToMember_topBanner.place(relx=0.5, rely=0.1, anchor=CENTER)

    MEMIDLOAN_label = Label(
        booksOnLoanToMember, text="Membership ID", font=fontSize)
    MEMIDLOAN_label.place(relx=0.2, rely=0.45, anchor=CENTER)
    MEMIDLOAN = StringVar()
    global MEMIDLOAN_entry
    MEMIDLOAN_entry = Entry(
        booksOnLoanToMember, textvariable=MEMIDLOAN)
    MEMIDLOAN_entry.place(relx=0.4, rely=0.45, anchor=CENTER)

    reportToSearchMemb_btn = Button(booksOnLoanToMember, height=bannerHeight, width=buttonWidth,
                                    command=reportsreportsreports, text="Search Member", font=fontSize)
    reportToSearchMemb_btn.place(relx=0.3, rely=0.8, anchor=CENTER)

    backToReportsMenu4_btn = Button(booksOnLoanToMember, height=bannerHeight, width=buttonWidth,
                                    command=reportsLoanToMember, text="Back To\nReports Menu", font=fontSize)
    backToReportsMenu4_btn.place(relx=0.7, rely=0.8, anchor=CENTER)


def booksOnLoanToMemToReport():
    booksOnLoanToMember.destroy()
    chartMemOnLoanToMem.destroy()
    reportsFunction()


def searchMemOnLoanToMem():
    wow = MEMIDLOAN_entry.get()
    global chartMemOnLoanToMem
    chartMemOnLoanToMem = Tk()
    chartMemOnLoanToMem.geometry(pageGeometry)
    chartMemOnLoanToMem.title("Book on Loan to Member")
    chartMemOnLoanToMem_label = Label(
        chartMemOnLoanToMem, text="Book on Loan to Member", font=fontSize)
    chartMemOnLoanToMem_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    chartMemOnLoanToMem_label.pack()

    connectReserve = mysql.connector.connect(
        host='localhost', user='root', password=Password, database='ALS')
    conep = connectReserve.cursor()
    conep.execute(
        "SELECT ALS.Book.AccessionNumber,ALS.Book.Title, ALS.Book.Authors, ALS.Book.ISBN,ALS.Book.Publisher, ALS.Book.PublicationYear FROM ALS.Book,ALS.BookLoan WHERE ALS.Book.AccessionNumber = ALS.BookLoan.AccessionNumber AND ALS.BookLoan.MembershipID = '{}'".format(wow))
    tree7 = ttk.Treeview(chartMemOnLoanToMem)
    tree7['show'] = 'headings'

    tree7["columns"] = ("AccessionNumber", "Title",
                        "Authors", "ISBN", "Publisher", "Year")

    tree7.column("AccessionNumber", width=150, minwidth=150, anchor=tk.CENTER)
    tree7.column("Title", width=200, minwidth=200, anchor=tk.CENTER)
    tree7.column("Authors", width=150, minwidth=150, anchor=tk.CENTER)
    tree7.column("ISBN", width=150, minwidth=150, anchor=tk.CENTER)
    tree7.column("Publisher", width=150, minwidth=150, anchor=tk.CENTER)
    tree7.column("Year", width=50, minwidth=50, anchor=tk.CENTER)

    tree7.heading("AccessionNumber",
                  text="Accession Number", anchor=tk.CENTER)
    tree7.heading("Title", text="Title", anchor=tk.CENTER)
    tree7.heading("Authors", text="Authors", anchor=tk.CENTER)
    tree7.heading("ISBN", text="ISBN", anchor=tk.CENTER)
    tree7.heading("Publisher", text="Publisher", anchor=tk.CENTER)
    tree7.heading("Year", text="Year", anchor=tk.CENTER)

    i = 0
    for ro in conep:
        tree7.insert('', i, text="", values=(
            ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]))
        i = i + 1

    tree7.pack()

    backToReportFunction6_btn = Button(chartMemOnLoanToMem, height=bannerHeight, width=buttonWidth,
                                       command=booksOnLoanToMemToReport, text="Back to Reports Function", font=fontSize)
    backToReportFunction6_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    chartMemOnLoanToMem.mainloop()
