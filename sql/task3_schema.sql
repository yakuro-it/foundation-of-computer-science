DROP TABLE IF EXISTS Membership CASCADE;
DROP TABLE IF EXISTS Student CASCADE;
DROP TABLE IF EXISTS Club CASCADE;

CREATE TABLE Student (
    StudentID     INT PRIMARY KEY,
    StudentName   VARCHAR(100) NOT NULL,
    Email         VARCHAR(150) UNIQUE NOT NULL,
    City          VARCHAR(50)
);

CREATE TABLE Club (
    ClubID      INT PRIMARY KEY,
    ClubName    VARCHAR(100) NOT NULL UNIQUE,
    ClubRoom    VARCHAR(50)  NOT NULL,
    ClubMentor  VARCHAR(100) NOT NULL
);

CREATE TABLE Membership (
    MembershipID  INT PRIMARY KEY,
    StudentID     INT NOT NULL,
    ClubID        INT NOT NULL,
    JoinDate      DATE NOT NULL,
    Fee           DECIMAL(8,2),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (ClubID)    REFERENCES Club(ClubID)       ON UPDATE CASCADE ON DELETE RESTRICT,
    UNIQUE (StudentID, ClubID)
);

CREATE INDEX idx_membership_studentid ON Membership(StudentID);
CREATE INDEX idx_membership_clubid ON Membership(ClubID);

INSERT INTO Student (StudentID, StudentName, Email, City) VALUES
(1, 'Asha',   'asha@email.com',   NULL),
(2, 'Bikash', 'bikash@email.com', NULL),
(3, 'Nisha',  'nisha@email.com',  NULL),
(4, 'Rohan',  'rohan@email.com',  NULL),
(5, 'Suman',  'suman@email.com',  NULL),
(6, 'Pooja',  'pooja@email.com',  NULL),
(7, 'Aman',   'aman@email.com',   NULL);

INSERT INTO Club (ClubID, ClubName, ClubRoom, ClubMentor) VALUES
(101, 'Music Club',  'R101', 'Mr. Raman'),
(202, 'Sports Club', 'R202', 'Ms. Sita'),
(303, 'Drama Club',  'R303', 'Mr. Kiran'),
(404, 'Coding Club', 'Lab1', 'Mr. Anil');

INSERT INTO Membership (MembershipID, StudentID, ClubID, JoinDate, Fee) VALUES
(10001, 1, 101, DATE '2024-01-10', NULL),
(10002, 2, 202, DATE '2024-01-12', NULL),
(10003, 1, 202, DATE '2024-01-15', NULL),
(10004, 3, 101, DATE '2024-01-20', NULL),
(10005, 4, 303, DATE '2024-01-18', NULL),
(10006, 5, 101, DATE '2024-01-22', NULL),
(10007, 2, 303, DATE '2024-01-25', NULL),
(10008, 6, 202, DATE '2024-01-27', NULL),
(10009, 3, 404, DATE '2024-01-28', NULL),
(10010, 7, 404, DATE '2024-01-30', NULL);

INSERT INTO Student (StudentID, StudentName, Email, City)
VALUES (8, 'Alice Johnson', 'alice.johnson@college.ac.uk', 'London');

INSERT INTO Club (ClubID, ClubName, ClubRoom, ClubMentor)
VALUES (505, 'Robotics Society', 'Room 4B', 'Dr. Sharma');

SELECT StudentID, StudentName, Email, City
FROM Student
ORDER BY StudentName ASC;

SELECT ClubID, ClubName, ClubRoom, ClubMentor
FROM Club
ORDER BY ClubName ASC;

SELECT
    s.StudentName,
    c.ClubName,
    m.JoinDate
FROM Membership m
JOIN Student s ON m.StudentID = s.StudentID
JOIN Club c    ON m.ClubID    = c.ClubID
ORDER BY s.StudentName ASC, m.JoinDate ASC;
