def convert_temperature(temp, unit):
    if unit == 'c':
        return (temp * 9/5) + 32, temp + 273.15, temp
    elif unit == 'f':
        return (temp - 32) * 5/9, (temp + 459.67) - 273.15, temp
    elif unit == 'k':
        return temp - 273.15, (temp - 273.15) * 9/5 + 32, temp

def main():
    temperature = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original unit of measurement (C, F, K): ").lower()
    if original_unit in ['c', 'f', 'k']:
        c, f, k = convert_temperature(temperature, original_unit)
        print("The equivalent temperatures are:")
        if original_unit == 'c':
            print(f"{f:.2f} degrees F")
            print(f"{k:.2f} Kelvin")
        elif original_unit == 'f':
            print(f"{c:.2f} degrees C")
            print(f"{k:.2f} Kelvin")
        else:
            print(f"{c:.2f} degrees C")
            print(f"{f:.2f} degrees F")
    else:
        print("Invalid unit of measurement. Please enter C, F, or K.")

if __name__ == "__main__":
    main()