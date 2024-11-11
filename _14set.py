# a set is a unordered collection of unique list element
# set in math mean "ensemble"
my_set = {1,2,2,2,2,2,3,4,5}
print(my_set )
# no duplicate value
print(type(my_set))
my_set.add(100)
print(my_set)
my_set.add(3)
print(my_set)

# set can be use to remove duplicate on list
my_list = [1,1,1,1,2,2,2,2,3,3,3,3]
no_duplicate = set(my_list)
print(my_list)
print(no_duplicate)

# check exist
print(1 in my_set)
# element of set can be access individualy

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
# diffrence : value on firts but not in second : A minus B
print(set1.difference(set2))
# discartd : difference of single value : A / {x} : update the set
print(set1.discard(5))
print(set1)
set1.add(5)
# diffrence_update : same like difference but update the set
print(set1.difference_update(set2))
print(set1)
set1.add(4)
set1.add(5)
set1.add(6)
# intersection : value on firts tha is on second : A inter B
print(set1.intersection(set2))
# intersection can be done with &
print(set1 & set2)
# isdisjoint : test if 2 set dont have any same value
print(set1.isdisjoint(set2))
# union : associate to set
print(set1.union(set2))
union_set = set1.union(set2)
print(union_set)
# union can be set with | 
print(set1 | set2)
# issubset : all value of firts is on second
print(set1.issubset(union_set))
# issuperset : if firts contains all value of on second
print(set1.issubset(union_set))
