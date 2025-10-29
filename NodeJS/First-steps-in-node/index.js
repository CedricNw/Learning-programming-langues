const {add, substract, name} = require("./mathOperations.js")
const {currentDate, currentYear} = require("./logger.js");

function printMessage(msg) {
    console.log(msg);
}

printMessage(currentDate() + currentYear());