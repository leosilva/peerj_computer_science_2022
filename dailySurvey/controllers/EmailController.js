"use scrict"
var path = require("path")

const surveyTemplate = require("../views/survey/survey")

module.exports = {
    send: async function(randomHash, user) {
        // Generate test SMTP service account from ethereal.email
        // Only needed if you don't have a real mail account testing
        // let testAccount = await nodemailer.createTestAccount()

        // create reusable transporter object using the default SMTP transport
        let transporter = nodemailer.createTransport({
            host: "smtp.mail.me.com",
            port: 587,
            secure: false, // true for 465, false for other ports
            auth: {
                user: "leo.moreira@me.com",
                pass: "oibo-zbfk-jchu-fife"
            }
        })

        let info = await transporter.sendMail({
            from: "leo.moreira@me.com",
            to: user.email,
            subject: "Daily Survey - University of Coimbra Research",
            html: surveyTemplate.getTemplate(randomHash, user.id, false),
            attachments: [
                {
                    filename: 'very-unhappy.png',
                    path: path.resolve() + '/images/very-unhappy.png',
                    cid: 'very-unhappy' // should be as unique as possible
                },
                {
                    filename: 'unhappy.png',
                    path: path.resolve() + '/images/unhappy.png',
                    cid: 'unhappy' // should be as unique as possible
                },
                {
                    filename: 'neutral.png',
                    path: path.resolve() + '/images/neutral.png',
                    cid: 'neutral' // should be as unique as possible
                },
                {
                    filename: 'happy.png',
                    path: path.resolve() + '/images/happy.png',
                    cid: 'happy' // should be as unique as possible
                },
                {
                    filename: 'very-happy.png',
                    path: path.resolve() + '/images/very-happy.png',
                    cid: 'very-happy' // should be as unique as possible
                },
                {
                    filename: 'uc.pt.png',
                    path: path.resolve() + '/images/uc.pt.png',
                    cid: 'uc-logo' // should be as unique as possible
                }
            ]
        })

        // console.log("Message sent: %s", info.messageId)
        // console.log("Preview URL: %s", nodemailer.getTestMessageUrl(info))
    }
}

const nodemailer = require("nodemailer")
