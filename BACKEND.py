def connectDB():
    import mysql.connector

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1222ths#',  # should be set to your password
        database='ALS'
    )

    mycursor = mydb.cursor()

    return mydb, mycursor


def emptyCursor(mycursor):
    return len(mycursor.fetchall()) == 0

################################
# SHOW FUNCTION


def showMembershipID(membershipID):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Member WHERE MembershipID = '{membershipID}'")
        myresult = mycursor.fetchone()[0]
        return myresult
    except:
        print("Error")
        mydb.rollback()
    mydb.close()


def showName(membershipID):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Member WHERE MembershipID = '{membershipID}'")
        myresult = mycursor.fetchone()[1]
        return myresult
    except:
        print("Error")
        mydb.rollback()
    mydb.close()


def showFaculty(membershipID):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Member WHERE MembershipID = '{membershipID}'")
        myresult = mycursor.fetchone()[2]
        return myresult
    except:
        print("Error")
        mydb.rollback()
    mydb.close()


def showPhoneNumber(membershipID):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Member WHERE MembershipID = '{membershipID}'")
        myresult = mycursor.fetchone()[3]
        return myresult
    except:
        print("Error")
        mydb.rollback()
    mydb.close()


def showEmailAddress(membershipID):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Member WHERE MembershipID = '{membershipID}'")
        myresult = mycursor.fetchone()[4]
        return myresult
    except:
        print("Error")
        mydb.rollback()
    mydb.close()


def showTitle(accessionNumber):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Book WHERE AccessionNumber = '{accessionNumber}'")
        myresult = mycursor.fetchone()[1]
        return myresult
    except:
        mydb.rollback()
    mydb.close()


def showAuthors(accessionNumber):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Book WHERE AccessionNumber = '{accessionNumber}'")
        myresult = mycursor.fetchone()[2]
        return myresult
    except:
        mydb.rollback()
    mydb.close()


def showISBN(accessionNumber):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Book WHERE AccessionNumber = '{accessionNumber}'")
        myresult = mycursor.fetchone()[3]
        return myresult
    except:
        mydb.rollback()
    mydb.close()


def showPublisher(accessionNumber):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Book WHERE AccessionNumber = '{accessionNumber}'")
        myresult = mycursor.fetchone()[4]
        return myresult
    except:
        mydb.rollback()
    mydb.close()


def showYear(accessionNumber):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Book WHERE AccessionNumber = '{accessionNumber}'")
        myresult = mycursor.fetchone()[5]
        return myresult
    except:
        mydb.rollback()
    mydb.close()


def showLoanedAccessionNumber(accessionNumber):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'")
        myresult = mycursor.fetchone()[0]
        return myresult
    except:
        mydb.rollback()
    mydb.close()


def showLoanedBookTitle(accessionNumber):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Book WHERE AccessionNumber = '{accessionNumber}'")
        myresult = mycursor.fetchone()[1]
        return myresult
    except:
        mydb.rollback()
    mydb.close()


def showLoanedMembershipID(accessionNumber):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'")
        myresult = mycursor.fetchone()[1]
        return myresult
    except:
        mydb.rollback()
    mydb.close()


def showLoanedMemberName(accessionNumber):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'")
        member = mycursor.fetchone()[1]
        mycursor.execute(
            f"SELECT * FROM ALS.Member WHERE MembershipID = '{member}'")
        myresult = mycursor.fetchone()[1]
        return myresult
    except:
        mydb.rollback()
    mydb.close()


def showReturnDate(accesssionNumber):

    import datetime
    from datetime import datetime

    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d")

    return date_time


def showFine(accessionNumber):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'")
        member = mycursor.fetchone()[1]
        mycursor.execute(
            f"SELECT * FROM ALS.MemFine WHERE MembershipID = '{member}'")
        myresult = mycursor.fetchone()[1]
        if not emptyCursor(mycursor):
            return myresult
        else:
            return 0
    except:
        mydb.rollback()
    mydb.close()


def showLoanDate(accessionNumber):

    import datetime
    from datetime import datetime

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'")
        dueDate = mycursor.fetchone()[3]
        myResult = dueDate.strftime('%Y-%m-%d')
        return myResult
    except:
        mydb.rollback()
    mydb.close()


def agari(membershipID):
    mydb, mycursor = connectDB()

    fineSql = f"SELECT * FROM ALS.MemFine WHERE MembershipID = '{membershipID}'"
    try:
        mycursor.execute(fineSql)
        if not emptyCursor(mycursor):
            mycursor.execute(fineSql)
            myresult = mycursor.fetchone()[1]
            return myresult
    except:
        mydb.rollback()
    mydb.close()

###################################
# MEMBERSHIP


