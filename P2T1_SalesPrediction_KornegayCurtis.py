# Program that asks the user to enter the projected amount of total sales.
# Then displays the profit that will be made from that amount.
# February, 17, 2020
# CTI-110 P2T1 - Sales Prediction
# Curtis Kornegay

# Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of totasl sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))


