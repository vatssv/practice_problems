import copy
class Solution:
    def __init__(self):
        pass

    def permute(self, nums):
        nums.sort()
        all_permutations = []
        all_permutations.append(nums)
        # print('Before while loop: ', all_permutations)
        while(True):
            next_combo = []
            curr = copy.deepcopy(all_permutations[-1])
            next_combo = self.next_permute(curr)
            # print('Next combo is: ', next_combo)
            # print('All permute before append: ', all_permutations)
            if next_combo is None:
                break
            else:
                all_permutations.append(next_combo)
            # print('All permute after append: ', all_permutations)
        # print('After while loop: ', all_permutations)
        return all_permutations
    
    def next_permute(self, curr = []):
        k = 999
        l = 999
        # print('Finding next permutation for current list: ', curr)
        for i in range(len(curr)-2, -1, -1):
            if curr[i] < curr[i+1]:
                k = i
                # print('Curr before any swapping is: ', curr)
                for j in range(len(curr)-1, k, -1):
                    if curr[k] < curr[j]:
                        l = j
                        break
                curr[k], curr[l] = curr[l], curr[k]
                # print('Curr after swapping is: ', curr)
                curr_1 = curr[0:k+1]
                curr_2 = curr[k+1:len(curr)]
                # print('Curr 2 before reversing is: ', curr_2)
                curr_2.reverse()
                # print('Curr 2 after reversing is: ', curr_2)
                curr = curr_1 + curr_2
                # print('The result for this one is: ', curr)
                return curr
            else:
                continue
        
        # print('The result for this one is: ', None)
        return None
        
def main():
    nums = [1, 2, 3]
    sol = Solution()
    res = sol.permute(nums)
    print('Res: ', res)

if __name__ == '__main__':
    main()