def createMembership(membershipID, name, faculty, phoneNumber, emailAddress):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Member WHERE MembershipID = '{membershipID}'")
        if emptyCursor(mycursor):
            mycursor.execute(
                f"INSERT INTO ALS.member VALUES ('{membershipID}', '{name}', '{faculty}', '{phoneNumber}', '{emailAddress}')")
            mydb.commit()
            print("Success! ALS Membership created.")
            return True
        else:
            print("Error! Member already exist; Missing or Incomplete fields ")
            return False
    except:
        mydb.rollback()
    mydb.close()


def deleteMembership(membershipID):

    mydb, mycursor = connectDB()

    unsuccessDeletion = "Member has loans, reservations or outstanding fines."
    successDeletion = "Successfully Deleted"

    try:

        memberSql = f"SELECT * FROM ALS.Member WHERE MembershipID = '{membershipID}'"
        loanSql = f"SELECT * FROM ALS.BookLoan WHERE MembershipID = '{membershipID}'"
        reserveSql = f"SELECT * FROM ALS.ReservedBook WHERE MembershipID = '{membershipID}'"
        fineSql = f"SELECT * FROM ALS.MemFine WHERE MembershipID = '{membershipID}'"

        mycursor.execute(loanSql)
        if not emptyCursor(mycursor):
            print(unsuccessDeletion)
            return False
        mycursor.execute(fineSql)
        if not emptyCursor(mycursor):
            print(unsuccessDeletion)
            return False
        mycursor.execute(reserveSql)
        if not emptyCursor(mycursor):
            print(unsuccessDeletion)
            return False

        mycursor.execute(memberSql)
        if emptyCursor(mycursor):
            print(unsuccessDeletion)
            return False
        else:
            mycursor.execute(
                f"DELETE FROM ALS.Member WHERE MembershipID = '{membershipID}'")
            mydb.commit()
            print(successDeletion)
            return True

    except:
        print("Error")
        mydb.rollback()
    mydb.close()


def updateMembership(membershipID, name, faculty, PhoneNo, email):

    mydb, mycursor = connectDB()

    memberSql = f"SELECT * FROM ALS.Member WHERE MembershipID = '{membershipID}'"

    try:
        mycursor.execute(memberSql)
        if emptyCursor(mycursor):
            return False
        elif membershipID != '' and name != '' and faculty != '' and PhoneNo != '' and email != '':
            mycursor.execute(
                f"UPDATE Member SET Name = '{name}' WHERE MembershipID = '{membershipID}'")
            mydb.commit()
            mycursor.execute(
                f"UPDATE Member SET Faculty = '{faculty}' WHERE MembershipID = '{membershipID}'")
            mydb.commit()
            mycursor.execute(
                f"UPDATE Member SET Phonenumber = '{PhoneNo}' WHERE MembershipID = '{membershipID}'")
            mydb.commit()
            mycursor.execute(
                f"UPDATE Member SET Email = '{email}' WHERE MembershipID = '{membershipID}'")
            mydb.commit()
            return True
        else:
            return False
    except:
        print("error")
        mydb.rollback()
    mydb.close()


##################################
# Book
def bookAcquisition(accessionNumber, title, authors, ISBN, publisher, publicationYear):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.Book WHERE AccessionNumber = '{accessionNumber}'")
        if emptyCursor(mycursor):
            mycursor.execute(
                f"INSERT INTO ALS.Book VALUES ('{accessionNumber}', '{title}', '{authors}', '{ISBN}', '{publisher}', '{publicationYear}', NULL)")
            mydb.commit()
            return True
        else:
            return False
    except:
        mydb.rollback()
    mydb.close()


def bookWithLoan(accessionNumber):

    mydb, mycursor = connectDB()

    loanSql = f"SELECT AccessionNumber FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'"

    try:
        mycursor.execute(loanSql)
        if not emptyCursor(mycursor):
            print("Error! Book is currently on Loan.")
            return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()


def bookWithReserve(accessionNumber):

    mydb, mycursor = connectDB()

    reserveSql = f"SELECT AccessionNumber FROM ALS.ReservedBook WHERE AccessionNumber = '{accessionNumber}'"

    try:
        mycursor.execute(reserveSql)
        if not emptyCursor(mycursor):
            print("Error! Book is currently Reserved.")
            return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()


def successWithdrawal(accessionNumber):

    mydb, mycursor = connectDB()

    bookSql = f"SELECT * FROM ALS.Book WHERE AccessionNumber = '{accessionNumber}'"

    try:
        mycursor.execute(
            f"DELETE FROM ALS.Book WHERE AccessionNumber = '{accessionNumber}'")
        mydb.commit()
        return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()


###########################
# LOAN


