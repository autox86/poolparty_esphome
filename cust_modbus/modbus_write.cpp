// modbus_write.cpp

#include "modbus_write.h"

void ModbusWriteComponent::write_register(uint8_t slave_id, uint16_t reg_address, uint16_t value) {
  uint8_t frame[8];

  // Construct Modbus RTU frame
  frame[0] = slave_id; // Slave address
  frame[1] = 0x06; // Function code: Write Single Register
  frame[2] = (reg_address >> 8) & 0xFF; // High byte of register address
  frame[3] = reg_address & 0xFF; // Low byte of register address
  frame[4] = (value >> 8) & 0xFF; // High byte of value
  frame[5] = value & 0xFF; // Low byte of value

  // Calculate CRC16
  uint16_t crc = calculate_crc16(frame, 6);
  frame[6] = crc & 0xFF; // Low byte of CRC
  frame[7] = (crc >> 8) & 0xFF; // High byte of CRC

  // Send frame over UART
  for (int i = 0; i < 8; i++) {
    this->write(frame[i]);
  }
}

// CRC16 Calculation
uint16_t ModbusWriteComponent::calculate_crc16(uint8_t *data, uint16_t length) {
  uint16_t crc = 0xFFFF;
  for (uint16_t i = 0; i < length; i++) {
    crc ^= data[i];
    for (uint8_t j = 0; j < 8; j++) {
      if (crc & 0x0001) {
        crc >>= 1;
        crc ^= 0xA001;
      } else {
        crc >>= 1;
      }
    }
  }
  return crc;
}
