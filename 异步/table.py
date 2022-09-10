res = {"asd": 123, "wer": 345}
import prettytable as pt

print_str = pt.PrettyTable()
print_str.field_names = ["True name", "Detect name"]
for key, val in res.items():
    print_str.add_row([key, val])
print(print_str)

print_str = pt.PrettyTable()
print_str.field_names = ["True name", "Detect name"]
res = ['133', True, 234]
for item in res:
    print_str.add_row([item, type(item)])
print(print_str)
