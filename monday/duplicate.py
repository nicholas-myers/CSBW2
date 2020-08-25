class Double_Linked_list:
    def __init__(self, value, prev = None, nex = None):
        self.value = value
        self.prev = prev
        self.next = nex
        
    def
    
def containsDuplicate(nums) -> bool:
    dupes = {}
    while len(nums) > 0:
        if nums[0] not in dupes:
            dupes[nums[0]] = nums[0]
            nums.pop(0)
        else:
            return True
    return False
containsDuplicate([1,3,4,2])