
import  {Sensors} from "../collections/collections";

Template.sensorTable.helpers({
    sensors:function() {
        return Sensors.find();
    }});

Template.sensorRow.helpers({
    datetime:function() {
        return Date(Template.currentData().timestamp);
    }});