#!/usr/bin/env python3
# Created By: Kaylee R
# Date: 04, 11, 2026
# This program is for a shipping company. It asks the user
# to enter the dimensions of the package they want to deliver.
# If the weight and the volume of the package are under the limit,
# it lets them select a method of shipping. 


def main():
    # greet user
    print("Welcome to TateXpress Shipping")

    # get user's package dimensions
    print("Please enter you package dimensions")
    p_weight = input("Enter the weight in kg: ")
    p_length = input("Enter the length in cm: ")
    p_width = input("Enter the width in cm: ")
    p_height = input("Enter the height in cm: ")

    # try to cast dimensions to decimals
    try:
        weight_int = float(p_weight)
        length_int = float(p_length)
        width_int = float(p_width)
        height_int = float(p_height)

        # calculate the package weigth and height
        volume_int = height_int * length_int * width_int

        # show user their package weight and volume
        print(
            "Your package weighs {:.2f}kg and has a volume of {:.2f}cm³".format(
                weight_int, volume_int
            )
        )

        if weight_int > 27 or volume_int > 10000:
            print("Your package exceeds company weight and volume limits")
        else:
            # let user select shipping method
            print("Next, please select your shipping method")
            shipping = input("1 for truck, 2 for cargo and 3 for plane: ")

            try:
                shipping_int = int(shipping)

                # check if package is eligable for selected shipping method
                if shipping_int == 1 and weight_int <= 10:
                    print("Your package can be delivered by truck")
                    print("Expect delivery in 3-5 business days!")
                elif shipping_int == 2 and weight_int <= 20:
                    print("You package can be delivered by cargo")
                    print("Expect delivery in 5-10 business days!")
                elif shipping_int == 3 and weight_int <= 27:
                    print("Your package can be delivered by plane")
                    print("Expect delivery in 1-2 business days!")
                else:
                    print("Your package is too heavy for the shipping method")
                    print("Please select a different shipping method")

            except:
                print("Please select the right shipping method")

    except:
        print("Dimension inputs must be integers")


if __name__ == "__main__":
    main()
