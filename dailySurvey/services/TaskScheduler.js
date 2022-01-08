const cron = require('node-cron');
const surveyController = require("../controllers/SurveyController");

module.exports = {
    scheduleSendEmail: function() {
        console.log("scheduling task...")
        // Schedule tasks to be run on the server.
        cron.schedule('*/10 * * * *', function() {
            console.log('sending email...');
            surveyController.sendSurvey()
        });
    }
}