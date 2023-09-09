# Create a sample collection
users = {
    'Hans': 'active',
    'Éléonore': 'inactive',
    '景太郎': 'active'
}

for user in users:
    print(user)

print("########################")

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status


for user in users:
    print(user)
