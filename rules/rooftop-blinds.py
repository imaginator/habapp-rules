from bdb import Breakpoint
import logging
import time
from HABApp import Rule
from HABApp.core.events import ValueUpdateEvent, ValueChangeEvent
from HABApp.openhab.events import ItemStateChangedEvent,ItemStateChangedEventFilter
from HABApp.openhab.items import NumberItem, OpenhabItem
from HABApp.core.errors import ItemNotFoundException

log = logging.getLogger('HABAppLogger')

class MyRule(Rule):
    deffrom bdb import Breakpoint
import logging
import time
from HABApp import Rule
from HABApp.core.events import ValueUpdateEvent, ValueChangeEvent
from HABApp.openhab.events import ItemStateChangedEvent,ItemStateChangedEventFilter
from HABApp.openhab.items import NumberItem, OpenhabItem
from HABApp.core.errors import ItemNotFoundException

log = logging.getLogger('HABAppLogger')

class MyRule(Rule):
    def __init__(self):
        super().__init__()
        try: 
            self.rooftop_window_position = OpenhabItem.get_item('gRooftopWindows')
            self.rooftop_blind_position  = OpenhabItem.get_item('gHallwayBlinds')
            self.sun_elevation_postition = OpenhabItem.get_item('AstroSunPositionElevation')
        except ItemNotFoundException as e:
            log.warning(f"WARNING: item not found, raised {e}")
            return
        self.sun_elevation_postition.listen_event(self.item_changed, ItemStateChangedEventFilter())

    def item_changed(self, event: ItemStateChangedEvent):
        if self.rooftop_blind_position.value == "100":
            log.info("Blinds are already closed")
            print("PRINT Blinds are already closed")
            return 
        sun_angle_position = float(event.value)
        if 40 > sun_angle_position < 48:
            if self.rooftop_window_position.value != "100":
                self.rooftop_window_position.send_command("gRooftopWindows", "DOWN")
                time.sleep(20)
            self.rooftop_blind_position.send_command("gHallwayBlinds", "DOWN")
            log.info("Blinds are closed.")
        return
 
MyRule()
 __init__(self):
        super().__init__()
        try: 
            self.rooftop_window_position = OpenhabItem.get_item('gRooftopWindows')
            self.rooftop_blind_position  = OpenhabItem.get_item('gHallwayBlinds')
            self.sun_elevation_postition = OpenhabItem.get_item('AstroSunPositionElevation')
        except ItemNotFoundException as e:
            log.warning(f"WARNING: item not found, raised {e}")
            return
        self.sun_elevation_postition.listen_event(self.item_changed, ItemStateChangedEventFilter())

    def item_changed(self, event: ItemStateChangedEvent):
        if self.rooftop_blind_position.value == "100":
            log.info("Blinds are already closed")
            print("PRINT Blinds are already closed")
            return 
        sun_angle_position = float(event.value)
        if 40 > sun_angle_position < 48:
            if self.rooftop_window_position.value != "100":
                self.rooftop_window_position.send_command("gRooftopWindows", "DOWN")
                time.sleep(20)
            self.rooftop_blind_position.send_command("gHallwayBlinds", "DOWN")
            log.info("Blinds are closed.")
        return
 
MyRule()
