import argparse
ap = argparse.ArgumentParser()


ap.add_argument("-a", "--first_operand", required=True,
   help="first operand")
ap.add_argument("-b", "--second_operand", required=True,
   help="second operand")
args = vars(ap.parse_args())


print("Sum is {}".format(int(args['first_operand']) + int(args['second_operand'])))
print("Sub is {}".format(int(args['first_operand']) - int(args['second_operand'])))
print("Div is {}".format(int(args['first_operand']) / int(args['second_operand'])))
print("Mul is {}".format(int(args['first_operand']) * int(args['second_operand'])))
