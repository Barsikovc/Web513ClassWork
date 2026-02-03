from platform import platform, machine, processor, system, version

print(platform())
# print(platform(aliased=False, terse=False))
# print(platform(aliased=True, terse=False))
# print(platform(aliased=False, terse=True))
# print(platform(aliased=True, terse=True))
print(machine())
print(processor())
print(system())
print(version())