def MemQuotaExceeded(membershipID, accessionNumber):

    mydb, mycursor = connectDB()

    try:

        loanNumSql = f"SELECT * FROM ALS.BookLoan WHERE MembershipID = '{membershipID}'"

        mycursor.execute(loanNumSql)
        loanedBooks = mycursor.fetchall()
        if len(loanedBooks) == 2:
            print("Member loan quota exceeded.")
            return True
        else:
            return False
    except:
        print("Error")
        mydb.rollback()
    mydb.close()


def LoanedBook(membershipID, accessionNumber):

    mydb, mycursor = connectDB()

    try:

        loanSql = f"SELECT AccessionNumber FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'"

        mycursor.execute(loanSql)
        if not emptyCursor(mycursor):
            print("Book currenlty on Loan until:")
            return True
        else:
            return False
    except:
        print("Error")
        mydb.rollback()
    mydb.close()


def memFined(membershipID, accessionNumber):

    mydb, mycursor = connectDB()

    try:

        fineSql = f"SELECT * FROM ALS.MemFine WHERE MembershipID = '{membershipID}'"

        mycursor.execute(fineSql)
        if not emptyCursor(mycursor):
            print("Member has outstanding fines.")
            return True
        else:
            return False
    except:
        print("Error")
        mydb.rollback()
    mydb.close()


def bookOnReservation(membershipID, accessionNumber):

    import datetime
    from datetime import datetime
    from datetime import date

    mydb, mycursor = connectDB()

    try:

        reserveMemID = f"SELECT * FROM ALS.ReservedBook WHERE MembershipID = '{membershipID}'"
        reserveBook = f"SELECT * FROM ALS.ReservedBook WHERE AccessionNumber = '{accessionNumber}'"

        mycursor.execute(reserveMemID)
        if not emptyCursor(mycursor):
            mycursor.execute(reserveBook)
            dates = mycursor.fetchall()
            dates_list = []
            for date in dates:
                dates_list.append(date[2])
            min_date = min(dates_list)
            print(min_date)
            mycursor.execute(
                f"SELECT * FROM ReservedBook WHERE ReserveDate = '{min_date}'")
            member = mycursor.fetchone()[1]
            if member == membershipID:
                successBorrow(membershipID, accessionNumber)
                return True
            else:
                print("Not your turn")
                return False

    except:
        print("Error")
        mydb.rollback()
    mydb.close()


def successBorrow(membershipID, accessionNumber):

    import datetime
    from datetime import timedelta
    from datetime import time

    mydb, mycursor = connectDB()

    now = datetime.datetime.now()
    due = datetime.datetime.now() + timedelta(days=14)

    try:
        bookSql = f"SELECT * FROM ALS.Book WHERE AccessionNumber = '{accessionNumber}'"

        mycursor.execute(bookSql)
        if not emptyCursor(mycursor):
            mycursor.execute(
                f"INSERT INTO ALS.BookLoan VALUES ('{accessionNumber}', '{membershipID}', '{now}', '{due}', NULL)")
            mydb.commit()
            print("Borrowed")
            return True
        else:
            print("Not Borrowed")
            return False
    except:
        print("Error")
        mydb.rollback()
    mydb.close()


def returnBook(accessionNumber):

    import datetime
    from datetime import datetime
    from datetime import time
    from datetime import date

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"SELECT * FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'")
        dueDate = mycursor.fetchone()[3]
        curMonth = datetime.now().month
        curYear = datetime.now().year
        curDay = datetime.now().day
        today = date(curYear, curMonth, curDay)
        dueMonth = dueDate.month
        dueYear = dueDate.year
        dueDay = dueDate.day
        due = date(dueYear, dueMonth, dueDay)
        diff = (today - due).days
        print(diff)
        mycursor.execute(
            f"SELECT * FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'")
        member = mycursor.fetchone()[1]
        mycursor.execute(
            f"SELECT * FROM ALS.memFine WHERE MembershipID = '{member}'")
        if diff > 0 and not emptyCursor(mycursor):
            curAmount = mycursor.fetchone()[0]
            newAmount = curAmount + diff
            mycursor.execute(
                f"UPDATE ALS.memFine SET Amount = '{newAmount}' WHERE MembershipID = '{member}'")
            mydb.commit()
            mycursor.execute(
                f"DELETE FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'")
            mydb.commit()
            print("fine updated")
            return False
        if diff > 0 and emptyCursor(mycursor):
            mycursor.execute(
                f"INSERT INTO ALS.MemFine VALUES ('{member}', '{diff}')")
            mydb.commit()
            mycursor.execute(
                f"DELETE FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'")
            mydb.commit()
            print("New fine updated")
            return False
        if diff <= 0 and emptyCursor(mycursor):
            print(member)
            mycursor.execute(
                f"DELETE FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'")
            mydb.commit()
            print("Returned")
            return True
    except:
        print("Error")
        mydb.rollback()
    mydb.close()

