from database.db import run_bulk_query

def addMachines(machines):
    machines = [(machine,) for machine in machines]
    return run_bulk_query("INSERT", "INSERT INTO Machine (name) VALUES (%s);", machines)

def addAxes(axes):
    axes = [(axis,) for axis in axes]
    return run_bulk_query("INSERT", "INSERT INTO Axis (name) VALUES (%s);", axes)

def addMachineAxisRel(rels):
    return run_bulk_query("INSERT", "INSERT INTO MachineAxisRel (machine_id, axis_id) VALUES (%s, %s);", rels)

def addFieldNames(field_names):
    return run_bulk_query("INSERT", "INSERT INTO Field (machine_axis_rel_id, field_name) VALUES (%s, %s);", field_names)

if __name__ == "__main__":
    print(addAxes(["X", "Y", "Z"]))
