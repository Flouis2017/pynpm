import numpy

txt_data = numpy.genfromtxt("C:/Users/Flouis/Desktop/temporary/aaa.txt", delimiter=',', dtype=str, encoding='utf-8')
print(type(txt_data))
print(txt_data)

# print(help(numpy.genfromtxt))

