import csv
import mysql.connector

# Connect to database in Google Cloud instance
config = {
    'host' : '34.106.228.88',
    'user' : 'root',
    'passwd' : 'Hq43j070Fqm4blL7',
    'database' : 'assignment3'
}

db = mysql.connector.connect(**config)
mycursor = db.cursor()

# Prompt user for full file name
file_name = input("CSV File Name (ex: 'file_name.csv'): ")

# Open & read file
with open(file_name, newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter = ',', quotechar='|')

    # Iterate through each line of the file
    for row in filereader:
        # IF statements to organize data into correct tables using table numbers (from csv file generating code)
        if row[0] == '1':
            # Assign each value in row to variable to build input-param
            # MovieID attribute in MovieInfo table auto-increments
            title = row[2]
            genre = row[3]
            director = row[4]
            length = row[5] # as string
            actor1 = row[6]
            actor2 = row[7]
            actor3 = row[8]
            mood = row[9]
            rating = row[10]

            input_param = (title, genre, director, length, actor1, actor2, actor3, mood, rating)

            # Insert corresponding values from input_param into MovieInfo1 table
            mycursor.execute("INSERT INTO MovieInfo1(MovieTitle, Genre, Director, Length, Actor1, Actor2, Actor3, Mood, UserRatings)"
                             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", input_param)
            db.commit()

        elif row[0] == '2':
            # Assign row values to variables for input_param
            # UserID attribute in UserInfo table auto-increments
            first = row[2]
            last = row[3]

            input_param = (first, last)

            # Insert corresponding values from input_param into UserInfo table
            mycursor.execute("INSERT INTO UserInfo(FirstName, LastName)"
                             "VALUES (%s, %s)", input_param)
            db.commit()

        elif row[0] == '3':
            # Assign row values to variables to build input_param
            movieID = row[1]
            userID = row[2]
            rating = row[3]
            mood = row[4]

            input_param = (movieID, userID, rating, mood)

            # Insert corresponding values from input_param into UserRating table
            mycursor.execute("INSERT INTO UserRating(MovieID, UserID, Rating, UserMood)"
                             "VALUES (%s, %s, %s, %s)", input_param)
            db.commit()

        elif row[0] == '4':
            # Assign row values to variables to build input_param
            userID = row[1]
            movieID = row[2]

            input_param = (userID, movieID)

            # Insert corresponding values from input_param into WantToWatch table
            mycursor.execute("INSERT INTO WantToWatch(UserID, MovieID)"
                             "VALUES (%s, %s)", input_param)
            db.commit()

        elif row[0] == '5':
            # Assign row values to variables to build input_param
            userID = row[1]
            movieID = row[2]

            input_param = (userID, movieID)

            # Insert corresponding values from input_param into MovieInfo1 table
            mycursor.execute("INSERT INTO UserWatched(UserID, MovieID)"
                             "VALUES (%s, %s)", input_param)
            db.commit()

    db.close()


