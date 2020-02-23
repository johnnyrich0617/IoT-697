import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';


export const Sensors = new Mongo.Collection('sensors');

if (Meteor.isClient) {
    Meteor.subscribe('allSensors');
}

if(Meteor.isServer) {
        Meteor.publish('allSensors',function() {
            // only publish when logged-in users request publishing
            if(this.userId) {
                return[Sensors.find()];
            }
        });
    }