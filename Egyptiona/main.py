def egyptian_fraction(numerator, denominator):
    fractions = []

    while numerator > 0:
        unit_fraction_denominator = (denominator + numerator - 1) // numerator
        fractions.append(f"1/{unit_fraction_denominator}")
        numerator = numerator * unit_fraction_denominator - denominator
        denominator = denominator * unit_fraction_denominator

    return fractions


# Taking input from the user
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

if numerator <= 0 or denominator <= 0:
    print("Numerator and denominator must be positive integers.")
else:
    if numerator > denominator:
        whole_part = numerator // denominator
        numerator -= whole_part * denominator
        fractions = [f"{whole_part}"] + egyptian_fraction(numerator, denominator)
    else:
        fractions = egyptian_fraction(numerator, denominator)

    print(f"Egyptian Fraction Representation: {' + '.join(fractions)}")
