class RunnerModel(object):
    def __init__(self, name, height):
        """default height in mm"""
        self.name = name
        self.height = height


class RunnerView(object):
    def __init__(self, model):
        self.model = model

    def output_height_in_m(self):
        print("runner name: " + str(self.model.name))
        print("runner height(m):" + str(self.model.height / 1000))

    def output_height_in_cm(self):
        print("runner name: " + str(self.model.name))
        print("runner height(cm):" + str(self.model.height / 10))


class RunnerController(object):
    def __init__(self, model, measure):
        self.model = model
        self.view = RunnerView(self.model)
        self.measure = measure

    def output(self):
        if self.measure == "m":
            self.view.output_height_in_m()
        elif self.measure == "cm":
            self.view.output_height_in_cm()


if __name__ == "__main__":
    runner_1 = RunnerModel(name="sergey", height=1820)
    controller_1 = RunnerController(runner_1, "cm")
    controller_1.output()
    controller_1 = RunnerController(runner_1, "m")
    controller_1.output()
