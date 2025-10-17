class PDController:
    """
    Discrete-time PD controller:
      u[t] = KP * e[t] + KD * (e[t] - e[t-1])
    where e[t] = reference - measurement.
    KP and KD are configurable.
    """
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = float(kp)
        self.kd = float(kd)
        self.prev_error = 0.0

    def reset_state(self) -> None:
        self.prev_error = 0.0

    def compute(self, reference: float, measurement: float) -> float:
        """
        Compute control action for a single discrete time step.
        """
        error = float(reference) - float(measurement)
        action = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        return action