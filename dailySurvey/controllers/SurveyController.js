const typeorm = require("typeorm")
const crypto = require("crypto");
const emailController = require("./EmailController");

var self = module.exports = {
    generateRandomHash: function() {
        let randomHash = crypto.randomBytes(10).toString("hex")
        return randomHash
    },

    sendSurvey: function() {
        const connection = typeorm.createConnection();
        connection.then(async function (conn) {
            const userRepository = conn.getRepository("User");
            const surveyRepository = conn.getRepository("Survey");
            const allUsers = await userRepository.find();
            try {
                for (let i in allUsers) {
                    let user = allUsers[i]
                    let hash = self.generateRandomHash()
                    var survey = {
                        sendDate: new Date(),
                        securityHash: hash,
                        userId: user.id
                    }
                    surveyRepository.save(survey)
                    console.log("sending email...")
                    await emailController.send(hash, user)
                }
            } catch (e) {
                console.log(e)
            }
        })
    }
}