import pickle
import sqlite3

number = input('Give me a number:')

print(f'the double is: {float(number) * 2}')

some_text = '''Debitis explicabo maiores aliquid 
quia recusandae voluptatem. Accusantium repudiandae 
quia soluta ut nesciunt. Et eos est ducimus reiciendis.
'''

# Open for 'w'riting
f = open('some_text.txt', 'w')
# Write text to file
f.write(some_text)
# Close the file
f.close()

# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('some_text.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
# close the file
f.close()

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile, 'wb')
# Dump the object to a file
pickle.dump(shoplist, f)
f.close()

# Destroy the shoplist variable
del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)
f.close()

conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# Save (commit) the changes
conn.commit()

# get data
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
             ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
