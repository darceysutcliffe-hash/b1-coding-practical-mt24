class PDController:
    def_init__(self,kp=0.15,kd=0.6):
        self.kp = kp
        self.kd = kd
        self.prev_error = 0.0


    def compute(self, reference: float, measurement: float) -> float:
        error = reference - measurement
        control = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        return control