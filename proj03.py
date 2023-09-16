######
## Source Code
##
## Computer Project #3 display the proprites of a triangle promted by the user 
##
## create an empty variable and promot the value from the user to check of the user wants to try the program or not
##
## promot the sides of the triangle
##
## check if the it was a triangle or not and if it is a degenerate triangle or a valid triangle and print a message of what type of triangle it is  
##
## display the sides of the triangle with 1 decimal place
##
## calculate the angles of the triangle using the fourmla that was given in the wikipedia and then display it with 1 deciaml place
## check what type of triangle it is based on the information was given and calculated and then display the result to the user
##
## check if the user wants to try another triangle and if not, display a print statement og how many valid triangles it was
##
######
import math

BANNER = '''

╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃
╰╯┃┃┣┻┳┳━━┳━╮╭━━┫┃╭━━╮
╱╱┃┃┃╭╋┫╭╮┃╭╮┫╭╮┃┃┃┃━┫
╱╱┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰┫┃━┫
╱╱╰╯╰╯╰┻╯╰┻╯╰┻━╮┣━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
'''

print(BANNER)
print()
# create a variable named program_boot and set it empty so we can use it to let the user input the value of program_boot to see if the user would like to launch the program or not. 
program_boot= ""
number_of_valid_triangle= int(0)
program_boot= input("Do you wish to process a triangle (Y or N)?  " ).lower()
while program_boot != "n":
    # let the user promot the sides of the triangle 
    side_AB= float(input('\nEnter length of side AB: '))
    side_BC= float(input('\nEnter length of side BC: '))
    side_CA = float(input('\nEnter length of side CA: '))
    # check if the sides verify the condition of a degenrate triangle by cheking if the sum of two sides would equal the value of the other side. and if so print degenerate triangle and see if the user still wants to continue or not
    if side_AB + side_BC == side_CA or side_CA +side_BC == side_AB or side_AB + side_CA == side_BC:
        #degenrate triangle
        print("\n\n  Degenerate Triangle" )
        
        
        program_boot= input("\nDo you wish to process another triangle? (Y or N) ").lower()
    # check if the sides verify the condion of a triangle or not by verifying that the values of any two sides would be higher than the other side and promot an input again to see if the user still wishes to continue or not
    elif side_AB + side_BC < side_CA or side_CA +side_BC < side_AB or side_AB + side_CA < side_BC:
        #not a triangle
        print("\n\n  Not a Triangle")
        
        
        program_boot= input("\nDo you wish to process another triangle? (Y or N) ").lower()
    # check if the value of side_AB and the value of side_BC greater than the value of side_CA. if so, then it's must be a valid triangle 
    elif side_AB + side_BC > side_CA:
        #valid triangle
        
        #add an incrementer to see how many valid triangles the use promted, print the sides of the triangle with 1 decimal place
        number_of_valid_triangle += 1
        print("\n\n  Valid Triangle")
        print("\n  Triangle sides:")
        print("    Length of side AB: {:.1f}".format(side_AB))
        print("    Length of side BC: {:.1f}".format(side_BC))
        print("    Length of side CA: {:.1f}".format(side_CA))
        # calculate the preimeter then the S value to apply the area of triangle fourmla that was given in the wikipedia
        perimeter= float(side_AB + side_BC + side_CA)
        s= float(1/2 * perimeter)
        area_of_triangle= math.sqrt(s*(s-side_AB)*(s-side_BC)*(s-side_CA))
        
        
        #calculated angles a and b and c in radian
        angle_a_in_radiant = math.acos(((side_CA)**2 +(side_AB)**2 - (side_BC)**2 )/(2*side_CA * side_AB))
        angle_b_in_radiant = math.acos(((side_BC)**2 +(side_AB)**2 - (side_CA)**2 )/(2*side_BC * side_AB))
        angle_c_in_radiant = math.acos(((side_BC)**2 +(side_CA)**2 - (side_AB)**2 )/(2*side_BC * side_CA))
        #calculated angles a and b and c in degrees
        angle_a_in_degree= angle_a_in_radiant *(180 /math.pi)
        angle_b_in_degree= angle_b_in_radiant *(180 /math.pi)
        angle_c_in_degree= angle_c_in_radiant *(180 /math.pi)
        
        #display the results with one decimal place
        print("\n  Degree measure of interior angles:")
        print("    Angle A: {:.1f}".format(angle_a_in_degree))
        print("    Angle B: {:.1f}".format(angle_b_in_degree))
        print("    Angle C: {:.1f}".format(angle_c_in_degree))
        print("\n  Radian measure of interior angles:")
        print("    Angle A: {:.1f}".format(angle_a_in_radiant))
        print("    Angle B: {:.1f}".format(angle_b_in_radiant))
        print("    Angle C: {:.1f}".format(angle_c_in_radiant))
        print("\n  Perimeter and Area of triangle:")
        print("    Perimeter of triangle: {:.1f}".format(perimeter))
        print("    Area of triangle: {:.1f}".format(area_of_triangle))
        print("\n  Types of triangle:")
        # differentiate the every type of a given triangle based on the sides and the angles that satisfy the condition of every type  
        right_angle= False
        if side_AB != side_BC and side_AB != side_CA and side_BC != side_CA:
            print("    Scalene Triangle")

        if side_AB == side_BC or side_AB == side_CA or side_BC == side_CA:
            print("    Isosceles Triangle")
            
        if side_AB == side_BC and side_AB == side_CA and side_CA == side_BC:
            print("    Equilateral Triangle")
            
        if angle_a_in_degree == 90 or angle_b_in_degree == 90 or angle_c_in_degree == 90:
            print("    Right Triangle")
            right_angle = True
        if right_angle == False:
            print("    Oblique Triangle")
          
        if angle_a_in_degree > 90 or angle_b_in_degree > 90 or angle_c_in_degree > 90:
            print("    Obtuse Triangle")
        # check if the user wants to try another triangle
        program_boot= input("\nDo you wish to process another triangle? (Y or N) ").lower()
        #print the number of how many valid triangles the user have entered
print("\nNumber of valid triangles: {}".format(number_of_valid_triangle))
        
