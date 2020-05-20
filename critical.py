# example file


def critical_method():
    # example method tracked in critical_method_change_notify probe
    return 5


if __name__ == "__main__":
    critical = critical_method()
    print("critical_method returned: " + str(critical))
