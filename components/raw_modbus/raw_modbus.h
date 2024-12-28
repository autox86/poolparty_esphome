#pragma once

#include "esphome/core/component.h"
#include "esphome/core/uart.h"

namespace esphome {
namespace modbus_write {

class ModbusWrite : public Component {
 public:
  void set_slave(uint8_t slave) { slave_ = slave; }
  void set_address(uint16_t address) { address_ = address; }
  void set_value(uint16_t value) { value_ = value; }

  void send_raw(std::vector<uint8_t> data);

 protected:
  uint8_t slave_;
  uint16_t address_;
  uint16_t value_;
  uart::UARTComponent *uart_id_;
};

}  // namespace modbus_write
}  // namespace esphome
