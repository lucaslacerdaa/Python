print('Questão 10')

def largest(arr,n):

    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [10, 324, 45, 90, 9808, 5, 200, 900]
n = len(arr)
x = largest(arr,n)
print ("O maior valor é: ", x)