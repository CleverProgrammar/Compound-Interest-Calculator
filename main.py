if __name__ == "__main__":
    principle_amount = int(input("Enter the principle amount: "))
    rate_of_interest = int(input("Enter the rate of interest: "))
    interest_years = int(input("Enter the years to compute the interest: "))
    total_amount = principle_amount
    for _ in range(interest_years):
        total_amount += rate_of_interest * total_amount * .01
    print(total_amount)