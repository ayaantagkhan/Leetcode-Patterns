
from patterns import(
binary_search,
two_pointers
)

def main():
    items = [0,1,2,3,4,5,6]
    target = 5

    # result = binary_search(items, target)
    # print(f"Our target {target} was found")
    result = two_pointers(items, target)
    if result is not None:
        left, right = result
    print(f"These are the indexes that give us {left, right}")




if __name__ == "__main__":
    main()