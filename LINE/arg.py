# import sys
 
# print("the name of script is :", sys.argv[0])
# print("the number of arg is :", len(sys.argv))
# print(sys.argv)
# print(type(sys.argv))
# for arg in sys.argv:
#     print(arg)

# **********************************************
import sys
 
def main(argv):
 
    print ("the name of script is :", sys.argv[0])
    print ("the number of original arg is :", len(sys.argv))
    print ("the number of altered arg is :", len(argv))
 
    for arg in argv:
        print (arg)
 
if __name__ == "__main__":
    main(sys.argv[1:])