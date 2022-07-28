def solution(numbers, target):
    answer = 0
    def dfs(index):
        if index < len(numbers):
            numbers[index] *= 1
            dfs(index + 1)

            numbers[index] *= -1
            dfs(index + 1)
        elif sum(numbers) == target:
            nonlocal answer
            answer += 1
            
    dfs(0)
    return answer

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers,target))