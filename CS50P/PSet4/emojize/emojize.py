from emoji import emojize

input = input("Input: ").strip()
print(f"output: {emojize(input, language='alias')}")
