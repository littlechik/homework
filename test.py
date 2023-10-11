def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 將列表分成兩半
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 遞迴排序左半部分和右半部分
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # 將排序好的兩部分合併成一個有序的列表
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # 將剩餘的元素加入結果列表
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

# 測試
my_list = [5, 2, 4, 6, 1, 3]
sorted_list = merge_sort(my_list)
print("Sorted List:", sorted_list)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs_paths(node, target, path=[]):
    path = path + [node]  # 將當前節點添加到路徑中
    if node == target:
        return [path]  # 找到目標節點，返回路徑
    if node not in graph:
        return []  # 節點不在圖中，返回空列表
    paths = []
    for neighbor in graph[node]:
        if neighbor not in path:
            new_paths = dfs_paths(neighbor, target, path)
            paths.extend(new_paths)
    return paths

# 從節點 'A' 到節點 'F' 的所有路徑
all_paths = dfs_paths('A', 'F')

# 顯示所有路徑
for path in all_paths:
    print("->".join(path))
    print(path)

