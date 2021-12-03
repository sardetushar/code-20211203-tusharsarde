from bmi.unit_conversion import cm_to_meter_sq
import pytest


def test_cm_to_meter():
    val_in_cm = 180
    expected = 3.24
    res = cm_to_meter_sq(val_in_cm)
    assert res == expected

    with pytest.raises(TypeError):
        val_in_cm = ''
        res = cm_to_meter_sq(val_in_cm)
        assert res == expected
