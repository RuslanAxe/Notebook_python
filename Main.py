from controller.Controller import Controller
from model.Model import Model
from views.ConsoleUI import ConsoleUI


model: Model = Model()
view: ConsoleUI = ConsoleUI()
controller: Controller = Controller(model=model, view=view)

controller.start_app()