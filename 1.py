def convert_temperature(temp, unit):
    conversions = {
        'c': (temp * 9/5) + 32, temp + 273.15, temp,
        'f': (temp - 32) * 5/9, (temp + 459.67) - 273.15, temp,
        'k': temp - 273.15, (temp - 273.15) * 9/5 + 32, temp
    }
    return conversions[unit]

def main():
    temperature = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original unit of measurement (C, F, K): ").lower()
    if original_unit in ['c', 'f', 'k']:
        c, f, k = convert_temperature(temperature, original_unit)
        print("The equivalent temperatures are:")
        units = {'c': 'degrees C', 'f': 'degrees F', 'k': 'Kelvin'}
        for unit, value in zip(['f', 'k', 'c'], [f, k, c]):
            if unit != original_unit:
                print(f"{value:.2f} {units[unit]}")
    else:
        print("Invalid unit of measurement. Please enter C, F, or K.")

if __name__ == "__main__":
    main()
