# __init__.py for modbus_write component
from esphome import esphomeyaml
from esphome.core import Component
from esphome.components import uart

# Import the core functionality of your Modbus component
from esphome.components.modbus import ModbusRTU

# Define the setup of the component, this might include initialization of UART, Modbus, etc.
def setup_modbus_write_component(config):
    """
    Function to configure and register the ModbusWrite component.
    It integrates your modbus write functionality with ESPHome.
    """
    # Register your component in ESPHome configuration here
    uart_config = uart.UARTComponent(config.get('uart'), config)
    modbus_component = ModbusRTU(config)
    return modbus_component

# Define the schema for your component's configuration (validation)
def validate_modbus_write_config(config):
    """
    Function to validate the configuration for modbus_write.
    You can add your specific configuration validation here.
    """
    # Example: Validate required configuration fields
    if not config.get('uart'):
        raise esphomeyaml.InvalidConfigurationError('UART configuration is required for Modbus write.')

    return config

# Register the component for ESPHome integration
esphomeyaml.register_component('modbus_write', setup_modbus_write_component, validate_modbus_write_config)
