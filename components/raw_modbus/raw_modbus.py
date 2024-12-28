import esphome.codegen as cg
from esphome.components import uart
from esphome import pins
from esphome.const import CONF_ID
from .modbus_write import ModbusWrite
import struct

# Declare the component type and register it
DEPENDENCIES = ["uart"]

modbus_write_ns = cg.esphome_ns.namespace("modbus_write")
ModbusWrite = modbus_write_ns.class_("ModbusWrite", cg.Component)

# Function to calculate the CRC-16-ANSI checksum
def calculate_crc(data):
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return struct.pack("<H", crc)

# Function to send raw Modbus data with CRC
@cg.export
def send_raw_modbus_data(modbus_write, data):
    crc = calculate_crc(data)
    data.extend(crc)
    uart.write_bytes(modbus_write.uart_id, data)
    _LOGGER.info(f"Sending Modbus data: {data}")
