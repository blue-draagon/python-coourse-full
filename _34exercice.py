class SuperList(list):
    def __len__(self) -> int:
        return 125


super_list = SuperList()
super_list.append(10)
print(super_list[0])
print(len(super_list))
