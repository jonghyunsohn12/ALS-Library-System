DROP SCHEMA `ALS`;
CREATE SCHEMA `ALS`;

CREATE TABLE `ALS`.`Member` (
  `MembershipID` varchar(45) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Faculty` varchar(45) NOT NULL,
  `PhoneNumber` INT NOT NULL,
  `Email` varchar(45) NOT NULL,
  PRIMARY KEY (`MembershipID`)
) ENGINE=InnoDB;

CREATE TABLE `ALS`.`Book` (
  `AccessionNumber` varchar(45) NOT NULL,
  `Title` varchar(100) NOT NULL,
  `Authors` varchar(45) NOT NULL,
  `ISBN` BIGINT NOT NULL,
  `Publisher` varchar(45) NOT NULL,
  `PublicationYear` INT NOT NULL,
  `MembershipID` varchar(45) NULL,
  PRIMARY KEY (`AccessionNumber`),
  FOREIGN KEY (`MembershipID`) REFERENCES Member (`MembershipID`)
) ENGINE=InnoDB;

CREATE TABLE `ALS`.`MemFine` (
  `MembershipID` varchar(45) NOT NULL,
  `Amount` INT DEFAULT 0,
  PRIMARY KEY (`MembershipID`),
  FOREIGN KEY (`MembershipID`) REFERENCES Member (`MembershipID`)
) ENGINE=InnoDB;

CREATE TABLE `ALS`.`Payment` (
	`MembershipID` varchar(45) NOT NULL,
    `Date` datetime DEFAULT NULL,
	`Amount` INT DEFAULT 0,
    PRIMARY KEY (`MembershipID`),
    FOREIGN KEY (`MembershipID`) REFERENCES Member (`MembershipID`)
) ENGINE=InnoDB ;

CREATE TABLE `ALS`.`BookLoan` (
  `AccessionNumber` varchar(45) NOT NULL,
  `MembershipID` varchar(45) NOT NULL,
  `BorrowDate` datetime DEFAULT NULL,
  `DueDate` datetime DEFAULT NULL,
  `ReturnDate` datetime DEFAULT NULL,
  PRIMARY KEY (`MembershipID`, `AccessionNumber`),
  FOREIGN KEY (`MembershipID`) REFERENCES Member (`MembershipID`),
  FOREIGN KEY (`AccessionNumber`) REFERENCES Book (`AccessionNumber`)
) ENGINE=InnoDB;

CREATE TABLE `ALS`.`ReservedBook` (
  `AccessionNumber` varchar(45) NOT NULL,
  `MembershipID` varchar(45) NOT NULL,
  `ReserveDate` date DEFAULT NULL,
  PRIMARY KEY (`MembershipID`, `AccessionNumber`),
  FOREIGN KEY (`MembershipID`) REFERENCES Member (`MembershipID`),
  FOREIGN KEY (`AccessionNumber`) REFERENCES Book (`AccessionNumber`)
) ENGINE=InnoDB;
