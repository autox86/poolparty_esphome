import esphome.codegen as cg
from esphome import config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID, CONF_ADDRESS, CONF_SLAVE, CONF_VALUE
import logging

_LOGGER = logging.getLogger(__name__)

# Define the Modbus component ID and configuration
CONF_MODBUS_ID = "modbus_id"
CONF_MODBUS_WRITE = "modbus_write"

# Configuration schema for the component
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(),
    cv.Required(CONF_SLAVE): cv.positive_int,
    cv.Required(CONF_ADDRESS): cv.positive_int,
    CONF_VALUE: cv.Optional(cv.positive_int, default=1),
}).extend(uart.UART_DEVICE_SCHEMA)

def to_code(config):
    """This function will convert the configuration to code."""
    modbus_write = cg.new_Pvariable(config[CONF_ID])
    cg.add(modbus_write.set_slave(config[CONF_SLAVE]))
    cg.add(modbus_write.set_address(config[CONF_ADDRESS]))
    cg.add(modbus_write.set_value(config[CONF_VALUE]))
    return modbus_write
