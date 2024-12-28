// modbus_write.h

#ifndef MODBUS_WRITE_H
#define MODBUS_WRITE_H

#include "esphome.h"

class ModbusWriteComponent : public Component, public UARTDevice {
public:
  ModbusWriteComponent(UARTComponent *parent) : UARTDevice(parent) {}

  // Function to write a value to a Modbus register
  void write_register(uint8_t slave_id, uint16_t reg_address, uint16_t value);

private:
  // CRC16 Calculation
  uint16_t calculate_crc16(uint8_t *data, uint16_t length);
};

#endif // MODBUS_WRITE_H
