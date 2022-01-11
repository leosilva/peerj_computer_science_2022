const cron = require('node-cron');
const surveyController = require("../controllers/SurveyController");

module.exports = {
    scheduleSendEmail: function() {
        console.log("scheduling task...")
        // Schedule tasks to be run on the server.
        cron.schedule('0 8 * * *', function() {
            console.log('sending email at 8AM...');
            surveyController.sendSurvey()
        });

        cron.schedule('0 14 * * *', function() {
            console.log('sending email at 14PM...');
            surveyController.sendSurvey()
        });
    }
}