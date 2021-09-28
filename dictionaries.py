# Jan -> January
# Mar -> March
# all keys have to be unique
monthConversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
}

print(monthConversions.get('May'))
print(monthConversions['Apr'])
print(monthConversions.get('abc', 'Not a valid key')) 
