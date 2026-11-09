#!/usr/bin/env python3
# Created By: Kaylee R
# Date: 04, 11, 2026
# This program is for a shipping company. It asks the user
# to enter the dimensions of the package they want to deliver.
# If the weight and the volume of the package are under the limit,
# it lets them select a method of shipping.


def main():
    # greet the user
    print("Welcome to TateXpress Shipping")
    print()
    print("Note, the company has a weight and volume limit of 27kg and 10000cm³")
    print()

    # get user's package dimensions
    print("Please enter you package dimensions")
    p_weight = input("Enter the weight as kg: ")
    p_length = input("Enter the length as cm: ")
    p_width = input("Enter the width as cm: ")
    p_height = input("Enter the height as cm: ")

    # try to cast dimensions to decimals
    try:
        weight_int = float(p_weight)
        length_int = float(p_length)
        width_int = float(p_width)
        height_int = float(p_height)

        # calculate the package weight and height
        volume_int = height_int * length_int * width_int

        # show user their package weight and volume
        print(
            "Your package weighs {:.2f}kg and has a volume of {:.2f}cm³".format(
                weight_int, volume_int
            )
        )
        print()

        if weight_int > 27 or volume_int > 10000:
            print("Your package exceeds company weight and volume limits")
        elif weight_int < 0:
            print("Weight can not be negative")
        elif length_int < 0:
            print("Length can not be negative")
        elif width_int < 0:
            print("Width can not be negative")
        else:
            # let user select shipping method
            print("Next, please select your shipping method")
            print()
            print("Plane maximum weight limit is 10kg")
            print("Truck maximum weight limit is 15kg")
            print("Cargo maximum weight limit is 27kg")
            print()
            shipping = input("1 for plane, 2 for truck and 3 for cargo: ")

            try:
                shipping_int = int(shipping)

                # check if package is eligible for selected shipping method
                if shipping_int == 1 and weight_int <= 10:
                    print("Your package can be delivered by plane")
                    print("Expect delivery in 3-5 business days!")
                elif shipping_int == 2 and weight_int <= 15:
                    print("You package can be delivered by truck")
                    print("Expect delivery in 5-10 business days!")
                elif shipping_int == 3 and weight_int <= 27:
                    print("Your package can be delivered by cargo")
                    print("Expect delivery in 1-2 business days!")
                elif shipping_int > 3:
                    print("Please select the correct shipping method")
                else:
                    print("Your package is too heavy for the shipping method")
                    print("Please select a different shipping method")

            except:
                print("Please select the right shipping method")

    except:
        print("Dimension inputs must be integers")


if __name__ == "__main__":
    main()
