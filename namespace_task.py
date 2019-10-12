namespaces = {'global': None}
variables = {'global': set()}

def add_command(parent_namespace: str, var_name: str):
    variables[parent_namespace].add(var_name)


def create_command(parent_namespace: str, var_name: str):
    namespaces[var_name] = parent_namespace
    variables[var_name] = set()


def get_command(parent_namespace: str, var_name: str):
    if var_name in variables[parent_namespace]:
        return print(parent_namespace)
    else:
        if parent_namespace == "global":
            return print("None")
        parent_namespace = namespaces[parent_namespace]
        return get_command(parent_namespace, var_name)


n = int(input())
for x in range(n):
    cmd, str1, str2 = input().split()

    parent_namespace = str1
    var_name = str2

    if cmd == "create":
        parent_namespace, var_name = var_name, parent_namespace
        create_command(parent_namespace, var_name)
    elif cmd == "add":
        add_command(parent_namespace, var_name)
    elif cmd == "get":
        get_command(parent_namespace, var_name)

