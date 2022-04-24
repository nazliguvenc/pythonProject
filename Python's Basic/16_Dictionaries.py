# dictionaries ==> {} , key and value , key must be unique ( like a Map in Java)

# Example: Jan -> January /  Mar -> March
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv", "Not a value"))

