from swampy.Lumpy import Lumpy


lumpy = Lumpy()
lumpy.make_reference()

message = 'ываываыва'
n = 17
pi = 3.1415926535897932

lumpy.object_diagram()


def countdown(n):
    lumpy.object_diagram()
    if n <= 0:
        print ('Blastoff!')
    else:
        print (n)
        countdown(n-1)

lumpy = Lumpy()
lumpy.make_reference()
countdown(3)