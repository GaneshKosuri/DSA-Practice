# --EASY--
# https://leetcode.com/problems/count-items-matching-a-rule/description/


# Solution starts
def countMatches(items,ruleKey,ruleValue):
    column = 0 if ruleKey == 'type' else 1 if ruleKey == 'color' else 2
    items_count = 0
    for row in items:
        if(row[column] == ruleValue):
            items_count += 1
    return items_count

# Solution ends

# For Demo purpose
size = int(input("Enter Array Size : "))
items = []
for i in range(0,size):
    items.append(list(input("Enter the type, color, name of item {} : ".format((i+1))).strip().split())[:size])
rule_key = input("Enter rule Key : ")
rule_value = input("Enter rule value : ")
print(countMatches(items,rule_key,rule_value))