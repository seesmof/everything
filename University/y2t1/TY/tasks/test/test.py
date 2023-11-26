def calculate_accuracy(measured_value, true_value):
    accuracy = abs((measured_value - true_value) / true_value)
    return accuracy


# Example usage:
measured_value = 99.5
true_value = 100
accuracy = calculate_accuracy(measured_value, true_value)
print(f"The accuracy of the measurement is {accuracy * 100}%")
