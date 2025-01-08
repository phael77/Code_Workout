def missing_number(nums):
    n = max(nums)
    total = n * (n + 1) // 2  
    sum_nums = sum(nums)  
    return total - sum_nums if total - sum_nums > 0 else n + 1

nums = input("Digite uma sequência de números separados por vírgula, de 0 a n (ex.: 0,1,3): ")

nums = list(map(int, nums.split(',')))

missing = missing_number(nums)
print(f"O número que está faltando é: {missing}")
