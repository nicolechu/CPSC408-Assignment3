### Assignment 3

## 5 tables
# movie info (movieID, movieTitle, genre, ...)

# CREATE TABLE IF NOT EXISTS MovieInfo(MovieID INT PRIMARY KEY AUTO_INCREMENT,
#                         MovieTitle VARCHAR(32),
#                         Genre VARCHAR(32),
#                         Director VARCHAR(32),
#                         Length DATETIME,
#                         Actor1 VARCHAR(32),
#                         Actor2 VARCHAR(32),
#                         Actor3 VARCHAR(32),
#                         Mood VARCHAR(32),
#                         UserRatings TINYINT);

### Preferred MovieInfo table/schema for final project above, but Length changed to VARCHAR below for easier data import
CREATE TABLE IF NOT EXISTS MovieInfo1(MovieID INT PRIMARY KEY AUTO_INCREMENT,
                                        MovieTitle VARCHAR(32),
                                        Genre VARCHAR(32),
                                        Director VARCHAR(32),
                                        Length VARCHAR(32),
                                        Actor1 VARCHAR(32),
                                        Actor2 VARCHAR(32),
                                        Actor3 VARCHAR(32),
                                        Mood VARCHAR(32),
                                        UserRatings TINYINT);

# user info (userID, firstName, lastName)
CREATE TABLE IF NOT EXISTS UserInfo(UserID INT PRIMARY KEY AUTO_INCREMENT,
                                    FirstName VARCHAR(32),
                                    LastName VARCHAR(32));


### For the following tables, FOREIGN KEY prevents proper data import so FOREIGN KEY declarations have been commented out

# user ratings (movieID, keyword1, keyword2, keyword3)
CREATE TABLE IF NOT EXISTS UserRating(MovieID INT,
                                        #FOREIGN KEY (MovieID) REFERENCES MovieInfo(MovieID),
                                        UserID INT,
                                        #FOREIGN KEY (UserID) REFERENCES UserInfo(UserID),
                                        Rating TINYINT,
                                        UserMood VARCHAR(32));

# user want to watch (userID, movieID, wantToWatch)
CREATE TABLE IF NOT EXISTS WantToWatch(UserID INT,
                                        #FOREIGN KEY (UserID) REFERENCES UserInfo(UserID),
                                        MovieID INT);
                                        #MovieID INT,
                                        #FOREIGN KEY (MovieID) REFERENCES MovieInfo(MovieID));

# user watched (userID, movieID, Watched)
CREATE TABLE IF NOT EXISTS UserWatched(UserID INT,
                                        #FOREIGN KEY (UserID) REFERENCES UserInfo(UserID),
                                        MovieID INT);
                                        #MovieID INT,
                                        #FOREIGN KEY (MovieID) REFERENCES MovieInfo(MovieID));
