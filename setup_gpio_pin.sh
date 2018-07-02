#!/bin/bash
echo "Setting gpio pin input/output"

if [ "$#" -gt 0 ]; then
  export PIN=$1
  #export PIN_MODE=$2
  export PIN_MODE=out
  echo $1 $2
  if [ ! -e "/sys/class/gpio/gpio$PIN/value" ]; then
    echo $PIN > /sys/class/gpio/export
  fi
  echo $PIN_MODE > /sys/class/gpio/gpio$PIN/direction
else
  echo "source setting_gpio_pin.sh [pin] [mode]"
  echo "[pin]: 0-20"
  echo "[mode]: in/out"
fi
