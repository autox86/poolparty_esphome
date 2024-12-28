// modbus_write.h

#ifndef MODBUS_WRITE_H
#define MODBUS_WRITE_H

#include "esphome.h"
#include "modbus_controller.h"

namespace esphome {
namespace modbus_write {

class ModbusWrite : public Component {
 public:
  // Constructor that accepts parameters for slave_id, reg_address, and value
  ModbusWrite(int slave_id, uint16_t reg_address, uint16_t value)
      : slave_id_(slave_id), reg_address_(reg_address), value_(value) {}

  // Initialization function
  void setup() override {
    ESP_LOGCONFIG(TAG, "Setting up Modbus write to register %d with value %d", reg_address_, value_);
  }

  // Function to perform the Modbus write operation
  void write_register() {
    ESP_LOGD(TAG, "Writing value %d to register %d on Modbus slave %d", value_, reg_address_, slave_id_);
    // The actual writing to Modbus happens here via the modbus_controller
    if (modbus_controller_ != nullptr) {
      modbus_controller_->write_register(slave_id_, reg_address_, value_);
    }
  }

  // Set the Modbus controller object
  void set_modbus_controller(ModbusController *modbus_controller) {
    modbus_controller_ = modbus_controller;
  }

 private:
  int slave_id_;  // Slave ID for Modbus
  uint16_t reg_address_;  // Register address to write to
  uint16_t value_;  // Value to write to the register
  ModbusController *modbus_controller_ = nullptr;  // The Modbus controller to perform the write action
};

}  // namespace modbus_write
}  // namespace esphome

#endif  // MODBUS_WRITE_H
