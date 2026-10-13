"""The rover's drive. Every move is gated on the e-stop being armed."""

from gpiozero import Motor, Robot

import config


class Rover:
    def __init__(self, estop, motor_a=config.MOTOR_A, motor_b=config.MOTOR_B):
        self._robot = Robot(left=Motor(**motor_a), right=Motor(**motor_b))
        self._estop = estop

    def forward(self, speed=config.SPEED):
        self._drive(self._robot.forward, speed)

    def backward(self, speed=config.SPEED):
        self._drive(self._robot.backward, speed)

    def left(self, speed=config.SPEED):
        self._drive(self._robot.left, speed)

    def right(self, speed=config.SPEED):
        self._drive(self._robot.right, speed)

    def stop(self):
        self._robot.stop()

    def _drive(self, action, speed):
        if not self._estop.armed:
            return
        action(speed)
