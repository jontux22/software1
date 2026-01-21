size=float(input("Enter the length of the zander in centimeters: "))
if size < 42:
 print("The zander does not meet the size limit.")
 print("Please release the fish back into the lake.")
missing_centimeters = (42-size)
if size < 42:
 print(f"The fish was(missing_centimeters:6.2f) centimeters below the size limit.")
if size >= 42:
 print("The zander meets the size limit.")
