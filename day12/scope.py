
x = 5


def local_scope():
    """
    local scope
    """
    x = 10
    print(f"Local scope: {x}")


def change_global():
    """
    change global value in local scope
    """
    global x
    x = 2
    print(f"Local scope: {x}")


if __name__ == "__main__":
    local_scope()
    print(f"global scope: {x}")
    change_global()
    print(f"global scope: {x}")
    pass
