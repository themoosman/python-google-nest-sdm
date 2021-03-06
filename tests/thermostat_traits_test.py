from google_nest_sdm.device import Device


def test_thermostat_eco_traits():
    raw = {
        "name": "my/device/name",
        "traits": {
            "sdm.devices.traits.ThermostatEco": {
                "availableModes": ["MANUAL_ECHO", "OFF"],
                "mode": "MANUAL_ECHO",
                "heatCelsius": 20.0,
                "coolCelsius": 22.0,
            },
        },
    }
    device = Device.MakeDevice(raw, auth=None)
    assert "sdm.devices.traits.ThermostatEco" in device.traits
    trait = device.traits["sdm.devices.traits.ThermostatEco"]
    assert ["MANUAL_ECHO", "OFF"] == trait.available_modes
    assert "MANUAL_ECHO" == trait.mode
    assert 20.0 == trait.heat_celsius
    assert 22.0 == trait.cool_celsius


def test_thermostat_hvac_traits():
    raw = {
        "name": "my/device/name",
        "traits": {
            "sdm.devices.traits.ThermostatHvac": {
                "status": "HEATING",
            },
        },
    }
    device = Device.MakeDevice(raw, auth=None)
    assert "sdm.devices.traits.ThermostatHvac" in device.traits
    trait = device.traits["sdm.devices.traits.ThermostatHvac"]
    assert "HEATING" == trait.status


def test_thermostat_mode_traits():
    raw = {
        "name": "my/device/name",
        "traits": {
            "sdm.devices.traits.ThermostatMode": {
                "availableModes": ["HEAT", "COOL", "HEATCOOL", "OFF"],
                "mode": "COOL",
            },
        },
    }
    device = Device.MakeDevice(raw, auth=None)
    assert "sdm.devices.traits.ThermostatMode" in device.traits
    trait = device.traits["sdm.devices.traits.ThermostatMode"]
    assert ["HEAT", "COOL", "HEATCOOL", "OFF"] == trait.available_modes
    assert "COOL" == trait.mode


def test_thermostat_temperature_setpoint_traits():
    raw = {
        "name": "my/device/name",
        "traits": {
            "sdm.devices.traits.ThermostatTemperatureSetpoint": {
                "heatCelsius": 20.0,
                "coolCelsius": 22.0,
            },
        },
    }
    device = Device.MakeDevice(raw, auth=None)
    assert "sdm.devices.traits.ThermostatTemperatureSetpoint" in device.traits
    trait = device.traits["sdm.devices.traits.ThermostatTemperatureSetpoint"]
    assert 20.0 == trait.heat_celsius
    assert 22.0 == trait.cool_celsius


def test_thermostat_multiple_traits():
    raw = {
        "name": "my/device/name",
        "traits": {
            "sdm.devices.traits.ThermostatEco": {
                "availableModes": ["MANUAL_ECHO", "OFF"],
                "mode": "MANUAL_ECHO",
                "heatCelsius": 21.0,
                "coolCelsius": 22.0,
            },
            "sdm.devices.traits.ThermostatHvac": {
                "status": "HEATING",
            },
            "sdm.devices.traits.ThermostatMode": {
                "availableModes": ["HEAT", "COOL", "HEATCOOL", "OFF"],
                "mode": "COOL",
            },
            "sdm.devices.traits.ThermostatTemperatureSetpoint": {
                "heatCelsius": 23.0,
                "coolCelsius": 24.0,
            },
        },
    }
    device = Device.MakeDevice(raw, auth=None)
    assert "sdm.devices.traits.ThermostatEco" in device.traits
    assert "sdm.devices.traits.ThermostatHvac" in device.traits
    assert "sdm.devices.traits.ThermostatMode" in device.traits
    assert "sdm.devices.traits.ThermostatTemperatureSetpoint" in device.traits
    trait = device.traits["sdm.devices.traits.ThermostatEco"]
    assert ["MANUAL_ECHO", "OFF"] == trait.available_modes
    assert "MANUAL_ECHO" == trait.mode
    assert 21.0 == trait.heat_celsius
    assert 22.0 == trait.cool_celsius
    trait = device.traits["sdm.devices.traits.ThermostatHvac"]
    assert "HEATING" == trait.status
    trait = device.traits["sdm.devices.traits.ThermostatMode"]
    assert ["HEAT", "COOL", "HEATCOOL", "OFF"] == trait.available_modes
    assert "COOL" == trait.mode
    trait = device.traits["sdm.devices.traits.ThermostatTemperatureSetpoint"]
    assert 23.0 == trait.heat_celsius
    assert 24.0 == trait.cool_celsius
