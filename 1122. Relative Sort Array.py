class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        result = []
        for num in arr2:
            if num in count:
                for i in range(count[num]):
                    result.append(num)
                del count[num]
        remaining_elements = sorted(count.elements())
        result.extend(remaining_elements)
        
        return result
