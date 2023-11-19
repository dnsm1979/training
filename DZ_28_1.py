class Computer:
    def __init__(self):
        self.components = {}

    def add_component(self, key, value):
        self.components[key] = value

    def __str__(self):
        return f"Computer with components: {self.components}"


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def configure_processor(self, processor):
        self.computer.add_component("processor", processor)
        return self

    def configure_ram(self, ram):
        self.computer.add_component("ram", ram)
        return self

    def configure_graphics_card(self, graphics_card):
        self.computer.add_component("graphics_card", graphics_card)
        return self

    def configure_motherboard(self, motherboard):
        self.computer.add_component("motherboard", motherboard)
        return self

    def configure_power_unit(self, power_unit):
        self.computer.add_component("power_unit", power_unit)
        return self

    def configure_ssd(self, ssd):
        self.computer.add_component("ssd", ssd)
        return self

    def confugure_computer_case(self, computer_case):
        self.computer.add_component("computer_case", computer_case)
        return self

    def build(self):
        return self.computer


builder = ComputerBuilder()
computer = (
    builder.configure_processor("RYZEN 9 5950X")
    .configure_ram("DDR4 64GB")
    .configure_graphics_card("NVIDIA GTX 3090Ti")
    .configure_motherboard("ASUS X570")
    .configure_power_unit("1000W")
    .configure_ssd("SAMSUNG 2TB")
    .confugure_computer_case("DIPCOOL FULL TOWER")
    .build()
)


print(computer)
list_comp = []
for i in computer.components:
    list_comp.append(computer.components[i])
print(f"Computer configuration: ", ", ".join(list_comp))
print("Computer completed graphics card: ", computer.components["graphics_card"])
