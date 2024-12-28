// modbus_write.cpp

#include "modbus_write.h"
#include "modbus_controller.h"
#include "esphome/log.h"

namespace esphome {
namespace modbus_write {

static const char *TAG = "modbus_write";

void ModbusWrite::setup() {
  ESP_LOGCONFIG(TAG, "Setting up Modbus write to register %d with value %d", reg_address_, value_);
}

void ModbusWrite::write_register() {
  ESP_LOGD(TAG, "Writing value %d to register %d on Modbus slave %d", value_, reg_address_, slave_id_);
  if (modbus_controller_ != nullptr) {
    modbus_controller_->write_register(slave_id_, reg_address_, value_);
  } else {
    ESP_LOGE(TAG, "Modbus controller not initialized!");
  }
}

}  // namespace modbus_write
}  // namespace esphome
