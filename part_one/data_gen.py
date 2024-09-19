import random, query


def gen_machines(count):
    machine_names = ["MACHINE" + str(idx) for idx in range(1, count + 1)]
    query.addMachines(machine_names)


def gen_axes():
    axes_names = ["X", "Y", "Z", "A", "C"]
    query.addAxes(axes_names)


def populate_machine_axis_rel():
    # choose your relevant ids when populating
    query.addMachineAxisRel([(m, a) for a in range(1, 5 + 1) for m in range(5, 24 + 1)])


def gen_field_names():
    fields = {
        "tool_capacity": [24],
        "tool_offset": {"interval": 15 * 1000, "range": range(5, 40 + 1)},
        "feedrate": {"interval": 15 * 1000, "range": range(0, 20000 + 1)},
        "tool_in_use": {"interval": 15 * 1000, "range": range(5, 40)},
    }
    print([
            (ma_id, field_name, random.choice(fields[field_name]))
            for field_name in fields.keys()
            for ma_id in range(1, 100 + 1)
        ])
    # query.addFieldNames(
    #     [
    #         (ma_id, field, )
    #         for field_name in fields.keys()
    #         for ma_id in range(1, 100 + 1)
    #     ]
    # )


def main():
    # genMachines()
    # genAxes()
    gen_field_names()
    pass


if __name__ == "__main__":
    main()
