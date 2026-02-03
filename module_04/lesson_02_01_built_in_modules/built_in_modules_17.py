from platform import python_version_tuple, python_implementation


print(python_implementation())
print(python_version_tuple())
print(python_implementation(), '.'.join(python_version_tuple()))
