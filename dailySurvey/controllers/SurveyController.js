const typeorm = require("typeorm")
const crypto = require("crypto");
const emailController = require("./EmailController");
const errorCode = require("../src/util/ErrorCode")

var self = module.exports = {
    generateRandomHash: function() {
        let randomHash = crypto.randomBytes(16).toString("hex")
        return randomHash
    },

    sendSurvey: async function() {
        let conn = typeorm.getConnection()
        try {
            const userRepository = conn.getRepository("User");
            const surveyRepository = conn.getRepository("Survey");
            const allUsers = await userRepository.find();
            for (let i in allUsers) {
                let user = allUsers[i]
                let hash = self.generateRandomHash()
                var survey = {
                    sendDate: new Date(),
                    securityHash: hash,
                    user: user.id
                }
                console.log("saving survey...")
                await surveyRepository.save(survey)
                console.log("sending email...")
                await emailController.send(hash, user)
            }
        } catch (e) {
            console.log(e)
        }
    },

    updateSurvey: async function(survey) {
        let conn = typeorm.getConnection()
        try {
            const surveyRepository = conn.getRepository("Survey");
            const storedSurvey = await surveyRepository.findOne({
                relations: ["user"],
                where:
                    {
                        securityHash: `${survey.uniqueKeyUserSession}`,
                        user: survey.userId
                    }
            })

            self.checkIfCanAnswerSurvey(storedSurvey, survey)
            storedSurvey.q1 = survey.q1
            storedSurvey.q2 = survey.q2
            storedSurvey.q3 = survey.q3
            storedSurvey.answerDate = new Date()
            await surveyRepository.update(storedSurvey.id, storedSurvey)
            return "success"
        } catch (e) {
            console.log(e)
            return e.message
        }
    },

    checkIfCanAnswerSurvey: function(storedSurvey, survey) {
        if (!storedSurvey || storedSurvey.securityHash != survey.uniqueKeyUserSession
            || storedSurvey.user.id != survey.userId) {
            const error = new Error("Error while taking the survey. Please try again later.");
            error.code = errorCode.SECURITY_HASH_OR_USER_ID_MISMATCH_ERROR;
            throw error;
        }
        if (storedSurvey.answerDate != null) {
            const error = new Error("You already take this survey. Please wait for the next.");
            error.code = errorCode.SURVEY_ALREADY_ANSWERED_ERROR;
            throw error;
        }
    }
}