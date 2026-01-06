def generate_ascii_art():
    height = 29 # Total number of rows in the ASCII art
    width = 73   # Total number of columns in each row

    for row in range(height):
        for column in range(width):
            char = " "

            if row == 0:
                if 24 <= column <= 29:
                    char = "."
                elif column == 30:
                    char = "*"
                elif 31 <= column <= 40:
                    char = "#"
                elif 41 <= column <= 42:
                    char = ","
                elif 48 <= column <= 50:
                    char = "("
                elif 51 <= column <= 61:
                    char = "#"

            elif row == 1:
                if column == 23:
                    char = "#"
                elif column == 24:
                    char = "$"
                elif column == 25:
                    char = "#"
                elif column == 26:
                    char = "$"
                elif column == 27:
                    char = "%"
                elif column == 28:
                    char = "/"
                elif column == 29:
                    char = ","
                elif column == 30:
                    char = "/"
                elif column == 31:
                    char = "("
                elif column == 32:
                    char = "/"
                elif column == 33:
                    char = "@"
                elif column == 34:
                    char = "%"
                elif 35 <= column <= 36:
                    char = "@"
                elif column == 37:
                    char = "("
                elif 38 <= column <= 41:
                    char = "#"
                elif column == 42:
                    char = ","
                elif column == 43:
                    char = "."
                elif column == 45:
                    char = "."
                elif column == 46:
                    char = "#"
                elif column == 47:
                    char = "."
                elif column == 48:
                    char = "*"
                elif column == 49:
                    char = ","
                elif column == 50:
                    char = "*"
                elif column == 51:
                    char = "."
                elif column == 52:
                    char = "*"
                elif column == 53:
                    char = "."
                elif column == 54:
                    char = "."
                elif 55 <= column <= 58:
                    char = "#"
                elif column == 59:
                    char = "."
                elif column == 60:
                    char = "*"
                elif column == 61:
                    char = "#"
                elif column == 62:
                    char = "/"
            elif row == 2:
                if column == 22:
                    char = "&"
                elif 23 <= column <= 26:
                    char = "@"
                elif column == 27:
                    char = "&"
                elif 28 <= column <= 29:
                    char = "%"
                elif column == 30:
                    char = "#"
                elif column == 31:
                    char = "%"
                elif column == 32:
                    char = "#"
                elif column == 33:
                    char = "&"
                elif 34 <= column <= 36:
                    char = "@"
                elif column == 37:
                    char = "&"
                elif column == 38:
                    char = "%"
                elif column == 39:
                    char = "*"
                elif column == 40:
                    char = ","
                elif 41 <= column <= 44:
                    char = ">"
                elif 45 <= column <= 48:
                    char = "."
                elif 49 <= column <= 55:
                    char = "#"
                elif 56 <= column <= 58:
                    char = "."
                elif column == 59:
                    char = "@"
                elif column == 60:
                    char = "#"
                elif column == 61:
                    char = "@"
                elif column == 62:
                    char = "#"
                elif column == 63:
                    char = "@"
                elif column == 64:
                    char = "#"
                elif column == 65:
                    char = "@"
                elif column == 66:
                    char = "."

            elif row == 3:
                if 20 <= column <= 28:
                    char = "@"
                elif 29 <= column <= 30:
                    char = "&"
                elif 31 <= column <= 32:
                    char = "@"
                elif column == 33:
                    char = "%"
                elif 34 <= column <= 38:
                    char = "@"
                elif column == 39:
                    char = "%"
                elif column == 40:
                    char = "#"
                elif column == 41:
                    char = "/"
                elif column == 42:
                    char = "*"
                elif column == 43:
                    char = "("
                elif column == 44:
                    char = "/"
                elif column == 46:
                    char = "."
                elif column == 48:
                    char = "."
                elif column == 49:
                    char = "%"
                elif column == 50:
                    char = "&"
                elif column == 51:
                    char = "%"
                elif 52 <= column <= 54:
                    char = "#"
                elif 55 <= column <= 56:
                    char = "*"
                elif column == 57:
                    char = ","
                elif column == 58:
                    char = "."
                elif column == 59:
                    char = "@"
                elif column == 60:
                    char = "#"
                elif column == 61:
                    char = "@"
                elif column == 62:
                    char = "#"
                elif column == 63:
                    char = "@"
                elif column == 64:
                    char = "#"
                elif column == 65:
                    char = "@"
                elif column == 66:
                    char = "#"
                elif 67 <= column <= 68:
                    char = "@"
                elif column == 69:
                    char = "."
            elif row == 4:
                if column == 19:
                    char = "@"
                elif column == 20:
                    char = "&"
                elif 21 <= column <= 22:
                    char = "@"
                elif column == 23:
                    char = "&"
                elif column == 24:
                    char = "@"
                elif column == 25:
                    char = "&"
                elif column == 26:
                    char = "@"
                elif column == 27:
                    char = "#"
                elif column == 28:
                    char = "&"
                elif column == 29:
                    char = "%"
                elif 30 <= column <= 31:
                    char = "&"
                elif 32 <= column <= 33:
                    char = "#"
                elif column == 34:
                    char = "%"
                elif column == 35:
                    char = "@"
                elif column == 36:
                    char = "&"
                elif column == 37:
                    char = "@"
                elif 38 <= column <= 39:
                    char = "&"
                elif 40 <= column <= 41:
                    char = "%"
                elif 42 <= column <= 43:
                    char = "&"
                elif column == 44:
                    char = "#"
                elif column == 45:
                    char = "("
                elif column == 46:
                    char = "%"
                elif 47 <= column <= 49:
                    char = "@"
                elif column == 50:
                    char = "&"
                elif column == 51:
                    char = "@"
                elif column == 52:
                    char = "#"
                elif 53 <= column <= 55:
                    char = "%"
                elif 56 <= column <= 58:
                    char = "("
                elif column == 59:
                    char = "/"
                elif column == 60:
                    char = ","
                elif column == 61:
                    char = "@"
                elif column == 62:
                    char = "#"
                elif column == 63:
                    char = "@"
                elif column == 64:
                    char = "#"
                elif 65 <= column <= 66:
                    char = "@"
                elif column == 67:
                    char = "#"
            elif row == 5:
                if 18 <= column <= 21:
                    char = "&"
                elif 22 <= column <= 25:
                    char = "@"
                elif column == 26:
                    char = "&"
                elif 27 <= column <= 32:
                    char = "@"
                elif 33 <= column <= 34:
                    char = "&"
                elif column == 35:
                    char = "%"
                elif column == 36:
                    char = "#"
                elif column == 37:
                    char = "&"
                elif column == 38:
                    char = "@"
                elif column == 39:
                    char = "%"
                elif column == 40:
                    char = "&"
                elif column == 41:
                    char = "%"
                elif 42 <= column <= 43:
                    char = "#"
                elif 44 <= column <= 45:
                    char = "("
                elif column == 46:
                    char = "#"
                elif 47 <= column <= 48:
                    char = "%"
                elif 49 <= column <= 51:
                    char = "@"
                elif 52 <= column <= 53:
                    char = "&"
                elif column == 54:
                    char = "@"
                elif column == 55:
                    char = "%"
                elif column == 56:
                    char = "&"
                elif 57 <= column <= 58:
                    char = "%"
                elif column == 59:
                    char = "#"
                elif column == 60:
                    char = "*"
                elif column == 61:
                    char = "#"
                elif column == 62:
                    char = "/"
                elif column == 63:
                    char = "*"
                elif column == 64:
                    char = "."
                elif column == 65:
                    char = "*"
                elif 66 <= column <= 68:
                    char = "."
                elif column == 69:
                    char = "#"
            elif row == 6:
                if column == 17:
                    char = "@"
                elif 18 <= column <= 19:
                    char = "&"
                elif column == 20:
                    char = "@"
                elif column == 21:
                    char = "&"
                elif 22 <= column <= 24:
                    char = "@"
                elif column == 25:
                    char = "&"
                elif 26 <= column <= 32:
                    char = "@"
                elif 33 <= column <= 34:
                    char = "%"
                elif column == 35:
                    char = "#"
                elif column == 36:
                    char = "("
                elif column == 37:
                    char = "*"
                elif column == 38:
                    char = ","
                elif 39 <= column <= 48:
                    char = "."
                elif column == 49:
                    char = ","
                elif 50 <= column <= 51:
                    char = "/"
                elif column == 52:
                    char = "#"
                elif column == 53:
                    char = "%"
                elif 54 <= column <= 55:
                    char = "&"
                elif column == 56:
                    char = "/"
                elif column == 57:
                    char = "("
                elif 58 <= column <= 60:
                    char = "/"
                elif column == 61:
                    char = "."
                elif column == 62:
                    char = "@"
                elif 63 <= column <= 66:
                    char = "#"
                elif 67 <= column <= 68:
                    char = ","
                elif column == 69:
                    char = "."

            elif row == 7:
                if column == 17:
                    char = "@"
                elif 18 <= column <= 21:
                    char = "&"
                elif column == 22:
                    char = "@"
                elif 23 <= column <= 24:
                    char = "&"
                elif 25 <= column <= 27:
                    char = "@"
                elif 28 <= column <= 29:
                    char = "&"
                elif column == 30:
                    char = "%"
                elif column == 31:
                    char = "&"
                elif column == 32:
                    char = "%"
                elif 33 <= column <= 35:
                    char = "("
                elif column == 36:
                    char = "*"
                elif 37 <= column <= 38:
                    char = ","
                elif column == 39:
                    char = "."
                elif 57 <= column <= 58:
                    char = "."
                elif 61 <= column <= 62:
                    char = "."
                elif column == 63:
                    char = "*"
                elif column == 66:
                    char = "*"
                elif 67 <= column <= 68:
                    char = "/"
            elif row == 8:
                if 17 <= column <= 19:
                    char = "@"
                elif 20 <= column <= 21:
                    char = "&"
                elif column == 22:
                    char = "@"
                elif column == 23:
                    char = "&"
                elif column == 24:
                    char = "@"
                elif 25 <= column <= 26:
                    char = "&"
                elif column == 27:
                    char = "@"
                elif 28 <= column <= 29:
                    char = "&"
                elif 30 <= column <= 31:
                    char = "#"
                elif 32 <= column <= 33:
                    char = "("
                elif 34 <= column <= 35:
                    char = "/"
                elif 36 <= column <= 38:
                    char = "*"
                elif 39 <= column <= 40:
                    char = ","
                elif column == 41:
                    char = "."
                elif 63 <= column <= 64:
                    char = "*"
                elif column == 65:
                    char = "("
                elif column == 66:
                    char = "#"
            elif row == 9:
                if column == 17:
                    char = "@"
                elif column == 18:
                    char = "&"
                elif 19 <= column <= 23:
                    char = "@"
                elif column == 24:
                    char = "&"
                elif 25 <= column <= 28:
                    char = "@"
                elif column == 29:
                    char = "&"
                elif 30 <= column <= 31:
                    char = "%"
                elif column == 32:
                    char = "#"
                elif column == 33:
                    char = "("
                elif 34 <= column <= 36:
                    char = "/"
                elif column == 37:
                    char = "*"
                elif 38 <= column <= 39:
                    char = "/"
                elif column == 40:
                    char = "*"
                elif 41 <= column <= 42:
                    char = "/"
                elif column == 43:
                    char = "*"
                elif column == 44:
                    char = ","
                elif column == 45:
                    char = "."
                elif column == 46:
                    char = "."
                elif column == 64:
                    char = "."
                elif column == 65:
                    char = ","
                elif column == 66:
                    char = "*"
            elif row == 10:
                if column == 17:
                    char = "&"
                elif column == 18:
                    char = "&"
                elif column == 19:
                    char = "&"
                elif column == 20:
                    char = "@"
                elif column == 21:
                    char = "&"
                elif column == 22:
                    char = "@"
                elif column == 23:
                    char = "&"
                elif column == 24:
                    char = "@"
                elif column == 25:
                    char = "&"
                elif column == 26:
                    char = "@"
                elif column == 27:
                    char = "&"
                elif column == 28:
                    char = "&"
                elif 29 <= column <= 30:
                    char = "%"
                elif column == 31:
                    char = "#"
                elif 32 <= column <= 34:
                    char = "("
                elif 35 <= column <= 36:
                    char = "/"
                elif 37 <= column <= 38:
                    char = "*"
                elif 39 <= column <= 41:
                    char = ","
                elif 42 <= column <= 43:
                    char = "."
                elif column == 64:
                    char = "#"
            elif row == 11:
                if 17 <= column <= 20:
                    char = "@"
                elif column == 21:
                    char = "#"
                elif column == 22:
                    char = "/"
                elif column == 23:
                    char = "%"
                elif 24 <= column <= 25:
                    char = "@"
                elif 26 <= column <= 27:
                    char = "&"
                elif column == 28:
                    char = "#"
                elif 29 <= column <= 30:
                    char = "/"
                elif column == 31:
                    char = "*"
                elif 32 <= column <= 34:
                    char = "/"
                elif column == 35:
                    char = ","
                elif column == 36:
                    char = "."
                elif 37 <= column <= 41:
                    char = ","
                elif column == 42:
                    char = "."
                elif column == 43:
                    char = ","
                elif column == 44:
                    char = "."
                elif 45 <= column <= 47:
                    char = "."
                elif column == 48:
                    char = " "
                elif column == 49:
                    char = "."
                elif column == 50:
                    char = "."
                elif 51 <= column <= 61:
                    char = " "
                elif column == 62:
                    char = ","
                elif column == 63 :
                    char = "."
                elif column == 64:
                    char = "#"

            elif row == 12:
                if 18 <= column <= 21:
                    char = "@"
                elif column == 22:
                    char = "&"
                elif 23 <= column <= 26:
                    char = "#"
                elif 27 <= column <= 28:
                    char = "%"
                elif column == 29:
                    char = "("
                elif 30 <= column <= 33:
                    char = "*"
                elif column == 34:
                    char = "/"
                elif column == 35:
                    char = "#"
                elif 36 <= column <= 37:
                    char = "&"
                elif 38 <= column <= 49:
                    char = "@"
                elif column == 50:
                    char = "("
                elif column == 51:
                    char = ","
                elif column == 52:
                    char = "."
                elif column == 53:
                    char = "("
                elif column == 54:
                    char = "%"
                elif column == 55:
                    char = "&"
                elif column == 56:
                    char = "@"
                elif column == 57:
                    char = "&"
                elif column == 58:
                    char = "/"
                elif 59 <= column <= 61:
                    char = " "
                elif column == 62:
                    char = "."
                elif column == 63:
                    char = "#"
            elif row == 13:
                if 19 <= column <= 21:
                    char = "@"
                elif column == 22:
                    char = "("
                elif 23 <= column <= 24:
                    char = "@"
                elif column == 25:
                    char = "#"
                elif column == 26:
                    char = "*"
                elif 27 <= column <= 29:
                    char = "*"
                elif column == 30:
                    char = ","
                elif column == 31:
                    char = ","
                elif column == 32:
                    char = "*"
                elif column == 33:
                    char = "/"
                elif column == 34:
                    char = "#"
                elif column == 35:
                    char = "%"
                elif column == 36:
                    char = "&"
                elif column == 37:
                    char = "*"
                elif column == 38:
                    char = "#"
                elif column == 39:
                    char = "."
                elif column == 40:
                    char = "."
                elif column == 41:
                    char = "#"
                elif column == 42:
                    char = "@"
                elif column == 43:
                    char = "&"
                elif column == 44:
                    char = "@"
                elif column == 45:
                    char = "&"
                elif column == 46:
                    char = "*"
                elif column == 47:
                    char = " "
                elif 48 <= column <= 50:
                    char = "#"
                elif 51 <= column <= 53:
                    char = "@"
                elif column == 54:
                    char = "."
                elif 55 <= column <= 57:
                    char = "@"
                elif column == 58:
                    char = "("
                elif column == 59:
                    char = " "
                elif column == 60:
                    char = " "
                elif column == 61:
                    char = " "
                elif column == 62:
                    char = "."
                elif column == 63:
                    char = "#"

            elif row == 14:
                if 20 <= column <= 21:
                    char = "@"
                elif column == 22:
                    char = "#"
                elif column == 23:
                    char = "/"
                elif 24 <= column <= 26:
                    char = "#"
                elif 27 <= column <= 28:
                    char = "("
                elif column == 29:
                    char = "/"
                elif 30 <= column <= 32:
                    char = "*"
                elif column == 33:
                    char = ","
                elif 34 <= column <= 36:
                    char = "."
                elif 37 <= column <= 38:
                    char = ","
                elif column == 39:
                    char = "."
                elif column == 40:
                    char = " "
                elif 41 <= column <= 42:
                    char = "."
                elif column == 43:
                    char = " "
                elif 44 <= column <= 46:
                    char = "."
                elif 47 <= column <= 49:
                    char = ","
                elif 50 <= column <= 51:
                    char = "*"
                elif 52 <= column <= 54:
                    char = " "
                elif 55 <= column <= 56:
                    char = ","
                elif column == 57:
                    char = "#"
                elif column == 58:
                    char = "("
                elif column == 59:
                    char = "*"
                elif column == 60:
                    char = "."
                elif column == 61:
                    char = ","
                elif column == 62:
                    char = "#"

            elif row == 15:
                if column == 21:
                    char = "@"
                elif column == 22:
                    char = "("
                elif column == 23:
                    char = "#"
                elif column == 24:
                    char = "&"
                elif column == 25:
                    char = "@"
                elif 26 <= column <= 32:
                    char = "("
                elif column == 33:
                    char = "/"
                elif column == 34:
                    char = "*"
                elif column == 35:
                    char = ","
                elif 36 <= column <= 42:
                    char = "."
                elif column == 43:
                    char = ","
                elif 44 <= column <= 45:
                    char = "*"
                elif 46 <= column <= 51:
                    char = " "
                elif column == 52:
                    char = "."
                elif 53 <= column <= 57:
                    char = " "
                elif column == 58:
                    char = " "
                elif column == 59:
                    char = "#"
            elif row == 16:
                if 23 <= column <= 24:
                    char = "@"
                elif column == 25:
                    char = "&"
                elif column == 26:
                    char = "%"
                elif 27 <= column <= 28:
                    char = "/"
                elif column == 29:
                    char = "("
                elif 30 <= column <= 33:
                    char = "#"
                elif column == 34:
                    char = "("
                elif column == 35:
                    char = "/"
                elif 36 <= column <= 37:
                    char = ","
                elif 38 <= column <= 40:
                    char = "."
                elif column == 41:
                    char = ","
                elif column == 42:
                    char = "%"
                elif column == 43:
                    char = "#"
                elif column == 44:
                    char = "*"
                elif column == 45:
                    char = "("
                elif column == 46:
                    char = "/"
                elif column == 47:
                    char = "."
                elif 48 <= column <= 57:
                    char = " "
                elif column == 58:
                    char = "*"
            elif row == 17:
                if 24 <= column <= 25:
                    char = "%"
                elif column == 26:
                    char = "#"
                elif column == 27:
                    char = "*"
                elif column == 28:
                    char = "/"
                elif 29 <= column <= 30:
                    char = "("
                elif 31 <= column <= 32:
                    char = "#"
                elif 33 <= column <= 35:
                    char = "%"
                elif 36 <= column <= 37:
                    char = "("
                elif column == 38:
                    char = "/"
                elif column == 39:
                    char = "*"
                elif 40 <= column <= 41:
                    char = "/"
                elif column == 42:
                    char = "#"
                elif 43 <= column <= 47:
                    char = "@"
                elif 48 <= column <= 49:
                    char = "&"
                elif column == 50:
                    char = ","
                elif column == 51:
                    char = "#"
                elif column == 52:
                    char = "."
                elif 53 <= column <= 56:
                    char = " "
                elif column == 57:
                    char = "/"
            elif row == 18:
                if column == 25:
                    char = "("
                elif column == 26:
                    char = "%"
                elif 27 <= column <= 28:
                    char = "("
                elif column == 29:
                    char = "/"
                elif 30 <= column <= 31:
                    char = "("
                elif 32 <= column <= 33:
                    char = "#"
                elif 34 <= column <= 35:
                    char = "%"
                elif 36 <= column <= 37:
                    char = "&"
                elif column == 38:
                    char = "%"
                elif column == 39:
                    char = "("
                elif column == 40:
                    char = "#"
                elif 41 <= column <= 43:
                    char = "("
                elif column == 44:
                    char = "#"
                elif column == 45:
                    char = "%"
                elif column == 46:
                    char = "&"
                elif column == 47:
                    char = "%"
                elif column == 48:
                    char = "."
                elif 49 <= column <= 52:
                    char = " "
                elif column == 53:
                    char = "("
                elif column == 54:
                    char = ","
                elif column == 55:
                    char = "."
                elif column == 56:
                    char = " "
                elif column == 57:
                    char = "#"
            elif row == 19:
                if 26 <= column <= 27:
                    char = "("
                elif column == 28:
                    char = "/"
                elif 29 <= column <= 31:
                    char = "("
                elif column == 32:
                    char = "#"
                elif 33 <= column <= 34:
                    char = "("
                elif column == 35:
                    char = "*"
                elif column == 36:
                    char = "/"
                elif column == 37:
                    char = "&"
                elif 38 <= column <= 39:
                    char = "#"
                elif column == 40:
                    char = "%"
                elif 41 <= column <= 42:
                    char = "&"
                elif 43 <= column <= 46:
                    char = "@"
                elif column == 47:
                    char = "&"
                elif column == 48:
                    char = "#"
                elif column == 49:
                    char = "("
                elif 50 <= column <= 52:
                    char = "."
                elif column == 53:
                    char = " "
                elif column == 54:
                    char = "#"
            elif row == 20:
                if column == 25:
                    char = "/"
                elif column == 26:
                    char = "("
                elif 27 <= column <= 29:
                    char = "#"
                elif 30 <= column <= 32:
                    char = "("
                elif 33 <= column <= 34:
                    char = "#"
                elif column == 35:
                    char = "("
                elif 36 <= column <= 40:
                    char = "/"
                elif column == 41:
                    char = "("
                elif column == 42:
                    char = "*"
                elif column == 43:
                    char = ","
                elif 44 <= column <= 45:
                    char = "*"
                elif column == 46:
                    char = "."
                elif 47 <= column <= 48:
                    char = " "
                elif column == 49:
                    char = "."
                elif 50 <= column <= 52:
                    char = " "
                elif column == 53:
                    char = "#"
            elif  row == 21:
                if column == 25:
                    char = "*"
                elif 26 <= column <= 28:
                    char = "@"
                elif column == 29:
                    char = "%"
                elif column == 30:
                    char = "/"
                elif column == 31:
                    char = "("
                elif column == 32:
                    char = "#"
                elif 33 <= column <= 34:
                    char = "%"
                elif column == 35:
                    char = "&"
                elif 36 <= column <= 37:
                    char = "%"
                elif 38 <= column <= 39:
                    char = "&"
                elif column == 40:
                    char = "%"
                elif column == 41:
                    char = "#"
                elif column == 42:
                    char = "("
                elif column == 43:
                    char = "/"
                elif column == 44:
                    char = "("
                elif column == 45:
                    char = "*"
                elif 46 <= column <= 54:
                    char = "."
                elif column == 55:
                    char = ","
            elif row == 22:
                if column == 25:
                    char = ","
                elif 26 <= column <= 30:
                    char = "@"
                elif 31 <= column <= 32:
                    char = "#"
                elif 33 <= column <= 40:
                    char = "%"
                elif 41 <= column <= 46:
                    char = "&"
                elif column == 47:
                    char = "%"
                elif column == 48:
                    char = "("
                elif column == 49:
                    char = "/"
                elif column == 50:
                    char = ","
                elif column == 51:
                    char = "."
            elif row == 23:
                if 23 <= column <= 24:
                    char = "@"
                elif column == 25:
                    char = "%"
                elif column == 26:
                    char = "@"
                elif column == 27:
                    char = "&"
                elif 28 <= column <= 30:
                    char = "@"
                elif 31 <= column <= 34:
                    char = "&"
                elif 35 <= column <= 36:
                    char = "%"
                elif 37 <= column <= 38:
                    char = "&"
                elif 39 <= column <= 41:
                    char = "@"
                elif 42 <= column <= 43:
                    char = "&"
                elif column == 44:
                    char = "/"
                elif 45 <= column <= 46:
                    char = " "
                elif 47 <= column <= 52:
                    char = "#"
            elif row == 24:
                if 21 <= column <= 26:
                    char = "@"
                elif 27 <= column <= 28:
                    char = "&"
                elif column == 29:
                    char = "%"
                elif 30 <= column <= 31:
                    char = "@"
                elif column == 32:
                    char = "&"
                elif 33 <= column <= 34:
                    char = "@"
                elif 35 <= column <= 40:
                    char = "&"
                elif column == 41:
                    char = "#"
                elif column == 42:
                    char = "/"
                elif column == 43:
                    char = ","
                elif 44 <= column <= 45:
                    char = " "
                elif column == 46:
                    char = "@"
                elif 47 <= column <= 48:
                    char = "%"
                elif 49 <= column <= 50:
                    char = "/"      
            elif row == 25:
                if 17 <= column <= 29:
                    char = "@"
                elif 30 <= column <= 31:
                    char = "&"
                elif column == 32:
                    char = "@"
                elif column == 33:
                    char = "&"
                elif 34 <= column <= 37:
                    char = "@"
                elif column == 38:
                    char = "%"
                elif 39 <= column <= 40:
                    char = "("
                elif column == 41:
                    char = "/"
                elif 42 <= column <= 43:
                    char = "*"
                elif column == 44:
                    char = ","
                elif 45 <= column <= 46:
                    char = " "
                elif column == 47:
                    char = "#"
                elif column == 48:
                    char = "@"
                elif 49 <= column <= 50:
                    char = " "
                elif column == 51:
                    char = "."
                elif 52 <= column <= 53:
                    char = "("
                elif 54 <= column <= 55:
                    char = "."
                elif column == 56:
                    char = ","
                elif 57 <= column <= 58:
                    char = "*"
            elif row == 26:
                if 13 <= column <= 17:
                    char = "@"
                elif column == 18:
                    char = "&"
                elif 19 <= column <= 26:
                    char = "@"
                elif column == 27:
                    char = "&"
                elif column == 28:
                    char = "@"
                elif column == 29:
                    char = "&"
                elif 30 <= column <= 32:
                    char = "@"
                elif column == 33:
                    char = "&"
                elif 34 <= column <= 38:
                    char = "@"
                elif column == 39:
                    char = "&"
                elif 40 <= column <= 44:
                    char = "."
                elif column == 45:
                    char = "&"
                elif column == 46:
                    char = "@"
                elif column == 47:
                    char = "."
                elif 48 <= column <= 49:
                    char = " "
                elif column == 50:
                    char = "."
                elif column == 51:
                    char = " "
                elif column == 52:
                    char = "*"
                elif column == 53:
                    char = "%"
                elif column == 54:
                    char = "/"
                elif 55 <= column <= 60:
                    char = ","
                elif 61 <= column <= 62:
                    char = "."
                elif column == 63:
                    char = "/"
                elif column == 64:
                    char = "%"
                elif column == 65:
                    char = "#"
                elif column == 66:
                    char = "("
                elif 67 <= column <= 68:
                    char = "&"
                elif column == 69:
                    char = "/"
            elif row == 27:
                if column == 9:
                    char = "&"
                elif column == 10:
                    char = "@"
                elif 11 <= column <= 17:
                    char = "&"
                elif column == 18:
                    char = "%"
                elif column == 19:
                    char = "&"
                elif column == 20:
                    char = "@"
                elif column == 21:
                    char = "&"
                elif column == 22:
                    char = "%"
                elif 23 <= column <= 25:
                    char = "&"
                elif column == 26:
                    char = "%"
                elif column == 27:
                    char = "("
                elif column == 28:
                    char = "#"
                elif column == 29:
                    char = "%"
                elif column == 30:
                    char = "@"
                elif column == 31:
                    char = "/"
                elif 32 <= column <= 33:
                    char = ","
                elif column == 34:
                    char = "#"
                elif 35 <= column <= 36:
                    char = "@"
                elif column == 37:
                    char = "&"
                elif column == 38:
                    char = "%"
                elif column == 39:
                    char = "@"
                elif 40 <= column <= 41:
                    char = "%"
                elif column == 42:
                    char = "@"
                elif column == 43:
                    char = "%"
                elif column == 48:
                    char = ","
                elif column == 49:
                    char = "*"
                elif column == 50:
                    char = "."
                elif 51 <= column <= 52:
                    char = "/"
                elif column == 53:
                    char = "("
                elif 54 <= column <= 55:
                    char = "*"
                elif 56 <= column <= 58:
                    char = ","
                elif column == 59:
                    char = "*"
                elif column == 60:
                    char = ","
                elif column == 61:
                    char = "*"
                elif 62 <= column <= 63:
                    char = "@"
                elif column == 64:
                    char = "/"
                elif 65 <= column <= 66:
                    char = ","
                elif column == 67:
                    char = "/"
                elif column == 68:
                    char = ","
                elif column == 69:
                    char = "."
            elif row == 28:
                if 6 <= column <= 7:
                    char = "%"
                elif column == 8:
                    char = "&"
                elif column == 9:
                    char = "@"
                elif column == 10:
                    char = "&"
                elif 11 <= column <= 12:
                    char = "%"
                elif column == 13:
                    char = "#"
                elif 14 <= column <= 15:
                    char = "%"
                elif column == 16:
                    char = "&"
                elif column == 17:
                    char = "%"
                elif column == 18:
                    char = "#"
                elif column == 19:
                    char = "@"
                    
                    
                elif column == 20:
                    char = "#"
                elif column == 21:
                    char = "("
                elif column == 22:
                    char = "%"
                elif column == 23:
                    char = "&"
                elif 24 <= column <= 25:
                    char = "#"
                elif column == 26:
                    char = "%"
                elif 27 <= column <= 28:
                    char = "&"
                elif column == 29:
                    char = "/"
                elif 30 <= column <= 31:
                    char = "("
                elif column == 32:
                    char = "&"
                elif column == 33:
                    char = "@"
                elif column == 34:
                    char = ","
                elif column == 35:
                    char = "#"
                elif 36 <= column <= 37:
                    char = "*"
                elif column == 38:
                    char = "("
                elif column == 39:
                    char = "*"
                elif column == 40:
                    char = "#"
                elif 41 <= column <= 42:
                    char = " "
                elif column == 43:
                    char = "@"
                elif column == 44:
                    char = " "
                elif 45 <= column <= 46:
                    char = ","
                elif 47 <= column <= 50:
                    char = " "
                elif column == 51:
                    char = "."
                elif column == 52:
                    char = ","
                elif column == 53:
                    char = "#"
                elif column == 54:
                    char = "*"
                elif column == 55:
                    char = "#"
                elif column == 56:
                    char = "/"
                elif 57 <= column <= 58:
                    char = "*"
                elif 59 <= column <= 62:
                    char = ","
                elif column == 63:
                    char = "&"
                elif 64 <= column <= 65:
                    char = "@"
                elif column == 66:
                    char = "%"
                elif 67 <= column <= 70:
                    char = ","
                elif column == 71:
                    char = "*"
                elif column == 72:
                    char = ","
            print(char, end="")
        print()


generate_ascii_art()

            
