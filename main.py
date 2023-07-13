"""Sum of max and min in an array
   Approach - 1) find max value and min value in same loop
             `2) sum them"""
class Sum():
    @staticmethod
    def sumof_max_min(array):

        minimum_value = float('inf')
        maximum_value = float("-inf")

        for i in range(0, len(array)):

            if maximum_value < array[i]:
                maximum_value = array[i]
            if minimum_value > array[i]:
                minimum_value = array[i]

        return (maximum_value+minimum_value)


instance = Sum()
array = list(map(int, input().split()))
print(instance.sumof_max_min(array))
