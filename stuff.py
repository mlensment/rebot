import math

elapsed_time = 1000
begin = 20
end = 0
timeframe = 2000

b = begin
c = math.fabs(end - begin)
begin = 0

pos = -c / 2 * (math.cos(math.pi * elapsed_time / timeframe) - 1)

if b > end:
    print math.fabs(pos - b)
else:
    print pos + b


# if b < c:
#     f = b
# else:
#     f = c

# c = math.fabs(end - begin)
# begin = 0

# if begin > end:
#     print 'bla'
#     c = math.fabs(end - begin)
#
# b = begin
# reverse = False
# if begin > end:
#     end = begin
#     begin = 0
#     reverse = True
#
# #0 -> 200
#
# if reverse:
#     print math.fabs(pos - b)
# else:
#     print pos
#
#
# # print begin
# # print end
# print math.fabs(pos - begin) + end

# #vaja oleks 50 -> 250
# print -c / 2 * (math.cos(math.pi * t / d) - 1) + f
#
#
# #vaja oleks 250 -> 50
# pos = -c / 2 * (math.cos(math.pi * t / d) - 1) + f
# c - pos
# print (c - pos + f) +
