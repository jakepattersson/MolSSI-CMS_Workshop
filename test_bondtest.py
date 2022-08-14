import geom_analysis as ga

def test_bond_check_true():
    atom_distance = 1
    expected = True
    observed = ga.bond_check(atom_distance)
    assert observed == expected

def test_bond_check_false():
    atom_distance = 2.0
    expected = False
    observed = ga.bond_check(atom_distance)
    assert observed == expected

def test_bond_check_0():
    atom_distance = 0
    expected = False
    observed = ga.bond_check(atom_distance)
    assert observed == expected

def test_bond_check_1_5():
    atom_distance = 1.5
    expected = True
    observed = ga.bond_check(atom_distance)
    assert observed == expected    
