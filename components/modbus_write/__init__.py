# __init__.py for modbus_write component
from esphome import esphomeyaml
from esphome.core import Component
from esphome.components import uart

#manually
import esphome.codegen as cg
import esphome.config_validation as cv

# Import your component-specific classes or functions
# (Make sure this matches the actual code you have for Modbus)
from esphome.components.modbus import ModbusRTU

# Define the setup of your component
def setup_modbus_write_component(config):
    """
    Configure and set up the modbus_write component.
    """
    # Ensure that UART and Modbus are set up
    uart_config = uart.UARTComponent(config.get('uart'), config)
    modbus_component = ModbusRTU(config)
    return modbus_component

# Validate configuration for your modbus_write component
def validate_modbus_write_config(config):
    """
    Validate the configuration for modbus_write.
    """
    if not config.get('uart'):
        raise esphomeyaml.InvalidConfigurationError('UART configuration is required for Modbus write.')

    return config

# Register the component with ESPHome
esphomeyaml.register_component('modbus_write', setup_modbus_write_component, validate_modbus_write_config)