####################################
# Fine


def nofine(membershipID):

    mydb, mycursor = connectDB()

    fineSql = f"SELECT MembershipID FROM ALS.MemFine WHERE MembershipID = '{membershipID}'"

    try:
        mycursor.execute(fineSql)
        if emptyCursor(mycursor):
            print("Error! Member has no fine.")
            return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()


def incorrectAmount(membershipID, paymentAmount):

    mydb, mycursor = connectDB()

    fineSql = f"SELECT * FROM ALS.MemFine WHERE MembershipID = '{membershipID}'"

    try:
        paymentAmount = int(paymentAmount)
        mycursor.execute(fineSql)
        myresult = mycursor.fetchone()[1]
        if myresult != paymentAmount:
            print("Error! Incorrect fine payment amount.")
            return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()


def notOnLoan(accessionNumber):
    mydb, mycursor = connectDB()

    LoanSql = f"SELECT * FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'"

    try:
        mycursor.execute(LoanSql)
        if emptyCursor(mycursor):
            print("The book is currenly not on loan. You may borrow it.")
            return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()


def successPayment(membershipID, paymentDate, paymentAmount):

    mydb, mycursor = connectDB()

    try:
        mycursor.execute(
            f"DELETE FROM ALS.MemFine WHERE MembershipID = '{membershipID}'")
        mydb.commit()
        return True
    except:
        print("error1")
        mydb.rollback()
    mydb.close()


def insertPayment(membershipID, paymentDate, paymentAmount):

    import datetime
    from datetime import timedelta
    from datetime import time
    from datetime import date

    mydb, mycursor = connectDB()

    now = datetime.datetime.now()

    paySql = f"SELECT * FROM ALS.Payment WHERE MembershipID = '{membershipID}'"

    try:
        mycursor.execute(paySql)
        if emptyCursor(mycursor):
            mycursor.execute(
                f"INSERT INTO ALS.Payment VALUES ('{membershipID}','{now}', '{paymentAmount}')")
            mydb.commit()
            return True
        else:
            mycursor.execute(
                f"UPDATE ALS.Payment SET Amount = Amount + '{paymentAmount}' WHERE MembershipID = '{membershipID}'")
            mydb.commit()
            return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()


def twoBooksReserved(membershipID):
    mydb, mycursor = connectDB()

    reserveSql = f"SELECT * FROM ALS.ReservedBook WHERE MembershipID = '{membershipID}'"

    try:
        mycursor.execute(reserveSql)
        records = mycursor.fetchall()
        if len(records) == 2:
            print("Error! Member currently has 2 Books on Reservation.")
            return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()


def outstandingFine(membershipID):

    mydb, mycursor = connectDB()

    fineSql = f"SELECT * FROM ALS.MemFine WHERE MembershipID = '{membershipID}'"

    try:
        mycursor.execute(fineSql)
        if not emptyCursor(mycursor):
            mycursor.execute(fineSql)
            myresult = mycursor.fetchone()[1]
            print(myresult)
            print("Error! Member has Outstanding Fine of $" + str(myresult))
            return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()


def notOnLoan(accessionNumber):
    mydb, mycursor = connectDB()

    LoanSql = f"SELECT * FROM ALS.BookLoan WHERE AccessionNumber = '{accessionNumber}'"

    try:
        mycursor.execute(LoanSql)
        if emptyCursor(mycursor):
            print("The book is currenly not on loan. You may borrow it.")
            return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()


def successReserve(accessionNumber, membershipID, reserveDate):
    import datetime
    from datetime import timedelta
    from datetime import time
    from datetime import date

    mydb, mycursor = connectDB()

    now = datetime.datetime.now()

    try:
        mycursor.execute(
            f"INSERT INTO ALS.ReservedBook VALUES ('{accessionNumber}','{membershipID}', '{now}')")
        mydb.commit()
        return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()


def noReservation(membershipID):
    mydb, mycursor = connectDB()
    try:
        mycursor.execute(
            f"SELECT * FROM ALS.ReservedBook WHERE MembershipID = '{membershipID}'")
        if emptyCursor(mycursor):
            print("Error! Member has no such reservation.")
            return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()


def successCancel(accessionNumber, membershipID, cancelDate):
    mydb, mycursor = connectDB()
    try:
        mycursor.execute(
            f"DELETE FROM ALS.ReservedBook WHERE MembershipID = '{membershipID}'")
        mydb.commit()
        return True
    except:
        print("error")
        mydb.rollback()
    mydb.close()
