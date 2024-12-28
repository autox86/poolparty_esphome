# __init__.py for modbus_write component

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import modbus
from esphome.const import CONF_ID, CONF_REGISTER, CONF_VALUE

# Define the unique component ID
CONF_MODBUS_WRITE = "modbus_write"

# Create the configuration schema
modbus_write_schema = cv.Schema({
    cv.Required(CONF_ID): cv.declare_id(modbus.ModbusController),
    cv.Required(CONF_REGISTER): cv.uint16_t,  # register address should be 16-bit
    cv.Required(CONF_VALUE): cv.uint16_t,  # value to write
}).extend(cv.COMPONENT_SCHEMA)

# Register the component and validate it
def setup_modbus_write(config):
    modbus_write = cg.new_component(config)
    modbus_write.id = config[CONF_ID]
    modbus_write.register = config[CONF_REGISTER]
    modbus_write.value = config[CONF_VALUE]
    return modbus_write

# Define the component for ESPHome
def validate_modbus_write(config):
    return modbus_write_schema(config)
