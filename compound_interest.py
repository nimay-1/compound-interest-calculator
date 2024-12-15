# Definition of a function to ask for a positive value
def request_positive_value(message, positive_value, reiterate_value, msg_valueerror):
    while True:
        try:
            positive_value = float(input(message))
            while positive_value <= 0:
                positive_value = float(input(reiterate_value))
            break
        except ValueError:
            print(msg_valueerror)
    return positive_value

# Using the previously defined function to ask for the values needed to perform the final calculation
initial_capital = request_positive_value("Enter your initial capital: ", int, "Your initial capital must be greater than 0: ", "Please enter a valid value (integer): ")
interest_rate = request_positive_value("Enter your annual interest rate in % (e.g., for 4% type 4): ", float, "Your interest rate must be greater than 0: ", "Please enter a valid value (integer): ")
compounding_frequency = request_positive_value("Enter your compounding frequency in number of months per year: ", int, "Your compounding frequency must be greater than 0: ", "Please enter a valid value (integer): ")
investment_duration = request_positive_value("Enter your investment duration (in years): ", int, "Your investment duration must be greater than 0: ", "Please enter a valid value (integer): ")

# Calculating the final amount using the collected values
final_amount = initial_capital * (1 + (interest_rate / 100) / compounding_frequency) ** (compounding_frequency * investment_duration)

# Returning the result to the user
print(f"\nYou plan to grow {int(initial_capital)}€ over {int(investment_duration)} year(s) with an interest rate of {interest_rate}%")
print(f"At the end of {int(investment_duration)} year(s), your capital will amount to {final_amount:.2f}€")
